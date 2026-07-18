# Lesson 0.1 — The terminal, your control panel

> **Milestone 0 · Lesson 1 of 5** — read this in VS Code, do it with Claude in chat.

## 🎯 Goal
Open a terminal, run one command, and understand what you're looking at. That's it.

## 🧠 New idea: what *is* the terminal?

Most of the time you use a computer by clicking things. The **terminal** is a different door into
the same computer: instead of clicking, you **type a command** and press Enter, and the computer
**types back**. That's the whole loop — you type, it answers.

A few words you'll hear constantly:

- **Terminal** — the window.
- **Shell** — the program inside that window that reads your commands (yours is probably `bash`).
- **Command** — the instruction you type, e.g. `whoami`.
- **Prompt** — the little text that sits there waiting for you, often ending in `$`. You type
  *after* it.

Why we care: our whole app is run and tested from the terminal, and we install its tools here
too. Getting comfortable with this window is step one of everything else.

> 💡 You are on Pop!_OS with two login sessions. For this tool, do everything in the **XFCE
> (X11)** session — that's where the tablet and `xdotool` work. (Details are in `CLAUDE.md`; ask
> Claude if you're unsure which session you're in.)

## 👀 See it

Open a terminal (in XFCE: look for "Terminal" in the applications menu, or press its keyboard
shortcut). You'll see a prompt like:

```
you@pop-os:~$
```

That `~` means "your home folder." The `$` means "ready for a command."

## ⌨️ Your turn

Type each of these, one at a time, pressing Enter after each. Don't paste all at once — watch
what each one does.

1. `whoami` — prints your username. (Proves the loop works: you typed, it answered.)
2. `pwd` — "print working directory": which folder the terminal is currently *in*.
3. `ls` — "list": the files and folders where you are.
4. `cd tablet-tool` then `ls` — "change directory" into the project, then look around. You should
   see `CLAUDE.md`, `PLAN.md`, `README.md`, and our new folders.

> ✋ You won't type any Python yet. This lesson is purely about being unafraid of the terminal.

**Hints**
- If `cd tablet-tool` says "No such file or directory," you're not in the folder that *contains*
  it. Run `ls` to see what's around you, and ask Claude — we'll figure out the path together.
- Commands are case-sensitive and picky about spelling. `Ls` is not `ls`.

## ✅ Done when

You can run `pwd` and see a path ending in `/tablet-tool`, and `ls` shows the project files.

When that works, tell Claude **"done with 0.1"** — the ledger ticks 0.1 to done and lights up
0.2.

---
**Next:** Lesson 0.2 — Python: the REPL and your first script.
