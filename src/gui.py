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

content = tk.Frame(root)
content.pack()

pad_entries = {}
pen_entries = {}
current_profile = raw.get("default_profile", "krita")

def show_profile(profile_name):
    global current_profile
    current_profile = profile_name

    for widget in content.winfo_children():
        widget.destroy()
    pad_entries.clear()
    pen_entries.clear()

    profile = raw["profiles"][profile_name]

    for code, combo in profile.get("pad_shortcuts", {}).items():
        row = tk.Frame(content)
        row.pack(anchor="w")
        tk.Label(row, text=f"  {KEYS.get(int(code), code)}").pack(side="left")
        entry = tk.Entry(row)
        entry.insert(0, combo)
        entry.pack(side="left")
        pad_entries[code] = entry

    for code, combo in profile.get("pen_shortcuts", {}).items():
        row = tk.Frame(content)
        row.pack(anchor="w")
        tk.Label(row, text=f"  {KEYS.get(int(code), code)}").pack(side="left")
        entry = tk.Entry(row)
        entry.insert(0, combo)
        entry.pack(side="left")
        pen_entries[code] = entry

button_row = tk.Frame(root)
button_row.pack()
tk.Button(button_row, text="Krita", command=lambda: show_profile("krita")).pack(side="left")
tk.Button(button_row, text="Blender", command=lambda: show_profile("blender")).pack(side="left")

show_profile(current_profile)


def save():
    for code, entry in pad_entries.items():
        raw["profiles"][current_profile]["pad_shortcuts"][code] = entry.get()
    for code, entry in pen_entries.items():
        raw["profiles"][current_profile]["pen_shortcuts"][code] = entry.get()
    with open(CONFIG_PATH, "w") as f:
        json.dump(raw, f, indent=2)
    print("Saved!")

tk.Button(root, text="Save", command=save).pack(pady=10)



root.mainloop()