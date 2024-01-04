import subprocess
import os
import threading
import time

# Directory where the video files are stored
video_directory = '/home/pi/bcvp/vids/'

# Preload videos into memory
videos_in_memory = {}
for video_file_name in os.listdir(video_directory):
    video_file_path = os.path.join(video_directory, video_file_name)
    if os.path.isfile(video_file_path):
        with open(video_file_path, 'rb') as video_file:
            videos_in_memory[video_file_name] = video_file.read()

def play_video_from_memory(video_data, video_name):
    # Path for the temporary video file
    temp_video_path = '/dev/shm/' + video_name

    # Write video data to a temporary file in RAM
    with open(temp_video_path, 'wb') as temp_video_file:
        temp_video_file.write(video_data)

    # Command to play video using VLC
    play_command = ['cvlc', '--play-and-exit', '--no-audio', temp_video_path]

    # Execute the command and wait for it to finish
    subprocess.run(play_command)

    # Remove the temporary file
    os.remove(temp_video_path)

while True:
    # Prompt the user to enter the name of the video file
    video_file_name = input("Enter the name of the video file to play or 'exit' to quit: ") + '.mp4'

    # Check if the user wants to exit the program
    if video_file_name.lower() == 'exit.mp4':
        break

    # Check if the file is preloaded in memory
    if video_file_name in videos_in_memory:
        play_video_from_memory(videos_in_memory[video_file_name], video_file_name)
    else:
        print("Video file not found. Please try again.")
