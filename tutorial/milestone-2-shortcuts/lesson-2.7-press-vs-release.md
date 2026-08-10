# Lesson 2.7 — Press vs release: no double-fire

> **Milestone 2 · Lesson 7 of 7** — the milestone finale: a solid, reliable tool.

## 🎯 Goal
Guarantee that one physical press = exactly one shortcut, every time — no doubles, no misfires —
and understand *why*.

## 🧠 New idea: value 1 / 0 / 2, and firing on the edge

Recall a key event's **value**:
- **`1`** = the key just went **down** (pressed).
- **`0`** = the key just came **up** (released).
- **`2`** = the key is being **held** (auto-repeat).

If you don't filter, a single tap can produce a down *and* an up (and repeats if held) — firing
your shortcut 2+ times. The fix is to act only on the **press edge**, `value == 1`. That's the
moment a button "clicks," and it happens once per tap. (Filtering to `1` is what you did in 1.5 —
here we make sure it survived all the edits and reason about the edge cases.)

> 💡 Background from `CLAUDE.md`: the pad's express keys are disabled at the `xsetwacom` level
> (`Button N 0`), so reading raw evdev events is **clean** — you won't get phantom double-events
> from the X server on top of yours. Good; it means `value == 1` is genuinely all you need.

## 👀 See it

Tap a key slowly while `detect.py` runs with a debug print of every value:

```python
if event.type == ecodes.EV_KEY:
    print("code", event.code, "value", event.value)
```

You'll see a `1` on press and a `0` on release (and `2`s if you hold). Your action must key off the
`1` only.

## ⌨️ Your turn

1. Confirm your fire condition is exactly `if event.value == 1` before the lookup — so releases
   (`0`) and repeats (`2`) never trigger a shortcut.
2. Test deliberately:
   - **Quick tap** → shortcut fires **once**.
   - **Press and hold** → decide the behavior you want. For most shortcuts, "fire once on press,
     ignore the hold" is right (that's what `value == 1` gives you). If you *want* a key to repeat
     while held, that's where value `2` would come in — but keep it simple for now.
3. Remove any leftover debug prints so the tool is tidy.

**Hints**
- If you ever see doubles, add the debug print from "See it" and watch the values — the data tells
  you exactly what's firing.
- Holding a key and getting repeats you didn't want? You're catching `2`s somewhere — tighten to
  `== 1`.

## ✅ Done when

Every tap fires its shortcut exactly once, holds behave the way you chose, and no stray prints
remain.

🎉 **Milestone 2 complete — you have a working, configurable tablet shortcut app!** This is the
core of the whole tool. Tell Claude **"done with 2.7"**. From here, Milestones 3–4 are about the
pen and polish.

---
**Next:** Lesson 3.1 — Meet xinput & xsetwacom (the tools that configure the pen itself).
