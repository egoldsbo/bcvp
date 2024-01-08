import subprocess
import os
import threading

def play_video(video_path):
    play_command = ['cvlc', 
                    '--no-osd', 
                    '--fullscreen', 
                    '--play-and-exit',
                     '--avcodec-hw=none', 
                     '--file-caching=300', 
                      '--no-audio', 
                    video_path]
    subprocess.run(play_command)

# Directory where the video files are stored
video_directory = '/home/pi/bcvp/vids/'

def start_video_thread(video_file_name):
    video_file_path = os.path.join(video_directory, video_file_name) + '.mp4'
    if os.path.exists(video_file_path):
        threading.Thread(target=play_video, args=(video_file_path,)).start()
    else:
        print("Video file not found. Please try again.")

while True:
    video_file_name = input("Enter the name of the video file to play, 'git' to update, or 'exit' to quit: ")

    if video_file_name.lower() == 'exit':
        break
    elif video_file_name.lower() == 'git':
        subprocess.run(['sudo', 'git', 'stash'])
        subprocess.run(['sudo', 'git', 'pull'])
        subprocess.run(['sudo', 'chmod', '+x', '/home/pi/bcvp/startupscript.sh'])
        subprocess.run(['sudo', 'chmod', '+x', '/home/pi/bcvp/script.py'])
    else:
        start_video_thread(video_file_name)
