import tkinter as tk
import json
import os
from keymap import KEYS

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "config.json")

with open(CONFIG_PATH) as f:
    raw =json.load(f)

root = tk.Tk()
root.title("Tablet Tool")

pad_entries = {}
for code, combo in raw.get("pad_shortcuts", {}).items():
    row = tk.Frame(root)
    row.pack(anchor="w")
    tk.Label(row, text=f"  {KEYS.get(int(code), code)}").pack(side="left")
    entry = tk.Entry(row)
    entry.insert(0, combo)
    entry.pack(side="left")
    pad_entries[code] = entry


pen_entries = {}
for code, combo in raw.get("pen_shortcuts", {}).items():
    row = tk.Frame(root)
    row.pack(anchor="w")
    tk.Label(row, text=f"  {KEYS.get(int(code), code)}").pack(side="left")
    entry = tk.Entry(row)
    entry.insert(0, combo)
    entry.pack(side="left")
    pen_entries[code] = entry

def save():
    for code, entry in pad_entries.items():
        raw["pad_shortcuts"][code] = entry.get()
    for code, entry in pen_entries.items():
        raw["pen_shortcuts"][code] = entry.get()
    with open(CONFIG_PATH, "w") as f:
        json.dump(raw, f, indent=2)
    print("Saved!")

tk.Button(root, text="Save", command=save).pack(pady=10)


root.mainloop()