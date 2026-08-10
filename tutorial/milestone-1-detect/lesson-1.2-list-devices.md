# Lesson 1.2 — List every input device with evdev

> **Milestone 1 · Lesson 2 of 6** — your first real code for the app.

## 🎯 Goal
Write a few lines of Python that print every input device on the machine, each with its name — so
you can *see* the tablet in the list.

## 🧠 New ideas: import, variables, lists, and the `for` loop

Four beginner concepts, all tiny, all used together here:

- **import** — pull a library's tools into your file: `from evdev import InputDevice, list_devices`.
- **variable** — a name that holds a value: `path = "/dev/input/event5"`.
- **list** — an ordered bunch of values in `[...]`. `list_devices()` hands us a list of device
  paths.
- **`for` loop** — "do this once for each item in a list":
  ```python
  for path in list_devices():
      ...   # runs once per path, with `path` set to each one
  ```

One more: an **object** bundles data together. `InputDevice(path)` gives you a device *object*, and
you read facts off it with a dot: `device.name`, `device.path`.

## 👀 See it

The shape of what you'll write (don't copy blindly — understand each line):

```python
from evdev import InputDevice, list_devices    # bring in the two tools we need

for path in list_devices():                     # for each device path...
    device = InputDevice(path)                   # ...open it as an object
    print(path, "->", device.name)               # ...print its path and name
```

## ⌨️ Your turn

1. Create a new file: `src/list_devices.py`.
2. Type the four lines above (typing, not pasting — you'll remember it).
3. Run it:
   ```bash
   python3 src/list_devices.py
   ```
4. Read the output and find the line containing **`Hanvon Ugee Deco Pro MW Pad`**. That's our
   target device.

**Hints**
- `print(a, "->", b)` prints several things on one line separated by spaces — handy for readable
  output.
- If you get `PermissionError`, the `input` group (Lesson 0.4) hasn't kicked in — re-login.
- Don't see the tablet at all? Make sure you're in the **XFCE/X11** session and the dongle is
  plugged in; tell Claude what the list *does* show.

## ✅ Done when

Running `src/list_devices.py` prints a list of devices that includes the `...Deco Pro MW Pad` line.

Tell Claude **"done with 1.2"**.

---
**Next:** Lesson 1.3 — Find and open just the Pad, by name.
