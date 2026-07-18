# Tablet Tool

A custom app to configure an XP-Pen Deco Pro MW on Linux/X11 — assign shortcuts to the pen
buttons and pad express keys, map the pen to a monitor, tune pressure — because the vendor
software is unusable on this machine.

It's built as a **learning project**: a beginner-friendly, build-your-first-app tutorial where
**you write the code** and Claude guides, teaches, and reviews.

## The three parts of this repo

| Folder | What it is |
|---|---|
| [`tutorial/`](tutorial/README.md) | The lessons. Bite-sized, one concept each. Start here. |
| [`ledger/index.html`](ledger/index.html) | Your progress dashboard. Open it in a browser. |
| `src/` | Where the code you write will live (empty until we get there). |

## How to use it

1. **Open the ledger** (`ledger/index.html`) in your browser to see where you are.
2. **Open the current lesson** in VS Code (the ledger tells you which one).
3. **Work through it with Claude** in the VS Code Claude extension — you type, Claude guides.
4. When a lesson's "✅ Done when" is satisfied, **tell Claude** — it marks the lesson done in
   the ledger, and you reload the browser to see progress tick up.

## What we're building (the short version)

The vendor app has a stuck-modifier bug and doesn't work well here. So instead:

1. **Read the tablet's button presses directly** from its input device, using Python's `evdev`.
2. **Send the matching keyboard shortcut** with `xdotool`, which presses *and releases* keys
   cleanly (no stuck Ctrl/Shift).

Simple, reliable, and something you'll fully understand because you built it.

## The plan at a glance

- **M0** Foundations & setup → **M1** Detect button presses → **M2** Map to shortcuts →
  **M3** Pen buttons, monitor mapping, pressure → **M4** Polish (config, autostart, GUI, per-app
  profiles).

See [`tutorial/README.md`](tutorial/README.md) for the full lesson list, or the ledger for live
status.
