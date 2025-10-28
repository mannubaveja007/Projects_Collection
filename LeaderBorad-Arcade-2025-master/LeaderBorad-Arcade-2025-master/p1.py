"""event_extractor.py

Requirements:
  pip install requests beautifulsoup4 python-dateutil

Usage:
  - Set AZURE_OPENAI_API_KEY, AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_API_VERSION, AZURE_OPENAI_DEPLOYMENT
    in your environment or update the placeholders below.
  - Run: python event_extractor.py "https://example.com/some-event-page"
"""

import os
import re
import json
import sys
import requests
from bs4 import BeautifulSoup
from dateutil import parser as dateparser
from typing import Optional, Dict, Any
import sys
import requests
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError


# Replace this import if your Azure client class lives elsewhere.
# The snippet below assumes you have the AzureOpenAI client with the same interface used earlier.
try:
    from openai import AzureOpenAI
except Exception:
    # If your environment uses a different package, make sure to import your AzureOpenAI wrapper.
    AzureOpenAI = None

# ---------------- CONFIG ----------------
AZURE_OPENAI_API_KEY = "d3c367c33e3f44338f91b767283cc15b"
AZURE_OPENAI_ENDPOINT = "https://api-code-gen.openai.azure.com/"  # ends with /. Example: https://myres.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT = (
    "gpt-35-turbo-Code-Generator"  # e.g. gpt-35-turbo or custom name you set
)
AZURE_OPENAI_API_VERSION = "2024-12-01-preview"
# Schema to match (as dict for easy merging)
SCHEMA = {
    "title": "",
    "slug": "",
    "short_description": "",
    "description": "",
    "type": "external",
    "start_datetime": "",
    "end_datetime": "",
    "location": "",
    "organizer_name": "",
    "event_url": "",
    "contact_email": "",
    "status": "pending",
    "is_public": False,
    "is_featured": False,
    "tags": [],
    "created_at": "",
    "updated_at": "",
}

SCHEMA_JSON = json.dumps(SCHEMA, ensure_ascii=False)

PROMPT_TEMPLATE = f"""You are a precise data extraction assistant.
Return ONLY a single JSON object (no extra text) exactly matching this schema:

{SCHEMA_JSON}

Rules:
- Fill fields when you can extract them from the provided text.
- If a field is unknown, leave it empty (or false / [] as appropriate).
- Use ISO 8601 for datetimes if you can parse them (e.g. 2025-08-21T18:00:00+05:30).
- Do NOT add explanation text or any other output.
TEXT START
{{text}}
TEXT END
"""

JSON_PATTERN = re.compile(r"\{[\s\S]*\}")


# ---------------- AZURE CLIENT ----------------
def make_azure_client():
    if AzureOpenAI is None:
        return None
    return AzureOpenAI(
        api_key=AZURE_OPENAI_API_KEY,
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        api_version=AZURE_OPENAI_API_VERSION,
    )


# ---------------- UTIL ----------------


def fetch_html(url: str, timeout: int = 30, use_playwright: bool = True) -> str:
    """
    Try requests first; if the response looks like an SPA shell or is too small,
    render with Playwright (Chromium) and return the rendered HTML.
    """
    try:
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
        r.raise_for_status()
        text = r.text
    except Exception:
        text = ""

    # SPA detection: use lowercase comparison for reliability
    lowered = (text or "").lower()
    spa_indicators = [
        '<div id="root">',
        'id="__next"',  # Next.js
        "window.env",  # our SPA bootstrap script
        '<script type="module" crossorigin src=',
    ]
    needs_render = False
    if not text or len(text) < 2000:
        needs_render = True
    else:
        # check indicators in lowercase HTML
        if any(indicator in lowered for indicator in spa_indicators):
            needs_render = True

    if not needs_render or not use_playwright:
        return text

    # Render with Playwright
    try:
        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=True)
            page = browser.new_page()
            try:
                page.goto(url, timeout=timeout * 1000, wait_until="networkidle")
            except PlaywrightTimeoutError:
                # fallback: try again with looser waiting
                try:
                    page.goto(url, timeout=(timeout * 1000))
                    page.wait_for_load_state("networkidle", timeout=5000)
                except Exception:
                    pass
            # Optional: wait for a selector if you know a reliable one.
            rendered = page.content()
            browser.close()
            return rendered
    except Exception as e:
        # If Playwright fails, return whatever requests returned (even if minimal)
        print(f"[fetch_html] Playwright render failed: {e}", file=sys.stderr)
        return text or ""


