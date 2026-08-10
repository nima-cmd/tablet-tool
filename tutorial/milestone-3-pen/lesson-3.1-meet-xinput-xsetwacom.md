# Lesson 3.1 — Meet xinput & xsetwacom

> **Milestone 3 · Lesson 1 of 4** — from *reading* buttons to *configuring* the pen.

## 🎯 Goal
Meet the two X11 tools that configure the pen (position, area, pressure), and find your pen's
device name with each.

## 🧠 New idea: reading input vs configuring a device

Milestones 1–2 *read* button events and *sent* keystrokes. The pen is different: we mostly want to
*configure* how X11 already treats it — where it points, how pressure feels. Two tools do that:

- **`xinput`** — lists and tweaks every X11 input device. General-purpose. We'll use it for
  **mapping the pen to a monitor** (Lesson 3.3).
- **`xsetwacom`** — a specialized tool for devices on the *wacom* X driver (your pen is forced onto
  it via the `99-xppen.conf` rule from `CLAUDE.md`). Great for **pressure curve** and pen options
  (Lesson 3.4).

> ⚠️ Recall the core rule (`CLAUDE.md`): do **not** use `xsetwacom`'s **`key`** action to bind
> shortcuts (stuck-modifier bug). We use `xsetwacom` here only for *pen properties* like pressure
> and area — not for keybindings. Keybindings stay the evdev + xdotool way you already built.

Both are X11-only, so this milestone runs in your **XFCE/X11** session.

## 👀 See it

```bash
xinput list                     # every X11 input device; find the pen "stylus"
xsetwacom --list devices        # devices on the wacom driver
```

Look for names like **`Hanvon Ugee Deco Pro MW Pen stylus`**.

## ⌨️ Your turn

1. Run both commands and locate your **pen** entry in each.
2. Note the exact device **name** (and the numeric **id** xinput shows) — you'll pass these to the
   next lessons.
3. Peek at what's tweakable:
   ```bash
   xsetwacom --list parameters        # all the pen properties you can set
   ```
   Skim it — you'll recognize `Area`, `PressureCurve`, `Rotate` and more in the coming lessons.

**Hints**
- Device names with spaces must be quoted in commands: `xsetwacom --get "Hanvon Ugee Deco Pro MW
  Pen stylus" ...`.
- If the pen doesn't appear, confirm you're in the X11 session and the `99-xppen.conf`/driver setup
  from `CLAUDE.md` is in place — tell Claude what the lists show.

## ✅ Done when

You can name your pen device and have listed the parameters `xsetwacom` can set on it.

Tell Claude **"done with 3.1"**.

---
**Next:** Lesson 3.2 — Give the pen's own buttons shortcuts, reusing your M1/M2 engine.
