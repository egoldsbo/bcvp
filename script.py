import subprocess
import os

def play_video(video_path):
    # Command to play video using FFmpeg in fullscreen mode
    play_command = ['cvlc', '--no-audio', '--play-and-exit', video_path]

    # Execute the command and wait for it to finish
    subprocess.run(play_command)

def connect_to_wifi():
    # Prompt for WiFi credentials
    network_name = input("Enter the WiFi network name (SSID): ")
    password = input("Enter the WiFi password: ")

    # Configuration string for wpa_supplicant.conf
    config_string = f'\nnetwork={{\n    ssid="{network_name}"\n    psk="{password}"\n}}\n'

    # Append configuration to wpa_supplicant.conf
    with open('/etc/wpa_supplicant/wpa_supplicant.conf', 'a') as file:
        file.write(config_string)

    # Restart the network interface to apply changes
    subprocess.run(['sudo', 'wpa_cli', '-i', 'wlan0', 'reconfigure'])

# Directory where the video files are stored
video_directory = '/home/pi/bcvp/vids/'

while True:
    # Prompt the user to enter the name of the video file
    video_file_name = input("Enter the name of the video file to play, 'wifi' to connect to WiFi, 'gitupdate' to update, or 'exit' to quit: ")

    # Check if the user wants to exit the program
    if video_file_name.lower() == 'exit':
        break

    # Check if the user wants to run 'git pull'
    if video_file_name.lower() == 'gitupdate':
        # Run 'git pull' command
        subprocess.run(['git', 'pull'])
        # Exit the loop
        break

    # Check if the user wants to connect to WiFi
    if video_file_name.lower() == 'wifi':
        # Connect to WiFi
        connect_to_wifi()
        # Exit the loop
        break

    # Full path to the video file
    video_file_path = os.path.join(video_directory, video_file_name) + '.mp4'

    # Check if the file exists
    if not os.path.exists(video_file_path):
        print("Video file not found. Please try again.")
    else:
        play_video(video_file_path)
