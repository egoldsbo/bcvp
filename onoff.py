import subprocess
import time

def turn_off_hdmi():
    subprocess.call('tvservice -o', shell=True)

def turn_on_hdmi():
    subprocess.call('tvservice -p', shell=True)
    subprocess.call('fbset -depth 8; fbset -depth 16', shell=True)

# Example usage
turn_off_hdmi()
time.sleep(5)  # Waits for 5 seconds
turn_on_hdmi()
