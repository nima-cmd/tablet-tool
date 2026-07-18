# Lesson 3.2 — Pen button shortcuts

> **Milestone 3 · Lesson 2 of 4**

## 🎯 Goal
Make the two buttons on the pen barrel fire shortcuts too — by reusing the exact engine you built
for the Pad.

## 🧠 New idea: the same pattern, a second device

The pen is *also* an evdev device (`...Pen stylus`). So the buttons on it emit key events just like
the Pad's express keys. That means you don't need anything new — you need to **open a second
device** and run the same read-loop logic.

This nudges your code toward a nice shape: instead of one hard-coded `pad`, handle a **list of
devices**, each with its own shortcut map. Same loop, more inputs.

## 👀 See it

Two designs — pick with Claude based on how your code looks now:
- **Simple:** copy the detect logic, point it at the pen device, give it its own `SHORTCUTS`.
- **Cleaner (recommended long-term):** a small function `run_device(device, shortcuts)` you call
  for each device. This avoids duplicated loops — the DRY idea again.

Reading multiple devices at once (Pad *and* pen simultaneously) needs a way to watch several at
once — the `selectors` module, or evdev's async helpers. That's a real step up; do it with Claude.

## ⌨️ Your turn

1. Add the pen to your device discovery: find the device whose name contains `"Pen"` (mirror your
   Lesson 1.3 Pad-finding code).
2. Discover the pen buttons' **codes** the same way as Lesson 1.6: print key-down codes, click each
   pen button, record them.
3. Give the pen its own shortcut entries (in `config.json`), then fire them via the same
   `SHORTCUTS.get(code)` lookup.
4. Decide how to run **both** devices:
   - Start simple (test the pen alone), then
   - ask Claude to help watch Pad + pen **together** (this is where `selectors` comes in).

**Hints**
- The pen also emits lots of *motion/pressure* events while you draw — keep filtering to
  `EV_KEY` + `value == 1` so only real button clicks fire.
- Watching multiple devices in one loop is the genuinely new bit — flag it and we'll write it
  step by step; don't force it into a single `read_loop`.

## ✅ Done when

Pressing a pen barrel button fires its shortcut, and you have a plan (or working code) for handling
Pad and pen together.

Tell Claude **"done with 3.2"**.

---
**Next:** Lesson 3.3 — Confine the pen to a single monitor.
