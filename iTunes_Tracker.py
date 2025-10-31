import json
import requests

term = input("Search for a song or artist: ").strip()

response = requests.get(f"https://itunes.apple.com/search?entity=song&limit=50&term={term}")

o = response.json()
for result in o["results"]:
    print(result["trackName"])
