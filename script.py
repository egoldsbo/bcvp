import subprocess
import os
import RPi.GPIO as GPIO
import time
import threading

def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(6, GPIO.OUT)
    GPIO.output(6, GPIO.LOW)
    GPIO.setup(5, GPIO.OUT)
    GPIO.output(5, GPIO.HIGH)
    GPIO.setup(13, GPIO.OUT)
    GPIO.output(13, GPIO.HIGH)

def video_playback_thread(video_path, single_play):
    global video_playing
    GPIO.output(6, GPIO.HIGH)
    GPIO.output(5, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)

    play_command = ['cvlc',
                    '--no-osd',
                    '--no-audio',
                    '--fullscreen',
                    '--file-caching=100',
                    '--no-loop',
                    '--play-and-exit',
                    '/home/pi/bcvp/vids/blackscreen.mp4',
                    video_path]

    if not single_play:
        play_command.append(video_path)

    subprocess.run(play_command)

    GPIO.output(6, GPIO.LOW)
    GPIO.output(5, GPIO.HIGH)
    GPIO.output(13, GPIO.HIGH)

    video_playing = False

def play_video(video_path, single_play):
    global video_playing, current_video_thread
    video_playing = True
    current_video_thread = threading.Thread(target=video_playback_thread, args=(video_path, single_play))
    current_video_thread.start()

def check_shutdown():
    global last_video_end_time
    while True:
        current_time = time.time()
        if current_time - last_video_end_time >= 1800:
            subprocess.run(['sudo', 'shutdown', 'now'])
            break
        time.sleep(60)

setup_gpio()

last_video_end_time = time.time()

shutdown_thread = threading.Thread(target=check_shutdown)
shutdown_thread.start()

video_directory = './vids/'
single_play_videos = ['dinor', 'ddd']

video_playing = False
current_video_thread = None

while True:
    if not video_playing:
        video_file_name = input("Enter the name of the video file to play, 'git' to update, or 'exit' to quit: ")

        if video_file_name.lower() == 'exit':
            GPIO.cleanup()
            break
        elif video_file_name.lower() == 'git':
            subprocess.run(['sudo', './gitscript.sh'])
        else:
            video_file_path = os.path.join(video_directory, video_file_name) + '.mp4'

            if not os.path.exists(video_file_path):
                print("Video file not found. Please try again.")
            else:
                single_play = video_file_name in single_play_videos
                play_video(video_file_path, single_play)
    else:
        if current_video_thread.is_alive():
            new_video_file_name = input("Enter the name of a new video file to play or 'skip' to continue current: ")
            if new_video_file_name.lower() != 'skip':
                current_video_thread.join()
                video_file_path = os.path.join(video_directory, new_video_file_name) + '.mp4'
                if os.path.exists(video_file_path):
                    single_play = new_video_file_name in single_play_videos
                    play_video(video_file_path, single_play)

    time.sleep(1)
