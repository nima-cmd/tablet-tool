# Lesson 2.2 — Drive xdotool by hand

> **Milestone 2 · Lesson 2 of 7**

## 🎯 Goal
Fire real keyboard shortcuts with xdotool from the terminal, and *feel* how it works, before we
call it from code.

## 🧠 New idea: xdotool sends keys to the focused window

xdotool types into whatever window currently has **focus** — the same window your real keyboard
would type into. So to test it, you focus an app, then fire the command. The `sleep` trick from the
smoke test gives you time to click back into the target app.

Two subcommands matter for us:
- `xdotool key <combo>` — press (and release) a shortcut, e.g. `xdotool key ctrl+z`.
- `xdotool type "<text>"` — type literal text (we used this in 0.5).

## 👀 See it

```bash
xdotool key ctrl+z              # fires undo into the focused window
xdotool sleep 2 key ctrl+s      # waits 2s (time to focus an app), then saves
```

## ⌨️ Your turn

Open an app you can safely test in (a text editor, or Krita/your drawing app):

1. Type some text, then fire undo:
   ```bash
   xdotool sleep 2 key ctrl+z
   ```
   (Click into the editor during the 2 seconds.) The last thing you typed should undo.
2. Work through **your Lesson 2.1 wishlist** — fire each shortcut by hand and confirm it does what
   you expect in that app:
   ```bash
   xdotool sleep 2 key ctrl+shift+z
   xdotool sleep 2 key b
   ```
3. Note any that don't behave — those are worth sorting now, while it's just the terminal.

**Hints**
- If a modifier ever *seems* stuck, add `--clearmodifiers`: `xdotool key --clearmodifiers ctrl+z`.
- Single letters like `b` are lowercase; for a capital use `shift+b` or `B`.
- The keystroke lands wherever focus is — if nothing happens, you probably fired it into the
  terminal. Use the `sleep` and click into the app.

## ✅ Done when

You can fire every shortcut on your wishlist by hand and see each do the right thing in your app.

Tell Claude **"done with 2.2"**.

---
**Next:** Lesson 2.3 — Do the same thing from inside Python.
