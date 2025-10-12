# Ultimate Tic-Tac-Toe — README

A small Flask + JavaScript web app that implements **Ultimate Tic-Tac-Toe** with a hand-drawn look and a number of UX features you requested.

---

## Overview

This project is a playable Ultimate Tic-Tac-Toe game served by Flask. It combines a 9×9 board (9 mini 3×3 boards) with:

* a hand-drawn visual style (thick separators, sketchy font),
* clear visual guidance for the next sub-board to play in,
* chess-like faint dots showing legal moves,
* captured sub-boards rendered as a single large `X` or `O`,
* player name entry and live display,
* scoreboard that persists during the server lifetime,
* undo (single-step) functionality,
* move counters per player.

This README documents how the app works, how to run it, the API, troubleshooting tips, plus feature suggestions for the main web app.

---

## Features (implemented)

### Gameplay / Rules

* Standard Ultimate Tic-Tac-Toe rules.
* Backend enforces legal moves and computes global-board winners.
* When a move sends the next player to a sub-board that is already captured or full, all open sub-boards are allowed.

### Visual / UX

* **Hand-drawn style**: paper-like background, thicker dividing lines every 3 cells, Caveat font for a sketchy X/O look.
* **Active sub-board highlight**: the sub-board to play next is shaded.
* **Legal-move indicators**: faint blue dots appear on legal squares (like chess apps).
* **Captured sub-boards**: when a mini-board is won, the entire 3×3 block visually displays a large `X` or `O`. Clicking inside a captured block is disabled.
* **Themes**: (kept as in your working styling) — the original hand-drawn look is preserved.

### Player / Scoreboard

* Player name input fields for X and O.
* Live scoreboard display shows name, wins, and moves for each player.
* Scores persist across resets during the running server session.
* Live updating of displayed names when the user types in the input fields.

### Controls

* `Reset Game` — clears the board, preserves the scoreboard totals (server session).
* `Undo` — reverts the last move (single-step undo).
* Click a cell to make a move (frontend calls `/move`).

---

## How to run

1. Ensure Python 3.x is installed.

2. Install dependencies:

   ```bash
   pip install flask numpy
   ```

3. Run the server:

   ```bash
   python temp.py
   ```

   (or whichever file you saved the script as; the app runs in Flask debug mode in the example).

4. Open your browser at `http://127.0.0.1:5000/`.

---

## API endpoints

These are the endpoints used by the frontend (simple JSON communication):

* `GET /`
  Returns the HTML page (game UI).

* `GET /reset`
  Resets the current board (keeps scoreboard totals that live in memory) and returns the new state JSON.

* `POST /move`
  Request body (JSON):

  ```json
  { "r": <rowIndex 0-8>, "c": <colIndex 0-8> }
  ```

  Response: State JSON (or `{'error':'Invalid move'}` on illegal move).

* `GET /undo`
  Undo the last move. Returns the new state JSON or `{'error':'No moves to undo'}` if none.

---

## State JSON (what the frontend receives)

Example structure returned by `get_state()` (keys explained below):

```json
{
  "board": [[...], ...],          // 9x9 matrix with 0 (empty), 1 (X), -1 (O)
  "global_board": [[...], ...],   // 3x3 matrix; 0 ongoing, 1 (X captured sub-board), -1 (O)
  "current_player": 1,            // 1 => X, -1 => O
  "done": false,                  // true when overall game finished
  "winner": 0,                    // 0 draw/ongoing, 1 X, -1 O
  "next_subboard": 4,             // 0..8 or null/None for any subboard allowed
  "legal_moves": [[r,c], ...],    // list of legal moves as coordinates
  "scores": { "1": 0, "-1": 0 },  // wins per player (server-session lifetime)
  "move_counts": { "1": 0, "-1": 0 } // how many moves each player has made
}
```

> Frontend uses `global_board` to detect captured sub-boards and render large symbols over the 3×3 area.

