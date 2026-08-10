# Lesson 1.6 — Build your key map (physical key → code)

> **Milestone 1 · Lesson 6 of 6** — the milestone finale.

## 🎯 Goal
Press each of the 8 express keys in turn, record the code each one produces, and save that table.
This is the "Rosetta Stone" the whole app depends on.

## 🧠 New idea: mapping the physical world to numbers (and comments)

The tablet doesn't know your keys are "top-left" or "the big one" — it only emits code *numbers*.
To bind shortcuts later, **you** must decide which physical key is which code. There's no shortcut
for this; you press each key and write down what code appears. This is genuinely how real driver
config is built.

We'll record it as two useful forms:
- **A comment** — human notes, e.g. `# key 1 (top-left) = 259`.
- **A dictionary** — code the app can use later:
  ```python
  KEYS = {
      259: "key1",   # top-left
      260: "key2",
      # ...
  }
  ```
  A **dictionary** maps a *key* (here, the code number) to a *value* (a label). We'll lean on this
  heavily in Milestone 2.

## 👀 See it

You already have the tool: `detect.py` from Lesson 1.5 prints `pressed, code = N`. Now you just use
it as a measuring instrument.

## ⌨️ Your turn

1. Run `python3 src/detect.py`.
2. Press the express keys **one at a time, in an order you choose** (e.g. top to bottom). After each
   press, note the code it printed and which physical key it was. Do all 8. Don't forget the dial's
   press/tilt if it emits key events too.
3. Record your findings at the top of `src/detect.py` as a comment block **and** a `KEYS`
   dictionary. Fill in your real numbers:
   ```python
   # Physical key -> code (measured on my Deco Pro MW)
   # key1 top-left  = ___
   # key2           = ___
   # ... (all 8)
   KEYS = {
       ___: "key1",
       ___: "key2",
       # ...
   }
   ```

**Hints**
- Press deliberately and pause between keys so you can tell which line came from which key.
- If two physical keys report the *same* code, tell Claude — occasionally the dial or a modifier
  behaves differently and we'll adjust.
- Save this file — Milestone 2 builds directly on this `KEYS` table.

## ✅ Done when

You have all 8 express keys mapped to their codes, saved as a comment + `KEYS` dict in
`src/detect.py`.

🎉 **That's Milestone 1 done** — you can detect exactly which button was pressed. Tell Claude
**"done with 1.6"**, and we start Milestone 2: turning those presses into real keyboard shortcuts.

---
**Next:** Lesson 2.1 — What is a keystroke? (keys & modifiers).
