# Lesson 0.5 — Smoke test: prove the tools work

> **Milestone 0 · Lesson 5 of 5** — last lesson of setup. After this, we build.

## 🎯 Goal
Do the smallest possible check that *both* halves of the app are alive: evdev can see devices, and
xdotool can send a keystroke. Then setup is officially done.

## 🧠 New idea: a "smoke test"

The name comes from electronics: plug it in, and if no smoke comes out, the basics are probably
fine. In software, a **smoke test** is the tiniest experiment that proves the pieces are wired up
before you build anything real on top of them. It saves you from debugging a big program when the
actual problem was "the tool was never installed."

We'll do two five-second checks.

## 👀 See it

Two tiny commands, one per tool. You'll run them yourself below.

## ⌨️ Your turn

**Check 1 — evdev can see your input devices:**
```bash
python3 -c "import evdev; print(evdev.list_devices())"
```
This should print a Python list of device paths, like `['/dev/input/event2', '/dev/input/event5', ...]`.
An **empty list `[]`** almost always means the `input` group from Lesson 0.4 hasn't taken effect —
log out/in (or reboot) and try again.

**Check 2 — xdotool can type for you:**
1. Open a text editor (or a browser search box) and click into it so it has focus.
2. Wait a moment, then run this in the terminal:
   ```bash
   xdotool sleep 2 type "hello from xdotool"
   ```
   The `sleep 2` gives you two seconds to click back into the editor. You should see the text
   appear *in the editor*, typed by the tool.
3. Try a real shortcut too — click into the editor, then:
   ```bash
   xdotool sleep 2 key ctrl+a
   ```
   That should select all the text (Ctrl+A). This is exactly the mechanism our app will use.

**Hints**
- Whatever window is **focused** when the command fires is where the keystroke lands — that's why
  we click into the editor and use `sleep`.
- If `list_devices()` prints `[]`, it's the group/login thing from 0.4, not a code problem.

## ✅ Done when

- Check 1 prints a non-empty list of `/dev/input/...` paths, **and**
- Check 2 makes text appear / selects text in your editor.

That's Milestone 0 complete — your environment is ready. 🎉 Tell Claude **"done with 0.5"** and
we move to **Milestone 1**, where you write your first real code and read the tablet's buttons.

---
**Next:** Lesson 1.1 — What is an input device? (the mental model behind everything we're about to
build).
