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
    global video_playing, current_process
    GPIO.output(6, GPIO.HIGH)
    GPIO.output(5, GPIO.LOW)

    play_command = ['cvlc',
                    '--no-osd',
                    '--no-audio',
                    '--fullscreen',
                    '--file-caching=100',
                    '--no-loop',
                    '--play-and-exit',
                    '/home/pi/bcvp/vids/blackscreen.mp4',
                    video_path]

    

    current_process = subprocess.Popen(play_command)
    current_process.wait()

    GPIO.output(6, GPIO.LOW)
    GPIO.output(5, GPIO.HIGH)
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
current_process = None
video_playing = False
current_video_thread = None
current_video_name = ''  # Track the name of the currently playing video

shutdown_thread = threading.Thread(target=check_shutdown)
shutdown_thread.start()

video_directory = './vids/'
single_play_videos = ['dinor', 'ddd']

while True:
    if not video_playing:
        video_file_name = input("Enter the name of the video file to play, 'git' to update, or 'exit' to quit: ").strip()

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
                current_video_name = video_file_name
                play_video(video_file_path, single_play)
    else:
        if current_video_thread.is_alive():
            new_video_file_name = input("Enter the name of a new video file to play or 'skip' to continue current: ").strip()
            if new_video_file_name.lower() != 'skip':
                if current_video_name in single_play_videos:
                    if current_process is not None:
                        current_process.terminate()
                    current_video_thread.join()
                current_video_name = new_video_file_name
                video_file_path = os.path.join(video_directory, current_video_name) + '.mp4'
                if os.path.exists(video_file_path):
                    single_play = current_video_name in single_play_videos
                    play_video(video_file_path, single_play)

    time.sleep(1)
