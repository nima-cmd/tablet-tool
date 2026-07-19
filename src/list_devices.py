from evdev import InputDevice, list_devices

for path in list_devices():
    device = InputDevice(path)
    print(path,"->", device.name)