---

## UI controls & behaviour

* Click an empty legal cell to place your mark.
* If you misclick, use **Undo** (single-step) to restore the previous state.
* Type player names in the `X Player` and `O Player` boxes — the scoreboard and status update live.
* `Reset Game` clears the board (score totals remain until server is restarted).

---

## Troubleshooting & common gotchas

* If you see an `AttributeError` for `scores` or similar during startup, ensure the `UltimateTicTacToe.__init__` properly creates attributes before `reset()` uses them. The provided code initializes `scores` correctly.
* Scores and move counts persist only while the server process is alive. If you restart Python, they will reset.
* If legal move dots or highlights aren’t visible on your display, try increasing monitor brightness or tweak CSS `.legal::after` opacity/size in the stylesheet.
* When a sub-board is captured, click events inside that sub-board should be disabled — if clicks still work, ensure the frontend draws captured blocks using `state.global_board`.

---

## Suggested additional features — prioritized

Below are ideas to add to the **main web app**. I grouped them into *MVP next steps* and *nice-to-have*.

### MVP / High value (implement soon)

1. **AI opponent (single-player)** — a simple heuristic agent, then progressively stronger algorithms (Minimax with heuristics / Monte Carlo Tree Search).
2. **Persistent leaderboard** — store player stats (wins, losses) in a small DB or JSON file so scores survive server restarts.
3. **Multiplayer online** — local network or public matchmaking (WebSocket for real-time interactive play).
4. **Multiple undo / move history viewer** — allow stepping backward/forward through move history; visually show the move list.
5. **Start/Lock names button** — lock names at game start to avoid mid-game confusion and optionally attach avatars.

### UX / polish

6. **Animations** — smooth ink-like strokes when drawing big captured symbols, subtle hover animations for dots.
7. **Wobbly/sketchy borders** — use SVG or CSS to make imperfect pencil lines for more authentic hand-drawn feel.
8. **Mobile responsiveness** — layout and touch-friendly controls for phones/tablets.
9. **Accessibility** — high-contrast theme, larger font sizes, ARIA attributes for screen readers, keyboard navigation.
10. **Sound & haptics** — click/hit sounds, optional toggle.

### Social / sharing

11. **Game export / replay** — export a game as JSON or shareable URL enabling replay and embedding.
12. **Share to social** — create an image snapshot of the board and allow posting to social media.
13. **Spectator mode & chat** — allow non-players to observe live games and chat.

### Competitive / community

14. **Ranked ladder** — ELO/TrueSkill, matchmaking, time-controls (per-move timers).
15. **Tournament mode** — bracket or Swiss tournaments with admin UI.

---

## Example roadmap (short-term)

1. Add single-player AI (basic heuristic).
2. Add multiple-undo and move history panel.
3. Add persistent leaderboard (file-based or SQLite).
4. Add mobile styling / UX tweaks.
5. Add WebSocket-based real-time multiplayer.

---

## Code structure (single-file for now)

This project packages everything into one Python script that:

* defines `UltimateTicTacToe` (game logic),
* serves HTML/JS/CSS via `render_template_string`,
* exposes `/`, `/reset`, `/move`, `/undo`.

If this becomes larger, split into:

* `app.py` (Flask routes),
* `game.py` (logic),
* `static/` (CSS/JS),
* `templates/` (HTML templates),
* `data/` (persisted leaderboards/games).

---

## Contributing & notes

* The current code intentionally keeps the *hand-drawn board rendering* exactly as requested.
* Keep UI logic in `drawBoard()` lightweight — all game rules should remain enforced server-side to avoid cheating and state mismatch.
* When adding multiplayer, move from polling (fetch) to WebSocket (flask-socketio) for low-latency updates.

---

## License

This README does not include a formal license by default. For open-source usage, consider `MIT` or `Apache-2.0`. Add a `LICENSE` file to the repo if you want to publish.

---