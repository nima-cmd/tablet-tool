# Tablet Tool — a custom XP-Pen replacement (built to learn)

A small program to configure the XP-Pen Deco Pro MW on Linux/X11 — assign shortcuts to the
pen buttons and pad express keys, map the pen to a monitor, tune pressure — because the vendor
software is unusable on this machine (COSMIC/Wayland dialog bug). Built by **me (the user)** as a
learning project, with Claude guiding rather than writing it.

## Core design decision (important — learned the hard way)

Do **NOT** use `xsetwacom`'s `key` action for shortcuts — it has a stuck-modifier bug (Ctrl/Shift
get left held down; the keyboard then fires shortcuts on every press). Instead:

1. **Read the tablet's button presses directly** from its input device (Python `evdev`).
2. **Send the keystroke with `xdotool`**, which presses AND releases modifiers correctly.

This is cleaner and more capable than the vendor app.

## Stack
- **Python 3** (with `python3-evdev`)
- **xdotool** for sending keystrokes (X11 only — so the shortcut-sending runs in the XFCE/X11 session)
- Reading button events works in any session; the pad device is e.g. `Hanvon Ugee Deco Pro MW Pad`

## Milestones
- [ ] **M1 — Detect button presses.** Script that opens the pad device and prints which express key
      was pressed. (Also identifies which physical key = which code.)
- [ ] **M2 — Map to shortcuts.** A config (button code → keystroke) + send via `xdotool` on press.
- [ ] **M3 — Pen buttons + pen-to-monitor mapping + pressure curve** (wrap `xsetwacom`/`xinput`).
- [ ] **M4 — Polish:** config file, autostart, simple GUI, per-app profiles (e.g. pressure in Krita,
      mouse-like in Blender).

## Prerequisites (one-time)
- `sudo apt install -y python3-evdev xdotool`
- `sudo usermod -aG input $USER`  (then re-login — lets the app read the tablet without sudo)

## Status
Setup in progress. Next: write M1.
