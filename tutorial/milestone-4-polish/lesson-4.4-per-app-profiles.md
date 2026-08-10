# Lesson 4.4 — Per-application profiles

> **Milestone 4 · Lesson 4 of 4** — the final lesson. This is where your tool beats the vendor app.

## 🎯 Goal
Make the *same* physical key do *different* things depending on which app is focused — e.g. pressure
brushes in Krita, but mouse-like pan/orbit shortcuts in Blender.

## 🧠 New idea: knowing the active window, and choosing a profile

The missing piece is: *which app am I in right now?* On X11 you can ask:

- **`xdotool getactivewindow getwindowname`** — the title of the focused window.
- **`xprop -id <id> WM_CLASS`** — the app's "class" (often a cleaner, more stable identifier than
  the title).

Once you know the active app, you pick a **profile** — a named set of shortcuts — instead of a
single flat map:

```json
{
  "profiles": {
    "krita":   { "259": "ctrl+z", "260": "b",       "261": "e" },
    "blender": { "259": "ctrl+z", "260": "ctrl+tab", "261": "z" }
  },
  "default": "krita"
}
```

When a key is pressed, your app: (1) checks the active window, (2) chooses the matching profile,
(3) looks up the code in *that* profile. Same engine you built — one more lookup in front.

## 👀 See it

```bash
xdotool getactivewindow getwindowname     # e.g. "untitled — Krita"
xdotool getactivewindow getwindowclassname
```

Try focusing different apps and running it — see how each reports itself.

## ⌨️ Your turn

1. From Python, get the active window's name/class:
   ```python
   name = subprocess.run(
       ["xdotool", "getactivewindow", "getwindowname"],
       capture_output=True, text=True
   ).stdout.strip().lower()
   ```
2. Write a small function `pick_profile(name)` that returns which profile to use (e.g. if `"krita"`
   in `name` → the krita profile; if `"blender"` in `name` → blender; else the default).
3. In the read loop, on each key-down: pick the profile, then do the `SHORTCUTS.get(code)` lookup
   **within that profile**.
4. Restructure `config.json` into `profiles` (see above) and test: the same key should behave
   differently in Krita vs Blender.

**Hints**
- `capture_output=True, text=True` lets you *read* a program's output as a string (new: before we
  only *ran* commands; now we read their result).
- Checking the active window on every press is fine (it's fast). If you prefer, cache it and only
  re-check when it changes — an optimization for later.
- Start with two profiles you actually use; add more by editing config, no code changes needed.

## ✅ Done when

The same express key fires different shortcuts depending on whether Krita or Blender is focused,
driven by profiles in your config.

🎉🎉 **You did it — the tool is complete.** You built, from nothing, a configurable tablet utility
that reads raw device events, fires clean keystrokes, maps and tunes the pen, starts on login, has a
GUI, and switches per app — something the vendor software couldn't do well on your machine. Tell
Claude **"done with 4.4"** for the final ledger tick.

---
**What next?** Ideas to keep going: a dial/scroll-wheel action, on-screen "which key did what"
overlays, exporting/importing profiles, or packaging it so others can install it. Bring any of these
to Claude anytime.
