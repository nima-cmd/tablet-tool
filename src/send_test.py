import subprocess
import time

time.sleep(2)                                   # 2s to focus your app
subprocess.run(["xdotool", "key", "b"])
print("sent ctrl+z")
