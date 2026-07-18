# Lesson 2.1 — What is a keystroke? (keys & modifiers)

> **Milestone 2 · Lesson 1 of 7**

## 🎯 Goal
Understand how keyboard shortcuts are described in words, and decide what shortcut you want each of
your 8 keys to fire.

## 🧠 New idea: keys, modifiers, and combos

A **keystroke** is one press of a key. A **shortcut** is usually a key pressed *together with*
one or more **modifiers**:

- **Modifiers**: `ctrl`, `shift`, `alt`, `super` (the "Windows"/logo key). They don't do much
  alone — they *change* what another key means.
- **Combos** are written with `+`: `ctrl+z` (undo), `ctrl+shift+z` (redo), `ctrl+s` (save).

The tool we'll use, **xdotool**, speaks these exact strings: `"ctrl+z"`, `"ctrl+shift+z"`,
`"super"`, `"b"`. That's convenient — you'll write the shortcut the same way you'd say it.

> ⚠️ **The reason this project exists** (from `CLAUDE.md`/`PLAN.md`): the vendor approach with
> `xsetwacom`'s `key` action has a **stuck-modifier bug** — it holds Ctrl/Shift down and never
> lets go, so your keyboard starts misbehaving. `xdotool` presses **and releases** cleanly, which
> is why we build it this way. Keep this in mind; it's the core design decision.

## 👀 See it

Some common creative-app shortcuts, as xdotool strings:

| You want | xdotool string |
|---|---|
| Undo | `ctrl+z` |
| Redo | `ctrl+shift+z` |
| Save | `ctrl+s` |
| Brush tool (Krita) | `b` |
| Eraser (Krita) | `e` |
| Deselect | `ctrl+shift+a` |

## ⌨️ Your turn

This is a planning lesson — no code. Make your **wishlist**: for each of the 8 keys you mapped in
Lesson 1.6, decide the shortcut you want it to fire. Write it next to your `KEYS` notes, e.g.:

```
# key1 (code 259) -> ctrl+z   (undo)
# key2 (code 260) -> b        (brush)
# ...
```

**Hints**
- Pick shortcuts for whatever app you draw in most (Krita? Blender?). We can add per-app profiles
  much later (Lesson 4.4).
- Not sure of an app's shortcut? Check its menus — they usually show the shortcut next to each
  command.

## ✅ Done when

You have a written shortcut wishlist pairing each key's code with a desired xdotool string.

Tell Claude **"done with 2.1"**.

---
**Next:** Lesson 2.2 — Fire those shortcuts by hand with xdotool.