def text_from_soup(soup: BeautifulSoup) -> str:
    # Remove scripts/styles
    for s in soup(["script", "style", "noscript", "iframe"]):
        s.decompose()
    # Prefer main/article if present
    main = soup.find("main") or soup.find("article")
    if main:
        return main.get_text(separator="\n", strip=True)
    # fallback look for common content-ish containers
    candidates = soup.select(
        "div[class*=content], div[class*=main], section, .event, .event-card, .entry"
    )
    if candidates:
        texts = []
        for c in candidates:
            t = c.get_text(separator=" ", strip=True)
            if len(t) > 30:
                texts.append(t)
        if texts:
            return "\n\n".join(texts)
    # final fallback: whole body text
    body = soup.body
    if body:
        return body.get_text(separator="\n", strip=True)
    return soup.get_text(separator="\n", strip=True)


def parse_json_ld(soup: BeautifulSoup) -> Optional[Dict[str, Any]]:
    scripts = soup.find_all("script", type="application/ld+json")
    for s in scripts:
        try:
            data = json.loads(s.string or "{}")
        except Exception:
            # sometimes script contains multiple JSON objects or trailing text
            text = s.string or ""
            # try to find JSON objects inside
            match = JSON_PATTERN.search(text)
            if match:
                try:
                    data = json.loads(match.group(0))
                except Exception:
                    continue
            else:
                continue
        # JSON-LD might be a list
        if isinstance(data, list):
            for item in data:
                if isinstance(item, dict) and item.get("@type", "").lower() == "event":
                    return item
            # fallback to first dict
            for item in data:
                if isinstance(item, dict):
                    return item
        elif isinstance(data, dict):
            t = data.get("@type", "") or data.get("type", "")
            if isinstance(t, str) and "event" in t.lower():
                return data
            # some pages place event inside graph
            if "graph" in data or "@graph" in data:
                candidates = data.get("graph") or data.get("@graph") or []
                for c in candidates:
                    if (
                        isinstance(c, dict)
                        and "event" in str(c.get("@type", "")).lower()
                    ):
                        return c
            # fallback: if it contains typical event fields
            if any(k in data for k in ("startDate", "location", "name")):
                return data
    return None


def meta_field(soup: BeautifulSoup, name_variants):
    for name in name_variants:
        tag = soup.find("meta", property=name) or soup.find(
            "meta", attrs={"name": name}
        )
        if tag and tag.get("content"):
            return tag["content"].strip()
    return ""


def parse_time_from_time_tags(soup: BeautifulSoup):
    times = soup.find_all("time")
    results = []
    for t in times:
        dt = t.get("datetime")
        text = t.get_text(strip=True)
        if dt:
            results.append(dt)
        elif text:
            results.append(text)
    return results


def try_parse_date(text: str) -> Optional[str]:
    if not text or len(text) < 4:
        return None
    try:
        dt = dateparser.parse(text, fuzzy=True)
        # Return ISO format (with timezone naive — keep as isoformat)
        if dt:
            return dt.isoformat()
    except Exception:
        return None
    return None


def first_json(text: str) -> str:
    # Try fenced JSON blocks
    if "```" in text:
        blocks = re.findall(r"```(?:json)?\s*([\s\S]*?)```", text, flags=re.IGNORECASE)
        for b in blocks:
            b = b.strip()
            if b.startswith("{"):
                return b
    m = JSON_PATTERN.search(text)
    if m:
        return m.group(0)
    return text.strip()


