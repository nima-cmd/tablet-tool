# Lesson 4.2 — Start automatically on login

> **Milestone 4 · Lesson 2 of 4**

## 🎯 Goal
Have the tool launch by itself when you log into your XFCE session, so you never have to start it by
hand.

## 🧠 New idea: autostart with a `.desktop` file

On Linux desktops, anything you want to run at login goes in **`~/.config/autostart/`** as a small
**`.desktop`** file — a plain-text description of "what to run and what to call it." XFCE reads that
folder when your session starts.

```ini
[Desktop Entry]
Type=Application
Name=Tablet Tool
Exec=/usr/bin/python3 /home/nima-cmd/Projects/tablet-tool/src/detect.py
X-GNOME-Autostart-enabled=true
```

`Exec` is just the command that would start your app from a terminal — full paths, so it works
regardless of the current folder.

> 💡 This is the same mechanism `CLAUDE.md` mentions for *disabling* the harmful XP-Pen vendor
> autostart (`Hidden=true`). You're using the friendly side of the same system.

## 👀 See it

```bash
ls ~/.config/autostart/           # what already autostarts (you'll see the disabled xppen entry)
```

## ⌨️ Your turn

1. Make sure your app runs cleanly from a full-path command first (this is exactly what autostart
   will do):
   ```bash
   /usr/bin/python3 /home/nima-cmd/Projects/tablet-tool/src/detect.py
   ```
   Fix any path/config issues now — autostart won't show you errors.
2. Create `~/.config/autostart/tablet-tool.desktop` with the entry above, adjusting the `Exec`
   path to *your* real path.
3. Log out and back in, then check it's running:
   ```bash
   pgrep -af detect.py
   ```

**Hints**
- Because it applies pen mapping/pressure (M3) at startup, autostart is what makes those "stick"
  every login — solving the "resets on reconnect" note from Milestone 3.
- If it doesn't start, run the exact `Exec` command in a terminal and read the error with Claude —
  usually a wrong path or a config not found (add full paths in the code, or `cd` in the Exec).
- Consider logging output to a file so you can debug silent startup failures — ask Claude how.

## ✅ Done when

After logging in, `pgrep -af detect.py` shows your tool already running, and pen settings apply
without you doing anything.

Tell Claude **"done with 4.2"**.

---
**Next:** Lesson 4.3 — A tiny GUI to see and edit your mappings.
