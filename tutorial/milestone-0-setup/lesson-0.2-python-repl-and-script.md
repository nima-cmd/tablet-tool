# Lesson 0.2 — Python: the REPL and your first script

> **Milestone 0 · Lesson 2 of 5**

## 🎯 Goal
Run Python two ways: **live** (the REPL) and **from a file** (a script). Understand the
difference. Print one line of text each way.

## 🧠 New idea: Python, and two ways to run it

**Python** is the programming language we'll write the app in. It's known for reading almost like
English, which is why it's a great first language.

There are two ways to run Python, and you'll use both constantly:

1. **The REPL** (say "repple") — a live conversation. You type one line of Python, press Enter,
   and it runs *immediately*. Great for trying things out. REPL = Read-Eval-Print-Loop: it
   **reads** your line, **evaluates** it, **prints** the result, and **loops** back for more.
2. **A script** — a file full of Python (ending in `.py`). You run the whole file at once. This
   is how real programs live, because you can save them, edit them, and run them again tomorrow.

Rule of thumb: **REPL to experiment, script to keep.**

## 👀 See it — the REPL

In your terminal, type:

```
python3
```

The prompt changes to `>>>`. You're now *inside* Python. Try:

```python
>>> print("hello from the REPL")
```

It answers right away. Now try plain arithmetic — Python is also a calculator:

```python
>>> 2 + 2
```

To leave the REPL and go back to the normal terminal, type `exit()` and Enter (or press Ctrl-D).

> 🧩 `print(...)` is a **function**: a built-in action. The thing in the parentheses is what you
> give it. The quotes make it a **string** — plain text. We'll meet both properly soon; for now
> just notice the shape: `print("...")`.

## ⌨️ Your turn — your first script

Now make a file and run it. We'll put practice files in the `src/` folder.

1. In VS Code, create a new file: `src/hello.py`
2. On line 1, type (yourself — don't copy-paste, typing builds memory):

   ```python
   print("hello from a script")
   ```
3. Save the file (Ctrl-S).
4. Back in the terminal, from inside the `tablet-tool` folder, run it:

   ```
   python3 src/hello.py
   ```

You should see your line printed.

**Hints**
- `python3 src/hello.py` means "Python, run the file at this path." If it says "No such file,"
  check with `pwd` that you're in `tablet-tool`, and that the file really saved (VS Code shows a
  dot on the tab if there are unsaved changes).
- A common first bug: a missing quote or parenthesis. Python will point at the line — read the
  message, and show Claude if it's confusing. Reading errors is a real skill; we'll practice it.

## ✅ Done when

- You ran a line in the REPL and saw it respond, **and**
- `python3 src/hello.py` prints your message.

Tell Claude **"done with 0.2"** to update the ledger.

---
**Next:** Lesson 0.3 — Install our two tools (evdev + xdotool).
