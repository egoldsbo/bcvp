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

def on_key_press(event):
    global typed_filename
    if event.keysym == 'Return':
        video_path = "./vids/" + typed_filename + ".mp4"
        play_video(video_path, media_player)
        typed_filename = ''  # Reset the filename after playing
    elif event.keysym == 'BackSpace':
        typed_filename = typed_filename[:-1]
    else:
        typed_filename += event.char

# Create a Tkinter window
root = tk.Tk()
root.title("VLC Media Player")
root.geometry("800x480")

# Create a VLC player
player = vlc.Instance()
media_player = player.media_player_new()

# Create a Frame to embed the VLC player
video_frame = tk.Frame(root, bg="black")
video_frame.pack(fill=tk.BOTH, expand=True)

# Set the VLC player's drawable to the frame's window ID
media_player.set_xwindow(video_frame.winfo_id())

# Initialize a variable to store typed filename
typed_filename = ''

# Bind key press event
root.bind('<KeyPress>', on_key_press)

root.mainloop()
