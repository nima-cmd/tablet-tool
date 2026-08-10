# Lesson 1.1 — What is an input device?

> **Milestone 1 · Lesson 1 of 6** — the mental model behind everything we build next.

## 🎯 Goal
Understand, in plain terms, what actually happens when you press a button on the tablet — so the
code in the next lessons feels obvious instead of magic.

## 🧠 New idea: the kernel, device files, and events

When you press a key, tap the pen, or move the mouse, here's the chain:

1. The hardware sends a signal to the **kernel** — the core of the operating system that talks to
   hardware.
2. The kernel represents each input gadget as a **device file** under `/dev/input/` (e.g.
   `/dev/input/event5`). Reading that file = listening to that gadget.
3. What you read are **events**. Every event has three parts:
   - **type** — what *kind* of thing happened (a key/button? a movement?).
   - **code** — *which* specific key/button/axis.
   - **value** — the detail (for a button: `1` = pressed down, `0` = released, `2` = held/repeat).

So "I pressed express key #3" becomes an event roughly like *type: key, code: 259, value: 1*. Our
whole M1 job is: **open the right device file, read these events, and make sense of them.**

Your tablet shows up as **two** devices (from `CLAUDE.md`):
- `Hanvon Ugee Deco Pro MW Pen stylus` — the pen.
- `Hanvon Ugee Deco Pro MW Pad` — the **Pad**: the 8 express keys + the dial. This is our M1 target.

## 👀 See it

Peek at the device files the kernel has created:

```bash
ls /dev/input/
ls -l /dev/input/by-id/     # friendlier names, sometimes including the vendor
```

The plain `eventN` numbers change between reboots and plug-ins — which is exactly why, in the next
lesson, we'll find our device **by its name** instead of hard-coding a number.

## ⌨️ Your turn

This lesson is understanding, not coding. Do this:

1. Run the two `ls` commands above and look at what's there.
2. In your own words (say it to Claude, or jot it in a comment), answer:
   - What are **type**, **code**, and **value** in an input event?
   - Why is it a bad idea to hard-code `/dev/input/event5` in our program?

**Hints**
- The answer to the second question is in the "See it" note above.
- If you want a live preview of raw events, there's a tool called `evtest` (`sudo apt install
  evtest`, then `sudo evtest`) — optional, but fun to watch. We'll do the same thing in Python
  next, without needing `sudo`.

## ✅ Done when

You can explain type/code/value and why we'll look devices up by name. Tell Claude **"done with
1.1"**.

---
**Next:** Lesson 1.2 — List every input device with evdev (your first real Python for this app).
