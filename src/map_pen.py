#Script that lets us map to monitor
import subprocess

def map_to_monitor(pen_name, output="DP-0"):
    subprocess.run(["xinput", "map-to-output", pen_name, output])


