from evdev import InputDevice, list_devices, ecodes
import subprocess
import json
import selectors


# Physical key -> code (measured on my Deco Pro MW)
# above-dial top-left     = 256
# above-dial top-right    = 257
# above-dial bottom-left  = 258
# above-dial bottom-right = 259
# below-dial top-left     = 260
# below-dial top-right    = 261
# below-dial bottom-left  = 262
# below-dial bottom-right = 263

# Shortcut wishlist (Milestone 2 target)
# above_tl (256) -> ctrl+z         (undo)
# above_tr (257) -> ctrl+shift+z   (redo)
# above_bl (258) -> b              (brush tool)
# above_br (259) -> e              (eraser tool)
# below_tl (260) -> ctrl+s         (save)
# below_tr (261) -> ctrl+shift+a   (deselect)
# below_bl (262) -> [              (decrease brush size)
# below_br (263) -> ]              (increase brush size)

KEYS = {
    256: "above_tl",
    257: "above_tr",
    258: "above_bl",
    259: "above_br",
    260: "below_tl",
    261: "below_tr",
    262: "below_bl",
    263: "below_br",
}

with open("config.json") as f:
    raw = json.load(f)
SHORTCUTS = {int(code): combo for code, combo in raw.items()} #string Keys -> int keys

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
