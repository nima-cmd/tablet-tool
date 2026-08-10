# Lesson 0.3 — Install our two tools (evdev + xdotool)

> **Milestone 0 · Lesson 3 of 5**

## 🎯 Goal
Install the two pieces of software our app is built on, and confirm each one is really there.

## 🧠 New idea: packages, `apt`, and "library vs program"

Software on Linux comes in **packages** — tidy bundles you install with one command. Pop!_OS uses
a package manager called **`apt`**. You tell it a package name, it fetches and installs it.

We need two things, and they're different *kinds* of thing:

- **`python3-evdev`** — a **library**. A library is code you use *from inside* your own Python
  program (you'll write `import evdev`). It's how we'll *read* the tablet's buttons.
- **`xdotool`** — a **program**. A program is something you run *by name* from the terminal (or
  that your code runs for you). It's how we'll *send* keystrokes.

So: one tool listens to the tablet, the other talks to the screen. That's the whole app in a
sentence.

> 💡 Why `python3-evdev` and not just `pip install evdev`? On Pop!_OS the system Python prefers
> packages installed through `apt` — it avoids a class of "externally-managed-environment" errors
> beginners often hit with `pip`. We're taking the smooth road on purpose.

## 👀 See it

The install command (we'll run it in a second):

```bash
sudo apt install -y python3-evdev xdotool
```

Word by word: **`sudo`** = "do this as administrator" (installing software needs permission),
**`apt install`** = "install these packages", **`-y`** = "yes, don't ask me to confirm", then the
two package names.

## ⌨️ Your turn

1. Run the install (it'll ask for your login password — typing shows nothing, that's normal, just
   type and Enter):
   ```bash
   sudo apt install -y python3-evdev xdotool
   ```
2. Confirm **evdev** is importable (this runs one line of Python and exits):
   ```bash
   python3 -c "import evdev; print('evdev OK')"
   ```
   Seeing `evdev OK` means the library is installed and Python can find it.
3. Confirm **xdotool** exists:
   ```bash
   xdotool --version
   ```

**Hints**
- `python3 -c "..."` means "run this one line of Python." If you get `ModuleNotFoundError: No
  module named 'evdev'`, the install didn't take — re-run step 1 and read its output with me.
- If `sudo` says you're "not in the sudoers file," tell me — that's a permissions thing we'll sort.

## ✅ Done when

`python3 -c "import evdev; print('evdev OK')"` prints **evdev OK**, and `xdotool --version` prints
a version line.

Tell Claude **"done with 0.3"** to update the ledger.

---
**Next:** Lesson 0.4 — Join the `input` group (so you can read the tablet without `sudo`).
