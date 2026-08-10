# Lesson 2.3 — Call xdotool from Python

> **Milestone 2 · Lesson 3 of 7**

## 🎯 Goal
Run xdotool *from inside a Python script* — because soon "when a button is pressed" will trigger
exactly this.

## 🧠 New idea: `subprocess` — running programs from code

Python can launch other programs using the built-in **`subprocess`** library. The clean, safe way:

```python
import subprocess
subprocess.run(["xdotool", "key", "ctrl+z"])
```

Notice the **list of separate strings**: `["xdotool", "key", "ctrl+z"]`, not one big
`"xdotool key ctrl+z"` string. Passing a list means Python hands the pieces straight to the
program without a shell trying to re-interpret spaces or special characters. It's safer and avoids
a whole category of bugs — build the habit now.

- `"xdotool"` — the program to run.
- `"key"` — the subcommand.
- `"ctrl+z"` — the combo (this is the piece we'll swap per button later).

## 👀 See it

```python
import subprocess

subprocess.run(["xdotool", "key", "ctrl+z"])   # same effect as typing it in the terminal
```

## ⌨️ Your turn

1. Create `src/send_test.py`:
   ```python
   import subprocess
   import time

   time.sleep(2)                                   # 2s to focus your app
   subprocess.run(["xdotool", "key", "ctrl+z"])
   print("sent ctrl+z")
   ```
2. Run it, and click into your editor during the 2-second pause:
   ```bash
   python3 src/send_test.py
   ```
3. Confirm the undo happened, and `sent ctrl+z` printed.
4. Change `"ctrl+z"` to another combo from your wishlist and run again.

**Hints**
- `import time` + `time.sleep(2)` is the Python version of the `sleep 2` trick — it pauses the
  script.
- Keep the combo as its **own string** in the list. Next lesson we'll feed it a *variable*.
- `ModuleNotFoundError`? `subprocess` and `time` are built in — a spelling slip is the usual cause.

## ✅ Done when

`python3 src/send_test.py` fires the shortcut in your app and prints its confirmation line.

Tell Claude **"done with 2.3"**.

---
**Next:** Lesson 2.4 — The big moment: one button press → one shortcut.