# ---------------- CORE EXTRACTION ----------------
def local_extract(url: str, html: str) -> Dict[str, Any]:
    soup = BeautifulSoup(html, "html.parser")
    result = {
        k: (
            SCHEMA[k]
            if not isinstance(SCHEMA[k], bool) and not isinstance(SCHEMA[k], list)
            else SCHEMA[k]
        )
        for k in SCHEMA
    }

    # JSON-LD first
    jsonld = parse_json_ld(soup)
    if jsonld:
        # Map typical names
        if "name" in jsonld and not result["title"]:
            result["title"] = jsonld.get("name") or ""
        if "description" in jsonld and not result["description"]:
            result["description"] = jsonld.get("description") or ""
        if "startDate" in jsonld:
            sd = try_parse_date(jsonld.get("startDate"))
            if sd:
                result["start_datetime"] = sd
        if "endDate" in jsonld:
            ed = try_parse_date(jsonld.get("endDate"))
            if ed:
                result["end_datetime"] = ed
        if "location" in jsonld:
            loc = jsonld.get("location")
            if isinstance(loc, dict):
                result["location"] = (
                    loc.get("name", "")
                    or loc.get("address", {}).get("streetAddress", "")
                    or str(loc)
                )
            else:
                result["location"] = str(loc)
        if "url" in jsonld:
            result["event_url"] = jsonld.get("url")
        if "organizer" in jsonld:
            org = jsonld.get("organizer")
            if isinstance(org, dict):
                result["organizer_name"] = org.get("name", "") or ""
            else:
                result["organizer_name"] = str(org)

    # Meta Open Graph / Twitter
    og_title = meta_field(soup, ["og:title", "twitter:title"])
    if og_title and not result["title"]:
        result["title"] = og_title
    og_desc = meta_field(soup, ["og:description", "twitter:description", "description"])
    if og_desc and not result["short_description"]:
        # short desc prefer meta description
        result["short_description"] = og_desc
    og_url = meta_field(soup, ["og:url", "url"])
    if og_url and not result["event_url"]:
        result["event_url"] = og_url

    # Title heuristics
    if not result["title"]:
        h1 = soup.find("h1")
        if h1 and h1.get_text(strip=True):
            result["title"] = h1.get_text(strip=True)

    # Time tag heuristics
    times = parse_time_from_time_tags(soup)
    if times:
        parsed = [try_parse_date(t) for t in times]
        parsed = [p for p in parsed if p]
        if parsed:
            result["start_datetime"] = result["start_datetime"] or parsed[0]
            if len(parsed) > 1:
                result["end_datetime"] = result["end_datetime"] or parsed[1]

    # Search body text for date-like substrings (simple heuristic)
    body_text = text_from_soup(soup)
    # try to find lines that contain month names / digits
    lines = [l.strip() for l in body_text.splitlines() if l.strip()]
    for ln in lines[:200]:  # limit work
        if (
            any(
                m in ln.lower()
                for m in [
                    "jan",
                    "feb",
                    "mar",
                    "apr",
                    "may",
                    "jun",
                    "jul",
                    "aug",
                    "sep",
                    "oct",
                    "nov",
                    "dec",
                    "am",
                    "pm",
                    "gmt",
                    "utc",
                    "st",
                    "th",
                ]
            )
            and len(ln) < 200
        ):
            d = try_parse_date(ln)
            if d and not result["start_datetime"]:
                result["start_datetime"] = d
                break

    # location guesses: look for elements that mention venue or location
    if not result["location"]:
        # look for text around keywords
        for ln in lines[:500]:
            if any(
                w in ln.lower()
                for w in ["venue", "location", "address", "place", "at "]
            ):
                if len(ln) < 200:
                    result["location"] = ln
                    break

    # contact email
    if not result["contact_email"]:
        m = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", html)
        if m:
            result["contact_email"] = m.group(0)

    # slug from URL if empty
    if not result["slug"]:
        if "/" in url.rstrip("/"):
            result["slug"] = url.rstrip("/").split("/")[-1]

    # event_url fallback
    result["event_url"] = result["event_url"] or url
    # description fallback
    if not result["description"]:
        # take first longish paragraph as description
        long_paras = [p for p in lines if len(p) > 100]
        if long_paras:
            result["description"] = long_paras[0]
        else:
            result["description"] = "\n".join(lines[:6])

    # short_description fallback
    if not result["short_description"]:
        sd = result["description"]
        if sd and len(sd) > 200:
            result["short_description"] = sd[:200].rsplit(" ", 1)[0] + "..."
        else:
            result["short_description"] = sd

    return result, body_text


# ---------------- AI STEP ----------------
def call_ai_fill(client, text_snippet: str) -> Dict[str, Any]:
    prompt = PROMPT_TEMPLATE.replace(
        "{text}", text_snippet[:110000]
    )  # truncate for safety
    resp = client.chat.completions.create(
        model=AZURE_OPENAI_DEPLOYMENT,
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_tokens=1000,
    )
    content = resp.choices[0].message.content if resp.choices else ""
    raw = first_json(content)
    try:
        parsed = json.loads(raw)
        if isinstance(parsed, dict):
            return parsed
    except Exception:
        # If parse fails, return empty structure to avoid breaking
        return {}
    return {}


