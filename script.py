import subprocess
import os
import threading
import time

# Function to turn off HDMI display
def turn_off_display():
    subprocess.run(['tvservice', '-o'])

# Function to turn on HDMI display
def turn_on_display():
    subprocess.run(['tvservice', '-p'])
    subprocess.run(['fbset', '-depth', '8'])
    subprocess.run(['fbset', '-depth', '16'])

# Timer class to handle display timeout
class DisplayTimer:
    def __init__(self, timeout=10):  # 180 seconds = 3 minutes
        self.timeout = timeout
        self.timer = None

    def reset_timer(self):
        if self.timer is not None:
            self.timer.cancel()
        self.timer = threading.Timer(self.timeout, turn_off_display)
        self.timer.start()

    def cancel_timer(self):
        if self.timer is not None:
            self.timer.cancel()

display_timer = DisplayTimer()

def play_video(video_path):
    # Ensure display is on
    turn_on_display()

    # Command to play video using FFmpeg in fullscreen mode
    play_command = ['ffplay', '-fs', '-autoexit', video_path]

    # Execute the command and wait for it to finish
    subprocess.run(play_command)

    # Reset the timer after video is played
    display_timer.reset_timer()

# Directory where the video files are stored
video_directory = './vids/'

while True:
    # Reset the timer for every loop iteration
    display_timer.reset_timer()

    # Prompt the user to enter the name of the video file
    video_file_name = input("Enter the name of the video file to play or 'exit' to quit: ")

    # Check if the user wants to exit the program
    if video_file_name.lower() == 'exit':
        display_timer.cancel_timer()
        break

    # Full path to the video file
    video_file_path = os.path.join(video_directory, video_file_name) + '.mp4'

    # Check if the file exists
    if not os.path.exists(video_file_path):
        print("Video file not found. Please try again.")
    else:
        play_video(video_file_path)

# Ensure display is on before the script ends
turn_on_display()
