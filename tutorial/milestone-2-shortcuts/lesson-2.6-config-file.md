# Lesson 2.6 — Move shortcuts into a config file

> **Milestone 2 · Lesson 6 of 7**

## 🎯 Goal
Take the `SHORTCUTS` map out of your Python and put it in a separate **config file**, so you can
change your shortcuts without touching code.

## 🧠 New ideas: config vs code, and JSON

- **Config vs code**: *code* is the logic (read events, fire keys); *config* is your personal
  choices (which key does what). Keeping them separate means you can rebind keys by editing a small
  data file — and later, a GUI could edit that same file. This is the "long-term, maintainable"
  approach this project favors.
- **JSON** is a simple, standard text format for data that looks a lot like a Python dict:
  ```json
  {
    "259": "ctrl+z",
    "260": "b",
    "261": "ctrl+shift+z"
  }
  ```
  Python reads it with the built-in **`json`** library and hands you back a dictionary.

> ⚠️ One gotcha: in JSON, the keys are **text** (`"259"`), so when you read them back they're
> strings, not numbers. But `event.code` is a number. You'll bridge that — the hints cover how.

## 👀 See it

```python
import json

with open("config.json") as f:      # open the file...
    raw = json.load(f)               # ...and turn its JSON into a Python dict

# raw is like {"259": "ctrl+z", ...} with STRING keys
```

## ⌨️ Your turn

1. Create `config.json` (in the project root or `src/` — your call, just be consistent) with your
   key→shortcut map, using the JSON shape above. Keys in quotes.
2. In `src/detect.py`, delete the hard-coded `SHORTCUTS = {...}` and load it from the file instead:
   ```python
   import json
   with open("config.json") as f:
       raw = json.load(f)
   SHORTCUTS = {int(code): combo for code, combo in raw.items()}   # string keys -> int keys
   ```
3. Run it and confirm all keys still work — but now driven by the file.
4. Change one shortcut **in `config.json`**, save, re-run — the behavior changes with **no code
   edit**. That's the win.

**Hints**
- `int(code)` converts the JSON string key back to a number so it matches `event.code`. The
  `{... for ... in raw.items()}` line is a "dict comprehension" — ask Claude to unpack it; it's a
  handy pattern.
- Wrap the load in a friendly error later (Lesson 4.1) so a typo in JSON gives a clear message. For
  now, if `json.load` complains, it's usually a missing comma or quote — paste it to Claude.
- Make sure you run the script from a folder where `config.json` is findable (same folder, or use a
  full path). Ask Claude about paths if it can't find the file.

## ✅ Done when

Editing `config.json` (with no change to `detect.py`) changes which shortcuts your keys fire.

Tell Claude **"done with 2.6"**.

---
**Next:** Lesson 2.7 — Make each press fire exactly once (no double-fire), finishing Milestone 2.
