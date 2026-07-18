# Lesson 1.4 — The event loop: print raw events

> **Milestone 1 · Lesson 4 of 6**

## 🎯 Goal
Make `detect.py` *listen* to the Pad: read events forever and print each one, so you can watch
your button presses show up live.

## 🧠 New ideas: an endless loop, blocking, and Ctrl-C

- **`read_loop()`** — every device object can give you an endless stream of events:
  ```python
  for event in pad.read_loop():
      print(event)
  ```
  This `for` never naturally ends — it keeps waiting for the next event. That's exactly what a
  background tool wants.
- **blocking** — when there's nothing to read, the loop politely *waits* (it doesn't burn your
  CPU). The moment you press a button, the next event arrives and prints.
- **Ctrl-C** — since the loop runs forever, you stop it yourself by pressing **Ctrl-C** in the
  terminal. That sends an interrupt that ends the program.

## 👀 See it

The addition to your file, conceptually:

> After you've found and opened `pad`, start reading its events in a loop and print each one.

## ⌨️ Your turn

1. In `src/detect.py`, **after** the part that confirms `pad` was found, add the read loop:
   ```python
   print("Listening... press the Pad's express keys (Ctrl-C to stop).")
   for event in pad.read_loop():
       print(event)
   ```
2. Run it:
   ```bash
   python3 src/detect.py
   ```
3. Press some express keys on the tablet and watch lines appear. Press **Ctrl-C** to stop.

**Hints**
- You'll see *lots* of events, and some you didn't cause (the tablet chatters). That's normal —
  next lesson we filter down to just the button presses.
- Each printed line includes a `type`, `code`, and `value` — the three parts from Lesson 1.1. See
  if you can spot the `value 1` (press) and `value 0` (release) as you tap a key.
- Nothing printing? Confirm 1.3 still finds the Pad, and that you're pressing the **pad** keys (not
  drawing with the pen — that's the other device).

## ✅ Done when

Pressing an express key makes new lines appear in the terminal, and Ctrl-C stops the program.

Tell Claude **"done with 1.4"**.

---
**Next:** Lesson 1.5 — Filter the flood down to just the button presses.
