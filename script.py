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

   # Set the width and height
    width, height = 800, 480
    media_player.video_set_scale(0)  # Disable default scaling
    media_player.video_set_size(width, height)


    # Wait for the video to finish
    while media_player.get_state() != vlc.State.Ended:
        time.sleep(1)


while True:
    # Ask the user to input the path of the video file
    video_path = "./vids/"+input("filename (or type 'exit' to quit): ")+".mp4"
    
    if video_path.lower() == 'exit':
        break
    
    play_video(video_path)
