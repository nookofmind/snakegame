import pygame
import random
import time

# Welcome message
print('Welcome to the snake game')

# Initial score
score = 0

# Defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
lavender = pygame.Color(235, 150, 235)
magenta = pygame.Color(224, 81, 148)
salmon = pygame.Color(255, 141, 133)

# Defining snake speed
snake_speed = 10

# Window size
window_x = 500
window_y = 500

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('Dora explora el juego de serpiente')
game_window = pygame.display.set_mode((window_x, window_y))

# Display window
game_window.fill(magenta)
pygame.display.flip()

while True:
    pass




