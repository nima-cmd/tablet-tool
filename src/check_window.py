import subprocess
import time

time.sleep(2)
result = subprocess.run(
    ["xdotool", "getactivewindow", "getwindowname"],
    capture_output=True, text=True
)
name = result.stdout.strip().lower()
print("active window name:", repr(name))
