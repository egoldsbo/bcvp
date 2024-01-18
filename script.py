import subprocess
import os
import RPi.GPIO as GPIO  # Import the GPIO library

def setup_gpio():
    GPIO.setmode(GPIO.BCM)  # Use Broadcom SOC channel naming
    GPIO.setup(6, GPIO.OUT)  # Set GPIO 6 as an output
    GPIO.output(6, GPIO.HIGH)  # Set GPIO 6 HIGH initially

def play_video(video_path, single_play=False):
    # Set GPIO 6 LOW before playing the video
    GPIO.output(6, GPIO.LOW)

    play_command = ['cvlc',  # Using cvlc (command-line VLC)
                    '--no-osd',
                    '--no-audio',
                    '--fullscreen',
                    #'--avcodec-hw=none',  # Disable hardware acceleration
                    '--file-caching=100',  # Adjust file caching
                    '--no-loop',
                    '--play-and-exit',  # Exit VLC after playing the video
                    '/home/pi/bcvp/vids/blackscreen.mp4',  # Path to the video file
                    video_path]

    # Add video_path again if not in single play mode
    if not single_play:
        play_command.append(video_path)

    # Execute the command and wait for it to finish
    subprocess.run(play_command)

    # Set GPIO 6 HIGH after playing the video
    GPIO.output(6, GPIO.HIGH)


# Set up GPIO
setup_gpio()

# Directory where the video files are stored
video_directory = '/home/pi/bcvp/vids/'

# Array containing video file names to play only once
single_play_videos = ['dinor.mp4','ddd.mp4']# Replace with actual video names

# Flag to indicate if a video is playing
video_playing = False

while True:
    if not video_playing:
        video_file_name = input("Enter the name of the video file to play, 'git' to update, or 'exit' to quit: ")

        if video_file_name.lower() == 'exit':
            GPIO.cleanup()  # Clean up GPIO
            break
        elif video_file_name.lower() == 'git':
            subprocess.run(['sudo', './gitscript.sh'])
        else:
            video_file_path = os.path.join(video_directory, video_file_name) + '.mp4'

            if not os.path.exists(video_file_path):
                print("Video file not found. Please try again.")
            else:
                video_playing = True
                # Check if the video is in the single play list
                single_play = video_file_name in single_play_videos
                play_video(video_file_path, single_play)
                video_playing = False
