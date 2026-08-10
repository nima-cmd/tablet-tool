# The Tutorial — building the Tablet Tool from scratch

This folder holds the **lessons**. You read them in VS Code while Claude guides you live in
chat. You type the code; Claude explains, hints, and reviews — but does **not** hand you finished
programs. That's the whole point: you're learning by building.

## How a lesson works

Every lesson file follows the same shape so you always know where you are:

1. **🎯 Goal** — the one small thing this lesson achieves.
2. **🧠 New idea** — the single new concept or tool, explained in plain language.
3. **👀 See it** — something to run or look at, so the idea is concrete before you code.
4. **⌨️ Your turn** — the tiny bit *you* type. Hints, not solutions.
5. **✅ Done when** — how you know it worked. When it does, tell Claude and the ledger updates.

Each lesson teaches **one** tool or idea and produces just a few lines of code. Small on purpose.

## The map

We build in five milestones. Each is broken into bite-sized lessons.

### M0 — Foundations & Setup
Get comfortable with the terminal and Python, and install our two tools.
- **0.1** The terminal — your control panel
- **0.2** Python: the REPL and your first script
- **0.3** Install our two tools (evdev + xdotool)
- **0.4** Join the `input` group (read the tablet without sudo)
- **0.5** Smoke test — prove the tools work

### M1 — Detect button presses
Open the tablet's Pad and print which express key you pressed.
- **1.1** What is an input device?
- **1.2** List every input device with evdev
- **1.3** Find & open the tablet's Pad
- **1.4** The event loop — print raw events
- **1.5** Keep only the button presses
- **1.6** Build your key map (physical key → code)

### M2 — Map buttons to shortcuts
Press a button → fire a real keyboard shortcut via xdotool.
- **2.1** What is a keystroke? (keys & modifiers)
- **2.2** Drive xdotool by hand
- **2.3** Call xdotool from Python
- **2.4** First shortcut: one button → one keystroke
- **2.5** A dictionary of shortcuts
- **2.6** Move shortcuts into a config file
- **2.7** Press vs release — no double-fire

### M3 — Pen buttons, monitor mapping, pressure
Wrap `xinput`/`xsetwacom` to control the pen itself.
- **3.1** Meet xinput & xsetwacom
- **3.2** Pen button shortcuts
- **3.3** Map the pen to one monitor
- **3.4** Shape the pressure curve

### M4 — Polish & real-world use
Make it a tool you actually run every day.
- **4.1** A friendly config file
- **4.2** Start automatically on login
- **4.3** A tiny GUI
- **4.4** Per-application profiles

## Studying what you've learned

The **Grimoire** tab in `../ledger/index.html` is a running, parchment-themed reference of every
command and concept from every lesson so far (and every question you've asked along the way),
organized by milestone and explained in terms of this project's actual code. Open the ledger and
click the 📜 Grimoire tab. Look things up anytime, or ask Claude to quiz you on a chapter.

## Tracking progress

The **ledger** (`../ledger/index.html`) is your dashboard. Open it in a browser to see every
lesson, what's done, and what's next. Claude keeps it up to date by editing a small data block
inside that file — so updates are quick and cheap.

## Where your code lives

Your code goes in `../src/`. We'll create files there together as we reach the lessons that need
them. It starts empty on purpose.
