import vlc
import sys

# Dictionary mapping barcodes to video file paths
barcode_to_video = {
    "walk": "./vids/walk.mp4"
 
    # Add more barcodes and corresponding video paths here
}

def play_video(video_path):
    """ Play video at the given path """
    player = vlc.MediaPlayer(video_path)
    player.set_fullscreen(True)
    player.play()
    while player.is_playing():
        pass
    player.stop()

def main():
    try:
        while True:
            barcode = input("Scan barcode: ")
            video_path = barcode_to_video.get(barcode)
            if video_path:
                print(f"Playing video for barcode {barcode}")
                play_video(video_path)
            else:
                print("No video found for this barcode.")
    except KeyboardInterrupt:
        print("Program exited.")
        sys.exit()

if __name__ == "__main__":
    main()