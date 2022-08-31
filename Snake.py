import pygame
import random
import time
from pygame import mixer

# Defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
lavender = pygame.Color(235, 150, 235)
magenta = pygame.Color(224, 81, 148)
salmon = pygame.Color(255, 141, 133)

# Defining window size
window_x = 500
window_y = 500

# Snake class
class snakeClass:
    def __init__(self):
        self.snakeStartingLenght = 1
        self.snakeStartingBodyPositions = [[0, 0]]
        self.snakeDirection = 'right'
        self.desiredDirection = 'none'
        self.snakePartSize = 20
        self.snakeSpeed = 10

    # Move snake
    def moveSnake(self):
        for snakePart in self.snakeStartingBodyPositions:
            if self.snakeDirection == 'right':
                snakePart[0] = snakePart[0] + self.snakePartSize
            elif self.snakeDirection == 'left':
                snakePart[0] = snakePart[0] - self.snakePartSize
            elif self.snakeDirection == 'up':
                snakePart[1] = snakePart[1] - self.snakePartSize
            elif self.snakeDirection == 'down':
                snakePart[1] = snakePart[1] + self.snakePartSize

    # Change direction
    def changeDirection(self):
        if self.desiredDirection == 'right' and self.snakeDirection != 'left':
            self.snakeDirection = self.desiredDirection
        elif self.desiredDirection == 'left' and self.snakeDirection != 'right':
            self.snakeDirection = self.desiredDirection
        elif self.desiredDirection == 'up' and self.snakeDirection != 'down':
            self.snakeDirection = self.desiredDirection
        elif self.desiredDirection == 'down' and self.snakeDirection != 'up':
            self.snakeDirection = self.desiredDirection


# Food class
class foodClass:

    def __init__(self):
        self.foodSize = 20
        self.foodSpawn = True
        self.foodPosition = [random.randrange(1, (window_x//20)) * 20,
                  random.randrange(1, (window_y//20)) * 20]

    def addFood(self):
        pygame.draw.rect(game_window, magenta, pygame.Rect(
            self.foodPosition[0], self.foodPosition[1], self.foodSize, self.foodSize))

# Create snake instance
Snake = snakeClass()
Food = foodClass()

# Game over
def game_over():
    time.sleep(2)
    pygame.quit()
    quit()

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('Dora explora el juego de serpiente')
game_window = pygame.display.set_mode((window_x, window_y))

# Display window
pygame.display.flip()

# Play Dora song
mixer.init()
mixer.music.load("song.mp3")
mixer.music.set_volume(0.2)
mixer.music.play()

# Initial score
score = 0

# Loop - play the game
while True:

    # Changing direction
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                Snake.desiredDirection = 'up'
            if event.key == pygame.K_DOWN:
                Snake.desiredDirection = 'down'
            if event.key == pygame.K_LEFT:
                Snake.desiredDirection = 'left'
            if event.key == pygame.K_RIGHT:
                Snake.desiredDirection = 'right'

    Snake.changeDirection()

    # Draw window
    game_window.fill(lavender)

    # Draw snake
    for snakePart in Snake.snakeStartingBodyPositions:
        pygame.draw.rect(game_window, white, pygame.Rect(
            snakePart[0], snakePart[1], Snake.snakePartSize, Snake.snakePartSize))

    # Add food
    Food.addFood()

    # Refresh game screen
    pygame.display.update()

    # Move snake
    Snake.moveSnake()
    time.sleep(0.1)

    # Game over - touching the edge of the screen
    if snakePart[0] >= window_x or snakePart[0] < 0 or snakePart[1] >= window_y or snakePart[1] < 0:
        game_over()
