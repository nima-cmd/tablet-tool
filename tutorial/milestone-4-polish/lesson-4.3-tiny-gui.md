# Lesson 4.3 — A tiny GUI

> **Milestone 4 · Lesson 3 of 4**

## 🎯 Goal
Build a small window that shows your current key→shortcut mappings (and, if you're feeling it, lets
you edit them) — so you don't have to hand-edit JSON forever.

## 🧠 New idea: a graphical program and Tkinter

Everything so far has been terminal + text files. A **GUI** (graphical user interface) is a window
with widgets — labels, buttons, text boxes. Python ships with a simple GUI toolkit called
**Tkinter** (no install needed), which is perfect for a first window.

Two ideas make GUIs click:
- **Widgets** — the building blocks (a `Label` shows text, an `Entry` is a text box, a `Button`
  does something when clicked).
- **Event-driven** — instead of running top-to-bottom then ending, a GUI *waits* for you (clicks,
  typing) and responds. It has its own "loop" (`root.mainloop()`), much like the read loop waited
  for tablet events.

## 👀 See it

The smallest possible window:

```python
import tkinter as tk

root = tk.Tk()
root.title("Tablet Tool")
tk.Label(root, text="Your shortcuts:").pack()
root.mainloop()      # shows the window and waits
```

Run that and a window appears. That's your foundation.

## ⌨️ Your turn

Start tiny and grow:

1. **Show a window** with the snippet above (`src/gui.py`). Confirm it opens.
2. **List your mappings**: load `config.json` and, for each entry, `pack()` a `Label` like
   `key 259  →  ctrl+z`. Now the window *reflects your real config*.
3. **(Stretch) Edit**: put each shortcut in an `Entry`, add a **Save** button whose function writes
   the values back to `config.json` with `json.dump`. That closes the loop: GUI edits the same file
   the app reads.

**Hints**
- Build in that order — a visible window first, then real data, then editing. Don't attempt all
  three at once.
- `json.dump(data, f, indent=2)` writes a dict back out as tidy JSON.
- The GUI and the running detector are separate programs sharing `config.json`. For edits to take
  effect you'll restart the detector (or, later, have it reload) — ask Claude about the options.
- This is the biggest single lesson; take it in the three sub-steps and lean on Claude between them.

## ✅ Done when

A window opens showing your current mappings from `config.json` (bonus: you can edit and save them).

Tell Claude **"done with 4.3"**.

---
**Next:** Lesson 4.4 — Per-application profiles (the finale).
