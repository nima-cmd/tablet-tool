#Set the pressure of the pen on the tablet
import subprocess

def set_pressure_curve(pen_name, curve):
    subprocess.run(["xsetwacom", "set", pen_name, "PressureCurve"] + [str(n) for n in curve])
