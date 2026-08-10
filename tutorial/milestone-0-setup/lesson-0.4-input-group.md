# Lesson 0.4 — Join the `input` group (read the tablet without sudo)

> **Milestone 0 · Lesson 4 of 5**

## 🎯 Goal
Give your user account permission to read the tablet directly, so we never have to run our app as
administrator.

## 🧠 New idea: users, groups, and permissions

Linux protects hardware behind **permissions**. Every device shows up as a special file under
`/dev/input/`, and each of those files is **owned** by a user and a **group**. Only people in the
right group are allowed to read it.

- A **user** is you (`nima-cmd`).
- A **group** is a named team of users. Permissions are often granted to a *group*, then you just
  add yourself to that group.
- The tablet's device files belong to a group called **`input`**. So: add yourself to `input`, and
  you can read the tablet — no `sudo` needed.

> 💡 Why avoid `sudo`? Running everyday programs as administrator is a bad habit — a mistake as
> root can damage the system. The clean, long-term-correct approach (which this project always
> prefers) is to grant *just* the one permission we need. This is that.

## 👀 See it

Look at who owns a tablet device file and what groups you're currently in:

```bash
ls -l /dev/input/event*      # look at the group column (3rd-ish); many say "input"
groups                       # the groups you belong to right now
```

Right now `groups` probably does **not** list `input`. We're about to fix that.

## ⌨️ Your turn

1. Add yourself to the `input` group:
   ```bash
   sudo usermod -aG input $USER
   ```
   Reading it: `usermod` = modify a user, `-aG input` = **a**dd to **G**roup `input` (the `-a` is
   critical — it *adds* without removing your other groups), `$USER` = your username, filled in
   automatically.
2. **Log out and log back in.** Group changes only take effect on a fresh login. (A reboot works
   too.) This step is easy to forget and then nothing seems to work — so really do it.
3. After logging back in, confirm:
   ```bash
   groups
   ```
   You should now see `input` in the list.

**Hints**
- If `groups` still doesn't show `input` after re-login, a full reboot guarantees it.
- Don't skip the `-a` in `-aG` — without it you'd *replace* your groups, which you don't want.

## ✅ Done when

`groups` includes **input** in its output.

Tell Claude **"done with 0.4"** to update the ledger.

---
**Next:** Lesson 0.5 — Smoke test: prove both tools actually work before we build.
