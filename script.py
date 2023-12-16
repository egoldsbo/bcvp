import subprocess
import os

def play_video(video_path, width, height, x_position, y_position):
    # Command to play video using FFmpeg
    play_command = [
        'ffplay', 
        '-x', str(width), 
        '-y', str(height), 
        '-autoexit', 
        '-left', str(x_position), 
        '-top', str(y_position), 
        video_path
    ]

    # Execute the command and wait for it to finish
    subprocess.run(play_command)

video_width = 800  # Example width
video_height = 480 # Example height

# Desired window position
x_position = 0  # Example X coordinate
y_position = 0  # Example Y coordinate

# Directory where the video files are stored
video_directory = './vids/'

while True:
    # Prompt the user to enter the name of the video file
    video_file_name = input("Enter the name of the video file to play or 'exit' to quit: ")

    # Check if the user wants to exit the program
    if video_file_name.lower() == 'exit':
        break

    # Full path to the video file
    video_file_path = os.path.join(video_directory, video_file_name) + '.mp4'

    # Check if the file exists
    if not os.path.exists(video_file_path):
        print("Video file not found. Please try again.")
    else:
        play_video(video_file_path, video_width, video_height, x_position, y_position)

    # Refocus to the terminal (optional)
    # subprocess.run(['wmctrl', '-a', 'Terminal']) # Uncomment if window manager supports it
