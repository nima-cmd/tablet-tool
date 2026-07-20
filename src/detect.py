from evdev import InputDevice, list_devices

pad = None      #Nothing found yet
for path in list_devices():
    device = InputDevice (path)
    if "Pad" in device.name:    #finds the pad
        pad = device

if pad:
    print("found the pad:", pad.name, "at", pad.path)

    print("Listening... press the Pad's Express keys (Ctrl-C to stop).")
    for event in pad.read_loop():
        print(event)
else:
    print("Could not find the pad. Is the tablet plugged in?")