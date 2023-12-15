import vlc
import time

def play_video(video_path):
    # Create a VLC instance
    player = vlc.Instance()

    # Create a new player
    media_player = player.media_player_new()

    # Load the media file
    media = player.media_new(video_path)

    # Set the media player media
    media_player.set_media(media)

    # Play the video
    media_player.play()

    time.sleep(3)

    # Set to full screen
    media_player.set_fullscreen(True)

    # Wait for the video to finish
    while media_player.get_state() != vlc.State.Ended:
        time.sleep(1)

while True:
    # Ask the user to input the filename
    filename = input("filename (or type 'exit' to quit): ")

    # Check for 'exit' condition
    if filename.lower() == 'exit':
        break

    # Append the path and file extension
    video_path = "./vids/" + filename + ".mp4"
    
    # Play the video
    play_video(video_path)
