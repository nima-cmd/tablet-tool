# Lesson 3.3 — Map the pen to one monitor

> **Milestone 3 · Lesson 3 of 4**

## 🎯 Goal
Make the whole tablet surface map to **one** monitor (not stretched across all of them), so the pen
lands where you expect.

## 🧠 New idea: monitors, and mapping an input to an output

On a multi-monitor setup, by default the pen's rectangle is stretched across the *entire* desktop —
so drawing feels squished and the aspect ratio is wrong. You want the tablet to correspond to a
single screen.

- **`xrandr`** lists your monitors ("outputs") by name, e.g. `DP-2`, `HDMI-0`.
- **`xinput map-to-output <device> <output>`** ties the pen to one of them. X11 works out the
  coordinate math for you.

## 👀 See it

```bash
xrandr --listmonitors                 # names of your monitors
xinput map-to-output "Hanvon Ugee Deco Pro MW Pen stylus" DP-2   # example
```

After running the second command, the pen should only reach the `DP-2` screen.

## ⌨️ Your turn

1. Run `xrandr --listmonitors` and note the **output name** of the screen you draw on.
2. Map the pen to it:
   ```bash
   xinput map-to-output "<your pen name>" "<your output>"
   ```
   Test by hovering the pen at the tablet's corners — the cursor should hit that monitor's corners.
3. Wrap it in a tiny helper so it's repeatable — a shell script, or a Python function using
   `subprocess.run([...])` (same tool as your keystrokes):
   ```python
   subprocess.run(["xinput", "map-to-output", PEN_NAME, OUTPUT])
   ```
4. Add the chosen output to your config so it's not hard-coded.

**Hints**
- The aspect ratios of the tablet and monitor may differ; if circles look like ovals, we can also
  set the tablet **Area** with `xsetwacom` to match — ask Claude when you get there.
- This mapping resets when the tablet reconnects or you log in again — that's fine; Lesson 4.2
  (autostart) will re-apply it automatically.

## ✅ Done when

The pen reaches exactly one monitor's corners, and you can re-apply the mapping from a script/
function.

Tell Claude **"done with 3.3"**.

---
**Next:** Lesson 3.4 — Tune how pressure feels.
