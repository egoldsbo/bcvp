import subprocess
import time

def turn_off_hdmi():
    subprocess.call('vcgencmd display_power 0', shell=True)

def turn_on_hdmi():
    subprocess.call('vcgencmd display_power 1', shell=True)

# Example usage
turn_off_hdmi()
time.sleep(5)  # Waits for 5 seconds
turn_on_hdmi()
time.sleep(5)
turn_off_hdmi()
time.sleep(5)
turn_on_hdmi()
