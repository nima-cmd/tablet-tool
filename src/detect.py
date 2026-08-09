from evdev import InputDevice, list_devices, ecodes
import subprocess
import json
import selectors
import map_pen
import pressure
import sys
import os
from keymap import KEYS

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "config.json")




# Shortcut wishlist (Milestone 2 target)
# above_tl (256) -> ctrl+z         (undo)
# above_tr (257) -> ctrl+shift+z   (redo)
# above_bl (258) -> b              (brush tool)
# above_br (259) -> e              (eraser tool)
# below_tl (260) -> ctrl+s         (save)
# below_tr (261) -> ctrl+shift+a   (deselect)
# below_bl (262) -> [              (decrease brush size)
# below_br (263) -> ]              (increase brush size)



#bridges config file to detect
try:
    with open(CONFIG_PATH) as f:
        raw = json.load(f)
except FileNotFoundError:
    print("No config.json found - copy config.example.json to config.json")
    sys.exit(1)
except json.JSONDecodeError as e:
    print("config.json isn't valid JSON:",e)
    sys.exit(1)

pad_map = {int(code): combo for code, combo in raw.get("pad_shortcuts",{}).items()}
pen_map = {int(code): combo for code, combo in raw.get("pen_shortcuts",{}).items()}
SHORTCUTS = pad_map | pen_map

MONITOR = raw.get("monitor")
PRESSURE_CURVE = raw.get("pressure_curve")



#Find the Pad
pad = None      #Nothing found yet
for path in list_devices():
    device = InputDevice (path)
    if "Pad" in device.name:    #finds the pad
        pad = device

#Finds the Pen
pen = None
for path in list_devices():
    device = InputDevice(path)
    if "Pen" in device.name:
        pen = device

#Selector (Doorbell) that lets us listen to both devices
sel = selectors.DefaultSelector()
sel.register(pad, selectors.EVENT_READ)
sel.register(pen,selectors.EVENT_READ)

#tells us when pen or pad is detected
if pad:
    print("found the pad:", pad.name, "at", pad.path)
if pen:
    print("found the pen:", pen.name, "at", pen.path)
    map_pen.map_to_monitor(pen.name + " stylus", MONITOR) #maps pen to monitor
    pressure.set_pressure_curve(pen.name + " stylus", PRESSURE_CURVE)


#replaces if statement with infinite look always 
#listening for action picking pen or pad No longer stuck on first command
print("Listening... press a Pad key or click a pen button (Ctrl-C to stop).")
while True:
    for key, mask in sel.select():
        device = key.fileobj
        for event in device.read():
            if event.type == ecodes.EV_KEY and event.value == 1:
                combo = SHORTCUTS.get(event.code)
                if combo:
                    if combo.startswith("click:"):
                        button = combo.split(":", 1)[1]
                        subprocess.run(["xdotool", "click", button])
                    else:
                        subprocess.run(["xdotool", "key", combo])
                    print("fired", combo)