# ---------------- MERGE ----------------
def merge_results(local: Dict[str, Any], ai: Dict[str, Any]) -> Dict[str, Any]:
    out = {}
    for k, v in SCHEMA.items():
        # Prefer local heuristics if they look non-empty (and not the default)
        local_val = local.get(k)
        ai_val = ai.get(k) if isinstance(ai, dict) else None

        if k in ("is_public", "is_featured"):
            # booleans: ai may return true/false else keep local
            if isinstance(local_val, bool):
                out[k] = local_val
            elif isinstance(ai_val, bool):
                out[k] = ai_val
            else:
                out[k] = v
            continue

        # if local has non-empty useful value
        if isinstance(local_val, str) and local_val.strip():
            out[k] = local_val
        elif isinstance(local_val, list) and local_val:
            out[k] = local_val
        elif ai_val not in (None, "", [], {}):
            out[k] = ai_val
        else:
            out[k] = v  # default
    return out


# ---------------- ENTRYPOINT ----------------
# ---------- New functions: capture API JSON + smarter extract_event ----------
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
import time


def capture_json_from_network(url: str, timeout: int = 20) -> Optional[Dict[str, Any]]:
    """
    Launch a headless browser, navigate to the url, capture JSON responses.
    Return the first dict-like JSON that looks like event data (contains name/title/startDate/description).
    """
    found_json = None
    try:
        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=True)
            page = browser.new_page()
            responses = []

            def _on_response(resp):
                try:
                    # Only consider likely JSON responses
                    ct = (resp.headers.get("content-type") or "").lower()
                    if "application/json" in ct or resp.url.lower().endswith(".json"):
                        responses.append(resp)
                except Exception:
                    pass

            page.on("response", _on_response)

            # Go to the page and wait for network idle
            try:
                page.goto(url, timeout=timeout * 1000, wait_until="networkidle")
            except PlaywrightTimeoutError:
                # still proceed to collect whatever we have
                pass

            # give SPA some extra time to fire fetches if needed
            time.sleep(1.2)

            # iterate captured responses, try to find event-like JSON
            for resp in reversed(responses):  # check newest first
                try:
                    j = None
                    # attempt to parse JSON body
                    j = resp.json()
                    # j can be dict or list
                except Exception:
                    # skip non-JSON bodies
                    continue

                # If dict and contains event-like keys, return it or its nested item
                def looks_like_event(obj):
                    if not isinstance(obj, dict):
                        return False
                    keys = {k.lower() for k in obj.keys()}
                    # common event keys
                    for k in (
                        "name",
                        "title",
                        "startdate",
                        "start_date",
                        "start_datetime",
                        "description",
                    ):
                        if k in keys:
                            return True
                    # location or organizer hint
                    if any(
                        k in keys for k in ("location", "venue", "organizer", "address")
                    ):
                        return True
                    return False

                if isinstance(j, dict) and looks_like_event(j):
                    found_json = j
                    break
                if isinstance(j, list):
                    # find first element that looks like event
                    for item in j:
                        if isinstance(item, dict) and looks_like_event(item):
                            found_json = item
                            break
                    if found_json:
                        break

            browser.close()
    except Exception as e:
        # Playwright failed; return None (fallback will run)
        print(f"[capture_json_from_network] error: {e}", file=sys.stderr)
        return None

    return found_json


