import vlc
import time

# Ask the user to input the path of the video file
video_path = "./vids/"+ input("filename: ") + ".mp4" 

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

# Wait for the video to finish
time.sleep(1)  # Wait for it to start playing
duration = media_player.get_length() / 1000  # Duration in seconds
time.sleep(duration)
