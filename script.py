import subprocess
import os
import threading
import time

# Preload a small part of each video
def preload_videos(video_directory, preload_size=1024*1024):  # Preload the first 1MB of each video
    preloaded_videos = {}
    for filename in os.listdir(video_directory):
        if filename.endswith(".mp4"):
            file_path = os.path.join(video_directory, filename)
            with open(file_path, 'rb') as file:
                preloaded_videos[filename] = file.read(preload_size)
    return preloaded_videos

def play_video(video_path, preloaded_data=None):
    # Write preloaded data to a temporary file
    with open('/tmp/temp_video.mp4', 'wb') as temp_file:
        temp_file.write(preloaded_data)

    # Command to play video using mpv
    play_command = ['mpv', '--no-resume-playback', '/tmp/temp_video.mp4', video_path]

    # Execute the command and wait for it to finish
    subprocess.run(play_command)

# Directory where the video files are stored
video_directory = '/home/pi/bcvp/vids/'

# Preload videos
preloaded_videos = preload_videos(video_directory)

while True:
    video_file_name = input("Enter the name of the video file to play or 'exit' to quit: ")
    if video_file_name.lower() == 'exit':
        break

    video_file_path = os.path.join(video_directory, video_file_name) + '.mp4'

    if not os.path.exists(video_file_path):
        print("Video file not found. Please try again.")
    else:
        # Retrieve preloaded data if available
        preloaded_data = preloaded_videos.get(video_file_name + '.mp4', None)

        # Play the video using preloaded data
        if preloaded_data:
            play_video(video_file_path, preloaded_data)
        else:
            play_video(video_file_path)
