# Lesson 2.5 — A dictionary of shortcuts

> **Milestone 2 · Lesson 5 of 7**

## 🎯 Goal
Handle **all** your keys at once, cleanly — without writing a separate `if` for each one — by using
a dictionary lookup.

## 🧠 New idea: dictionaries and why they beat a pile of `if`s

If you added one `if event.code == ...` per key, you'd have 8 near-identical blocks. That's
repetitive and easy to get wrong. A **dictionary** replaces all of them:

```python
SHORTCUTS = {
    259: "ctrl+z",           # key1 -> undo
    260: "b",                # key2 -> brush
    261: "ctrl+shift+z",     # key3 -> redo
    # ...one line per key
}
```

Then, for any pressed code, you *look up* its shortcut in one step:

```python
combo = SHORTCUTS.get(event.code)     # returns the string, or None if not in the map
if combo:
    subprocess.run(["xdotool", "key", combo])
```

`.get(key)` is the safe way to look something up: if the code isn't in your map, it returns
`None` instead of crashing — so unmapped keys are simply ignored. This "one data structure + one
lookup" shape is a core programming pattern; you'll reuse it constantly. It's also **DRY** — Don't
Repeat Yourself.

## 👀 See it

Before: 8 copy-pasted `if`s. After: one `SHORTCUTS` dict + three lines that work for every key.
Adding a key later becomes a one-line edit to the dict.

## ⌨️ Your turn

1. In `src/detect.py`, build a `SHORTCUTS` dictionary from your Lesson 1.6 codes + Lesson 2.1
   wishlist — one entry per key.
2. Replace the single-key `if event.code == 259: ...` from Lesson 2.4 with the general lookup:
   ```python
   for event in pad.read_loop():
       if event.type == ecodes.EV_KEY and event.value == 1:
           combo = SHORTCUTS.get(event.code)
           if combo:
               subprocess.run(["xdotool", "key", combo])
               print("fired", combo)
   ```
3. Run it and test **every** key. Each should fire its own shortcut.

**Hints**
- The dict's keys are the **code numbers**; the values are the **xdotool strings**.
- Notice `combo` is now a variable feeding `subprocess.run` — that's why we kept the combo as its
  own string back in 2.3.
- A key does nothing? Its code probably isn't in `SHORTCUTS` (check for a typo in the number).

## ✅ Done when

Every mapped express key fires its own shortcut, all driven by the single `SHORTCUTS` dictionary.

Tell Claude **"done with 2.5"**.

---
**Next:** Lesson 2.6 — Move the mapping out of the code into a config file.
