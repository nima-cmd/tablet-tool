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
- **Grimoire pattern (reuse in other tutorial projects too):** this repo's `ledger/index.html` is a
  single HTML file with two tabs — a **Progress** tab (the existing `LEDGER` JS data block, unchanged)
  and a **Grimoire** tab: a parchment-themed, in-world "spellbook" reference of every command/concept
  taught, organized into chapters that mirror the milestones, written in terms of that project's
  actual code (not generic docs). Tabs are plain buttons toggling `.tabpanel` visibility via a few
  lines of JS — no framework. The Grimoire tab intentionally keeps its own fixed aged-paper look
  (CSS variables scoped under `#tab-grimoire`), independent of the app shell's light/dark theme.
  Decorative touches (a quill icon, a simple original magic-circle SVG divider between chapters) are
  hand-drawn inline SVG — never real copyrighted character art (e.g. no actual Frieren artwork).
  **Update the Grimoire continuously**: add an entry not just when a lesson introduces something new,
  but whenever the user asks a clarifying question about what they're doing — the grimoire should
  capture the real questions asked, not just the planned curriculum. When starting the equivalent
  tutorial system in Blender/Henwick or the Godot Frieren-game project, replicate this same
  two-tab-ledger structure there.

## Environment (verified facts)

- **OS:** Pop!_OS 24.04. Two desktop sessions, chosen at the cosmic-greeter login screen:
  - **COSMIC (Wayland):** daily driver — **and, as of 2026-08-07, the chosen environment for
    drawing too.** The old note here ("compositor doesn't route tablet/pressure") is
    **OUT OF DATE**. Re-verified in a live COSMIC session on 2026-08-07: `cosmic-comp`
    implements `zwp_tablet_manager_v2` (+ pad/ring/strip/dial), and XWayland exposes the pen
    with **Abs Pressure (0–65535)** and **Abs Tilt X/Y**. Pen and pressure work.
    What does NOT work here: `xsetwacom` (refuses to run under Wayland, so M3's pen config
    milestone needs rethinking), and the **pad is not forwarded to X11 apps** at all.
  - **XFCE (X11):** still works fully, still the fallback. Keep the xorg.conf.d rule.
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
2. ~~**Send the intended keystroke with `xdotool`**~~ — **SUPERSEDED 2026-08-07.** `xdotool` is
   X11-only and is a dead end now that we've moved to COSMIC/Wayland. **Send keystrokes through
   a `uinput` virtual keyboard instead** — `evdev.UInput` from the same library that already
   does the reading, so the whole tool becomes one dependency and works in **both** sessions.
   Verified on 2026-08-07, **no root required**: `/dev/uinput` is `crw-rw-rw-`, and a
   `UInput({e.EV_KEY: [...]})` device registers with the kernel as `Handlers=kbd` — which is
   exactly what libinput (and therefore cosmic-comp) enumerates. Press and release are explicit
   `write()` calls, so the original stuck-modifier bug still can't come back.
   *(Fallback if uinput ever fails: cosmic-comp also supports `zwp_virtual_keyboard_manager_v1`,
   so `wtype` would work — but uinput needs no compositor cooperation at all.)*

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

## Tutorial system (how this repo is organized)

This is a **build-your-first-app tutorial**, same spirit as the user's other learning projects.
Three parts:

- `tutorial/` — the lessons. Milestones broken into **bite-sized micro-lessons** (one tool/idea
  each). Every lesson has the same shape: 🎯 Goal · 🧠 New idea · 👀 See it · ⌨️ Your turn (hints,
  not solutions) · ✅ Done when. See `tutorial/README.md` for the full map.
- `ledger/index.html` — the **living progress ledger** the user opens in a browser. Its data is a
  single `const LEDGER = {…}` block near the top of the file. **To update progress, edit only that
  block** (flip a lesson's `status`, bump `updated`/`now`) — small diffs, cheap on tokens. Do NOT
  regenerate the whole file.
- `src/` — where the user's code goes. Starts empty; files created lesson by lesson.

### Working rhythm
The user works lessons in the **VS Code Claude extension** (Claude guides live, user types). This
web session set up the scaffolding. When the user says "done with X.Y", flip that lesson to
`done` and the next to `current` in the ledger, and update `now`/`updated`.

### Audience calibration (confirmed)
- **Experience: new to coding.** Explain every concept from scratch (what a variable is, what the
  terminal does). Assume nothing.
- **Lesson size: bite-sized micro-lessons.** One concept, a few lines of code, per lesson.

## Status

Tutorial fully authored: `README.md`, `ledger/index.html`, `src/`, and **all 26 lessons** written
across `tutorial/milestone-0-setup` … `milestone-4-polish` (M0 0.1–0.5, M1 1.1–1.6, M2 2.1–2.7,
M3 3.1–3.4, M4 4.1–4.4). Current lesson: **0.1 — the terminal**; the rest are ready to work through
in order. As the user finishes each ("done with X.Y"), flip that lesson's `status` in the ledger's
`LEDGER` block and advance the next to `current`. See `PLAN.md` and the ledger for milestone status.
