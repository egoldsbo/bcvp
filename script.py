import subprocess
import os

def play_video(video_path):
    # Command to play video using VLC in fullscreen mode
    play_command = ['cvlc', 
                    '--no-osd', 
                    '--no-audio', 
                    '--fullscreen', 
                    '--avcodec-hw=none',  # Disable hardware acceleration
                    '--file-caching=300',  # Adjust file caching
                    video_path]
    #a change
    # Execute the command and wait for it to finish
    subprocess.run(play_command)

# Directory where the video files are stored
video_directory = '/home/pi/bcvp/vids/'

# Flag to indicate if a video is playing
video_playing = False

while True:
    # Check if a video is not playing
    if not video_playing:
        # Prompt the user to enter the name of the video file
        video_file_name = input("Enter the name of the video file to play, 'git' to update, or 'exit' to quit: ")

        # Check if the user wants to exit the program
        if video_file_name.lower() == 'exit':
            break

        # Check if the user wants to run 'git pull'
        elif video_file_name.lower() == 'git':
            subprocess.run(['sudo', './gitscript.sh'])
           
        else:
            # Full path to the video file
            video_file_path = os.path.join(video_directory, video_file_name) + '.mp4'

            # Check if the file exists
            if not os.path.exists(video_file_path):
                print("Video file not found. Please try again.")
            else:
                # Set the flag to True, indicating a video is playing
                video_playing = True
                play_video(video_file_path)
                # Reset the flag to False after the video is done
                video_playing = False
