# CLAUDE.md — context for any Claude session in this repo

This file is auto-loaded by Claude Code. It carries over everything learned in the originating
session (the `2D-animation-tutorial` project) that's relevant to building this tool, so a fresh
session here starts fully caught up.

## What this project is

A custom app the **user is writing themselves** to replace the XP-Pen tablet software (which is
unusable on their machine), starting with **assigning shortcut keys** to the tablet's pen buttons
and pad express keys. Long-term it grows into full tablet config (pen→monitor mapping, pressure
curve, per-application profiles).

## How to work on this (IMPORTANT — working agreement)

- **The user writes the code. Claude guides, teaches, and reviews — do NOT hand over finished
  programs.** Explain concepts, scaffold, give hints, let them type it. This is a deliberate
  learning project.
- Favor **long-term, maintainable solutions over quick hacks.** The user has said this explicitly
  and repeatedly.
- Confirm the user's **programming experience level** early (was not yet established) to pace
  explanations — treat as beginner-friendly until told otherwise.
- This tool's approach also applies to the user's **Blender/Henwick** and **Godot Frieren-game**
  projects — it's a cross-project pattern of small custom workflow tools.

## Environment (verified facts)

- **OS:** Pop!_OS 24.04. Two desktop sessions, chosen at the cosmic-greeter login screen:
  - **COSMIC (Wayland):** daily driver. Everything works EXCEPT tablet pen input (its compositor
    doesn't route tablet/pressure — immature `tablet-v2` support).
  - **XFCE (X11):** the drawing/dev environment. Tablet works fully here.
- **GPU:** NVIDIA RTX 3070. The Claude Desktop app (Electron) freezes on X11 unless launched with
  `--disable-gpu` — already fixed via `~/.local/share/applications/claude-desktop.desktop`.
- **Tablet:** XP-Pen Deco Pro MW, wireless via 2.4GHz dongle, USB id `28bd:0934`. On X11 it's driven
  by the native kernel driver (`hid_uclogic`) forced onto the wacom X driver via
  `/etc/X11/xorg.conf.d/99-xppen.conf` (`MatchUSBID "28bd:0934"` → `Driver "wacom"`). The XP-Pen
  vendor driver is HARMFUL (misclassifies the pen) and its autostart is disabled
  (`~/.config/autostart/xppentablet.desktop`, Hidden=true). Do not re-enable it.
- Device names (evdev/xinput): `Hanvon Ugee Deco Pro MW Pen stylus`, `Hanvon Ugee Deco Pro MW Pad`
  (the pad = the 8 express keys + dial). Event node numbers vary; look them up at runtime.

## Critical design decision (learned the hard way)

Do **NOT** use `xsetwacom`'s `key` action to bind shortcuts — it has a stuck-modifier bug (Ctrl/Shift
stay held down; the keyboard then fires shortcuts on every keypress, and clicking gets buggy).
Instead:

1. **Read the tablet's raw button events** with Python `evdev` (works in ANY session).
2. **Send the intended keystroke with `xdotool`** (X11-only) — it presses AND releases modifiers
   correctly, so no stuck keys.

The pad's express keys are currently disabled at the xsetwacom level (`Button N 0`), so reading raw
evdev events is clean and won't double-fire.

## Stack & prerequisites

- **Python 3** + `python3-evdev`; **xdotool** for keystrokes.
- Install: `sudo apt install -y python3-evdev xdotool`
- User must be in the `input` group to read the tablet without sudo:
  `sudo usermod -aG input $USER` then re-login.
- Develop/run in the **XFCE (X11) session** (that's where xdotool works and where the tool lives).

## Milestones

- [ ] **M1 — Detect button presses.** Open the pad device, print which express key was pressed.
      (Also identifies which physical key = which code — never finalized yet.)
- [ ] **M2 — Map to shortcuts.** Config (button code → keystroke) + send via `xdotool` on press.
- [ ] **M3 — Pen buttons + pen→monitor mapping + pressure curve** (wrap `xsetwacom`/`xinput`).
- [ ] **M4 — Polish:** config file, autostart, simple GUI, per-app profiles.

## Status

Setup done (folder + plan). Next action: write M1 with the user (they type, Claude guides).
See `PLAN.md` for the same milestone list.
