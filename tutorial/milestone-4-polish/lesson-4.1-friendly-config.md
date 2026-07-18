# Lesson 4.1 — A friendly config file

> **Milestone 4 · Lesson 1 of 4** — turning a working script into a real tool.

## 🎯 Goal
Grow your config from "just the pad shortcuts" into one clear file that describes everything — pad
keys, pen buttons, monitor, pressure — with sensible defaults and helpful errors.

## 🧠 New idea: defaults, structure, and failing helpfully

A tool other people (future-you included) can use needs its config to be:
- **Structured** — group related settings so it's readable:
  ```json
  {
    "pad_shortcuts":  { "259": "ctrl+z", "260": "b" },
    "pen_shortcuts":  { "331": "ctrl+z" },
    "pen_output":     "DP-2",
    "pressure_curve": [0, 10, 80, 100]
  }
  ```
- **Defaulted** — if a setting is missing, fall back to something reasonable instead of crashing.
- **Honest when wrong** — if the file has a typo, print a *clear* message ("config.json line 4: bad
  JSON") rather than a scary stack trace.

These are the habits that separate a script from a tool. This project explicitly values that
long-term quality.

## 👀 See it

Loading config defensively:

```python
import json, sys

try:
    with open("config.json") as f:
        cfg = json.load(f)
except FileNotFoundError:
    print("No config.json found — copy config.example.json to config.json.")
    sys.exit(1)
except json.JSONDecodeError as e:
    print("config.json isn't valid JSON:", e)
    sys.exit(1)

pen_output = cfg.get("pen_output")          # None if not set -> treat as "don't remap"
```

## ⌨️ Your turn

1. Restructure `config.json` into named sections like the example above (pad, pen, output,
   pressure).
2. Update `detect.py` to read from the new structure, using `.get(...)` so missing sections don't
   crash — they just get skipped or use a default.
3. Wrap the file load in `try/except` (see "See it") so a missing/broken file gives a friendly
   message.
4. Create a `config.example.json` (safe to commit) so there's always a template to copy.

**Hints**
- `try/except` = "attempt this; if it fails this specific way, do that instead." Ask Claude to walk
  through it — it's the standard way to handle expected failures.
- Keep `config.json` (your personal one) out of git if you like, and commit only the example — tell
  Claude and we'll add a `.gitignore` line.

## ✅ Done when

Your app reads one structured config, survives a missing/typo'd file with a clear message, and ships
a `config.example.json`.

Tell Claude **"done with 4.1"**.

---
**Next:** Lesson 4.2 — Start the tool automatically at login.
