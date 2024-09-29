"""
    A place to put all the settings for the game.
"""
import pygame

# Initialize pygame and it's audio mixer.
pygame.init()
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=2048)
pygame.mixer.init()

# ########## DISPLAY ########## #
# Setup display variables by getting the screen resolution.
DISPLAY_INFO  = pygame.display.Info()
# SCREEN_RESOLUTION holds a tuple with the values of SCREEN_WIDTH & SCREEN_HEIGHT e.g (1920, 1080).
SCREEN_RESOLUTION = SCREEN_WIDTH, SCREEN_HEIGHT = DISPLAY_INFO.current_w, DISPLAY_INFO.current_h
# We'll use these setting to create a game window that is half the size of the screen.
WINDOW_SIZE = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2
# The game windows title.
TITLE = "Pygame Project"
