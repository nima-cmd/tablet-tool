from evdev import InputDevice, list_devices, ecodes
import subprocess


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

pad = None      #Nothing found yet
for path in list_devices():
    device = InputDevice (path)
    if "Pad" in device.name:    #finds the pad
        pad = device

if pad:
    print("found the pad:", pad.name, "at", pad.path)

    print("Listening... press the Pad's Express keys (Ctrl-C to stop).")
    for event in pad.read_loop():
        if event.type == ecodes.EV_KEY and event.value ==1:
            if event.code == 256:
                subprocess.run(["xdotool", "key", "ctrl+z"])
                print("fired ctrl+z")
else:
    print("Could not find the pad. Is the tablet plugged in?")