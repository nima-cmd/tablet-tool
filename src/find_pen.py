from evdev import InputDevice, list_devices, ecodes

pen = None
for path in list_devices():
    device = InputDevice(path)
    if "Pen" in device.name:
        pen = device

if pen:
    print("Found the pen:", pen.name, "at", pen.path)
    print("Listening... click the pen's barrel buttons (Ctrl-C to stop).")
    for event in pen.read_loop():
        if event.type == ecodes.EV_KEY and event.value == 1:
            print("pressed, code =", event.code)
else:
    print("Could not find the pen. Is the tablet plugged in?")

