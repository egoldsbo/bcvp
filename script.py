import subprocess
import os

# Directory where the video files are stored
video_directory = './vids/'

# Prompt the user to enter the name of the video file
video_file_name = input("Enter the name of the video file to play: ")

# Full path to the video file
video_file_path = os.path.join(video_directory, video_file_name)+'.mp4'

# Check if the file exists
if not os.path.exists(video_file_path):
    print("Video file not found.")
else:
    # Command to play video using FFmpeg
    play_command = ['ffplay','-fs', video_file_path]

    # Execute the command
    subprocess.run(play_command)
