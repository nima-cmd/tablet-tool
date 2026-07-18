# Lesson 3.4 — Shape the pressure curve

> **Milestone 3 · Lesson 4 of 4** — the milestone finale.

## 🎯 Goal
Adjust how hard you have to press for a given line weight — the "pressure curve" — and test it in
your drawing app.

## 🧠 New idea: the pressure curve

The pen reports how hard you press as a number. The **pressure curve** decides how that raw number
maps to output (line thickness/opacity). A softer curve = light touches give more effect; a firmer
curve = you must press harder. It's personal and worth tuning to your hand.

`xsetwacom` exposes this as **`PressureCurve`**, defined by four numbers (two control points of a
Bézier curve), each 0–100:

```bash
xsetwacom set "<pen name>" PressureCurve 0 0 100 100    # linear (the default-ish baseline)
xsetwacom set "<pen name>" PressureCurve 0 10 80 100    # softer: light presses do more
```

## 👀 See it

```bash
xsetwacom --get "Hanvon Ugee Deco Pro MW Pen stylus" PressureCurve    # current value
xsetwacom set  "Hanvon Ugee Deco Pro MW Pen stylus" PressureCurve 0 10 80 100
```

## ⌨️ Your turn

1. Check the current curve with `--get`.
2. Open your drawing app (Krita is ideal — its brush outline shows pressure well).
3. Try a few curves and draw after each, feeling the difference:
   - `0 0 100 100` (baseline)
   - `0 10 80 100` (softer start)
   - `10 0 100 90` (firmer)
4. Once you find one you like, save those four numbers in your config, and add a helper that
   applies it via `subprocess.run(["xsetwacom", "set", PEN_NAME, "PressureCurve", ...])`.

**Hints**
- Change one thing at a time and actually draw — pressure feel is hard to judge without testing.
- Like the monitor mapping, this resets on reconnect/login; Lesson 4.2 will re-apply it for you.
- Want more than a curve (e.g. min/max thresholds)? `xsetwacom --list parameters` shows the full
  set — explore with Claude.

## ✅ Done when

You've set a pressure curve you like and can re-apply it from a script/function.

🎉 **Milestone 3 done** — the pen now points where you want and feels how you want, on top of your
working shortcuts. Tell Claude **"done with 3.4"**. Milestone 4 turns all of this into a polished,
everyday tool.

---
**Next:** Lesson 4.1 — A friendly, robust config file.
