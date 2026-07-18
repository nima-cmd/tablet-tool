# Lesson 1.5 — Keep only the button presses

> **Milestone 1 · Lesson 5 of 6**

## 🎯 Goal
Cut the noise: from the flood of raw events, print **only** the moment a button is pressed *down* —
one clean line per press, showing which code it was.

## 🧠 New ideas: event types, `ecodes`, and filtering with `if`

From Lesson 1.1, every event has a **type**, **code**, and **value**. We want just the ones where:

- **type is a key/button event** — in evdev this type is named `EV_KEY`.
- **value is `1`** — meaning *pressed down* (not `0` release, not `2` repeat).

evdev gives us readable names for these through **`ecodes`**:

```python
from evdev import ecodes
...
if event.type == ecodes.EV_KEY and event.value == 1:
    print("button pressed, code:", event.code)
```

`==` means "is equal to" (a *question*), whereas a single `=` means "assign" (a *statement*). Mixing
them up is the #1 beginner bug — `==` for comparing.

## 👀 See it

Before: every twitch prints. After: exactly one line each time you *press* a key, telling you its
**code number**. Those code numbers are what we'll map to shortcuts in Milestone 2.

## ⌨️ Your turn

1. Add `ecodes` to your import at the top of `src/detect.py`:
   ```python
   from evdev import InputDevice, list_devices, ecodes
   ```
2. Change the body of your read loop so it prints **only** on a key-down. Replace the plain
   `print(event)` with the filtered version:
   ```python
   for event in pad.read_loop():
       if event.type == ecodes.EV_KEY and event.value == 1:
           print("pressed, code =", event.code)
   ```
3. Run it, press keys, and confirm you now get **one tidy line per press**.

**Hints**
- Remember `==` (compare) vs `=` (assign). The `if` line uses `==`.
- `and` means both conditions must be true.
- If you get two lines per tap, you may be catching the release too — double-check it says
  `event.value == 1`.

## ✅ Done when

Each press of an express key prints exactly one `pressed, code = <number>` line.

Tell Claude **"done with 1.5"**.

---
**Next:** Lesson 1.6 — Press every key and build your map of physical key → code.
