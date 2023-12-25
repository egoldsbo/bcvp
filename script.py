import subprocess
import os
import threading
import time

shutdown_timer = None
inactivity_limit = 60  # Inactivity time limit in seconds

def play_video(video_path):
    global shutdown_timer

    # Resetting the shutdown timer
    if shutdown_timer is not None:
        shutdown_timer.cancel()

    # Command to play video using FFmpeg in fullscreen mode
    play_command = ['ffplay', '-fs', '-autoexit', video_path]

    # Execute the command and wait for it to finish
    subprocess.run(play_command)

    # Restart the shutdown timer after the video finishes
    shutdown_timer = threading.Timer(inactivity_limit, shutdown_pi)
    shutdown_timer.start()

def shutdown_pi():
    print("Shutting down due to inactivity.")
    subprocess.run(['sudo', 'shutdown', 'now'])

# Directory where the video files are stored
video_directory = '/media/egoldsbo/USB Drive/vids/'

# Start the shutdown timer
shutdown_timer = threading.Timer(inactivity_limit, shutdown_pi)
shutdown_timer.start()

while True:
    # Prompt the user to enter the name of the video file
    video_file_name = input("Enter the name of the video file to play or 'exit' to quit: ")

    # Check if the user wants to exit the program
    if video_file_name.lower() == 'exit':
        if shutdown_timer is not None:
            shutdown_timer.cancel()
        break

    # Full path to the video file
    video_file_path = os.path.join(video_directory, video_file_name) + '.mp4'

    # Check if the file exists
    if not os.path.exists(video_file_path):
        print("Video file not found. Please try again.")
    else:
        play_video(video_file_path)
