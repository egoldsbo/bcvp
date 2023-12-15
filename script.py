import tkinter as tk
import vlc
import time

def play_video(video_path, media_player):
    # Load the media file
    media = vlc.Media(video_path)

    # Set the media player media
    media_player.set_media(media)

    # Play the video
    media_player.play()

    # Wait for the video to finish
    while media_player.get_state() != vlc.State.Ended:
        time.sleep(1)

def start_video():
    filename = entry.get()
    video_path = "./vids/" + filename + ".mp4"
    play_video(video_path, media_player)

# Create a Tkinter window
root = tk.Tk()
root.title("VLC Media Player")
root.geometry("800x600")

# Create a VLC player
player = vlc.Instance()
media_player = player.media_player_new()

# Create a Frame to embed the VLC player
video_frame = tk.Frame(root, bg="black")
video_frame.pack(fill=tk.BOTH, expand=True)

# Set the VLC player's drawable to the frame's window ID
media_player.set_xwindow(video_frame.winfo_id())

# Entry widget for video filename
entry = tk.Entry(root)
entry.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

# Play button
play_button = tk.Button(root, text="Play Video", command=start_video)
play_button.pack(side=tk.BOTTOM)

root.mainloop()