def map_api_json_to_schema(api_json: Dict[str, Any], url: str) -> Dict[str, Any]:
    """
    Map typical API/JSON-LD keys to your SCHEMA.
    This handles common shapes: JSON-LD, event API objects, nested organizer/location objects, etc.
    """
    out = {k: SCHEMA[k] for k in SCHEMA}  # start with defaults

    if not isinstance(api_json, dict):
        return out

    # helpers to safely extract
    def get_str(obj, *keys):
        for k in keys:
            v = obj.get(k) if isinstance(obj, dict) else None
            if isinstance(v, str) and v.strip():
                return v.strip()
        return ""

    # Title / name
    out["title"] = get_str(api_json, "name", "title") or out["title"]

    # slug
    if not out["slug"]:
        out["slug"] = get_str(api_json, "slug") or url.rstrip("/").split("/")[-1]

    # description
    out["description"] = (
        get_str(api_json, "description", "desc", "about") or out["description"]
    )

    # short_description - prefer a short meta if available
    out["short_description"] = (
        get_str(api_json, "short_description", "summary") or out["short_description"]
    )

    # datetimes - common keys: startDate, start_date, start_datetime, start
    start_candidates = [
        api_json.get(k)
        for k in (
            "startDate",
            "start_date",
            "start_datetime",
            "start",
            "starts_at",
            "startAt",
        )
        if k in api_json
    ]
    end_candidates = [
        api_json.get(k)
        for k in ("endDate", "end_date", "end_datetime", "end", "ends_at", "endAt")
        if k in api_json
    ]

    for sc in start_candidates:
        if sc:
            parsed = try_parse_date(str(sc))
            if parsed:
                out["start_datetime"] = parsed
                break

    for ec in end_candidates:
        if ec:
            parsed = try_parse_date(str(ec))
            if parsed:
                out["end_datetime"] = parsed
                break

    # location may be string or object with name/address
    loc = api_json.get("location") or api_json.get("venue") or api_json.get("place")
    if isinstance(loc, dict):
        out["location"] = (
            loc.get("name")
            or loc.get("address", {}).get("streetAddress")
            or loc.get("address", {}).get("formatted")
            or str(loc)
        )
    elif isinstance(loc, str):
        out["location"] = loc

    # organizer
    org = api_json.get("organizer") or api_json.get("host")
    if isinstance(org, dict):
        out["organizer_name"] = org.get("name") or org.get("organization") or ""
    elif isinstance(org, str):
        out["organizer_name"] = org

    # event_url
    out["event_url"] = get_str(api_json, "url", "event_url") or url

    # contact email
    contact = get_str(
        api_json, "contactEmail", "contact_email", "email", "support_email"
    )
    if contact:
        out["contact_email"] = contact
    else:
        # try to find email in raw JSON string quickly
        txt = json.dumps(api_json)
        m = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", txt)
        if m:
            out["contact_email"] = m.group(0)

    # tags / categories
    tags = (
        api_json.get("tags") or api_json.get("categories") or api_json.get("keywords")
    )
    if isinstance(tags, list):
        out["tags"] = [str(t) for t in tags if t]
    elif isinstance(tags, str):
        out["tags"] = [t.strip() for t in tags.split(",") if t.strip()]

    # status/public/featured
    if isinstance(api_json.get("isPublic"), bool):
        out["is_public"] = api_json.get("isPublic")
    if isinstance(api_json.get("isFeatured"), bool):
        out["is_featured"] = api_json.get("isFeatured")
    # created/updated
    for k in ("createdAt", "created_at", "created"):
        if k in api_json and api_json.get(k):
            p = try_parse_date(str(api_json.get(k)))
            if p:
                out["created_at"] = p
                break
    for k in ("updatedAt", "updated_at", "updated"):
        if k in api_json and api_json.get(k):
            p = try_parse_date(str(api_json.get(k)))
            if p:
                out["updated_at"] = p
                break

    # status mapping (if present)
    if api_json.get("status"):
        out["status"] = str(api_json.get("status"))

    return out


def extract_event(url: str):
    """
    Improved extract: try to capture JSON from network first (best),
    else render & parse DOM heuristics, else fallback to AI fill.
    """
    # 1) Try capturing API JSON from network (fast & accurate when available)
    api_json = capture_json_from_network(url, timeout=20)
    if api_json:
        mapped = map_api_json_to_schema(api_json, url)
        print(json.dumps(mapped, ensure_ascii=False))
        return

    # 2) Fallback: render page HTML (Playwright) and parse DOM heuristics
    try:
        html = fetch_html(url, timeout=30, use_playwright=True)
    except Exception as e:
        print(json.dumps({"error": f"Failed fetching URL: {str(e)}"}))
        return

    local_guess, cleaned_text = local_extract(url, html)

    # 3) Only call AI if needed (e.g., many empty required fields)
    need_ai = False
    keys_to_check = ["title", "description", "start_datetime"]
    empties = sum(1 for k in keys_to_check if not local_guess.get(k))
    if empties >= 2:
        need_ai = True

    ai_parsed = {}
    client = make_azure_client()
    if need_ai and client:
        try:
            ai_parsed = call_ai_fill(client, cleaned_text)
        except Exception as e:
            print(f"AI call failed: {e}", file=sys.stderr)
            ai_parsed = {}

    merged = merge_results(local_guess, ai_parsed)
    merged.setdefault("event_url", url)
    if not merged.get("slug"):
        merged["slug"] = url.rstrip("/").split("/")[-1]

    print(json.dumps(merged, ensure_ascii=False))


# ---------------- RUN ----------------
if __name__ == "__main__":
    url = "https://unstop.com/hackathons/codeclash-pranveer-singh-institute-of-technology-psit-kanpur-1544598"
    extract_event(url)
