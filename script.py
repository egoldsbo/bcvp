""" sudo apt-get install python3-pygame """

import pygame
import sys
from pygame.locals import *
import barcode

# Initialize Pygame
pygame.init()

# Set the display to fullscreen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

def play_video(video_path):
    """ Play the video at the given path fullscreen. """
    # Load the video
    movie = pygame.movie.Movie(video_path)

    # Get the size of the movie
    movie_screen = pygame.Surface(movie.get_size()).convert()

    # Set the movie screen as the target for the movie
    movie.set_display(movie_screen)

    # Start playing the movie
    movie.play()

    # Keep playing until the movie is finished or quit is detected
    while movie.get_busy():
        screen.blit(movie_screen,(0,0))
        pygame.display.update()

        # Check for quit events
        for event in pygame.event.get():
            if event.type == QUIT:
                movie.stop()
                pygame.quit()
                sys.exit()

# Barcode scanner input setup
scanner = barcode.get_scanner('usb') # Adjust as needed for your scanner

while True:
    barcode_data = scanner.get_barcode() # Get barcode data

    if barcode_data:
        # Assuming barcode data corresponds to the video filename
        video_path = f'/vids/{barcode_data}.mp4'
        play_video(video_path)