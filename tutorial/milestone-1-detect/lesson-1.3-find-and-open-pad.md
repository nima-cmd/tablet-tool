# Lesson 1.3 — Find & open the tablet's Pad

> **Milestone 1 · Lesson 3 of 6** — this creates `detect.py`, the start of the real app.

## 🎯 Goal
From the full list of devices, automatically pick the **Pad** (by name) and open just that one.
This is the first file of the actual tool.

## 🧠 New ideas: `if`, string matching, and storing a result

- **`if`** — do something only when a condition is true:
  ```python
  if "Pad" in device.name:
      ...   # only runs for devices whose name contains "Pad"
  ```
- **`in` for text** — `"Pad" in device.name` is `True` when the little string appears inside the
  bigger one. Simple, and robust against the `eventN` number changing.
- **storing the match** — when you find it, save it in a variable so you can use it after the loop:
  `pad = device`.

We also want to handle "what if it's not found?" gracefully instead of crashing — a habit worth
building from day one.

## 👀 See it

The logic in words:

> Look through every device. If one's name contains "Pad", remember it. After looking, if we found
> one, say so; if not, say we couldn't find the tablet.

## ⌨️ Your turn

1. Create `src/detect.py`.
2. Start from your `list_devices.py` loop, then add an `if` that checks the name and stores the
   match. Sketch (fill in the blanks yourself):
   ```python
   from evdev import InputDevice, list_devices

   pad = None                                  # nothing found yet
   for path in list_devices():
       device = InputDevice(path)
       if ______ in device.name:               # what text identifies the Pad?
           pad = device

   if pad:
       print("Found the Pad:", pad.name, "at", pad.path)
   else:
       print("Could not find the Pad. Is the tablet plugged in?")
   ```
3. Run it:
   ```bash
   python3 src/detect.py
   ```

**Hints**
- `pad = None` then `if pad:` is a common pattern: `None` means "nothing yet," and `if pad:` is
  true once it holds a real device.
- Matching on `"Pad"` works, but if another device also contains that word, tighten it (e.g.
  `"Deco Pro MW Pad"`). Ask Claude if the match grabs the wrong device.

## ✅ Done when

`python3 src/detect.py` prints **Found the Pad:** with the tablet's name and path.

Tell Claude **"done with 1.3"**.

---
**Next:** Lesson 1.4 — Read events from the Pad in a loop and print them.
