# Lesson 2.4 — First shortcut: one button → one keystroke

> **Milestone 2 · Lesson 4 of 7** — the two halves finally meet.

## 🎯 Goal
Press **one** express key on the tablet and have it fire **one** real shortcut. This is the first
moment the app actually *does its job*.

## 🧠 New idea: combining what you already built

You already have both halves:
- Milestone 1's `detect.py` knows *when* a key is pressed and *which code* it was.
- Lesson 2.3 knows how to *fire a shortcut* with `subprocess.run([...])`.

Joining them is just: **inside the read loop, when the code matches, call subprocess.** No new tool
— only wiring.

## 👀 See it

The idea, in pseudocode:

> for each event: if it's a key-down **and** its code is (my chosen key), then run xdotool with the
> shortcut I want.

## ⌨️ Your turn

1. Open `src/detect.py`. Make sure `import subprocess` is near the top.
2. Pick **one** key from your `KEYS` map (say code `259`) and one shortcut (say `ctrl+z`).
3. In the read loop's key-down branch, add the match + fire:
   ```python
   for event in pad.read_loop():
       if event.type == ecodes.EV_KEY and event.value == 1:
           if event.code == 259:                       # <- your chosen key's code
               subprocess.run(["xdotool", "key", "ctrl+z"])
               print("fired ctrl+z")
   ```
4. Run `python3 src/detect.py`, focus your drawing/editor app, and **press that one key**. It
   should trigger the shortcut. Ctrl-C to stop.

**Hints**
- Use a real code from *your* Lesson 1.6 table, not `259`.
- Test in an app where the effect is obvious (undo is great — do something, then press the key).
- Focus matters: the app you're pressing into must be the focused window, same as Lesson 2.2.
- Fires twice per press? You're probably also catching release — confirm `event.value == 1`.

## ✅ Done when

Pressing your chosen express key makes the shortcut happen in a real app. 🎉 The tool works — for
one key.

Tell Claude **"done with 2.4"**.

---
**Next:** Lesson 2.5 — Scale from one key to all of them with a dictionary.
