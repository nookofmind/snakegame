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
scoreBarSize = 20

gameArea_y = window_y - scoreBarSize
gameArea_x = window_x

# Snake class
class snakeClass:
    def __init__(self):
        self.snakeBodyPositions = [[40, 100], [20, 100], [0, 100]]
        self.snakeDirection = 'right'
        self.desiredDirection = 'none'
        self.snakePartSize = 20
        self.snakeSpeed = 10
        self.nextSnakePartPosition = [0, 0]
        self.previousSnakePartPosition = [0, 0]

    # Move snake
    def moveHead(self):
        if self.snakeDirection == 'right':
            # x increases, y stays the same
            self.nextSnakePartPosition[0] = self.snakeBodyPositions[0][0] + self.snakePartSize
            self.nextSnakePartPosition[1] = self.snakeBodyPositions[0][1]
        elif self.snakeDirection == 'left':
            # x decreases, y stays the same
            self.nextSnakePartPosition[0] = self.snakeBodyPositions[0][0] - self.snakePartSize
            self.nextSnakePartPosition[1] = self.snakeBodyPositions[0][1]
        elif self.snakeDirection == 'up':
            # x stays the same, y decreases
            self.nextSnakePartPosition[0] = self.snakeBodyPositions[0][0]
            self.nextSnakePartPosition[1] = self.snakeBodyPositions[0][1] - self.snakePartSize
        elif self.snakeDirection == 'down':
            # x stays the same, y increases
            self.nextSnakePartPosition[0] = self.snakeBodyPositions[0][0]
            self.nextSnakePartPosition[1] = self.snakeBodyPositions[0][1] + self.snakePartSize

    def moveBody(self):
        for index, snakeFragment in enumerate(self.snakeBodyPositions):
            self.previousSnakePartPosition = snakeFragment
            self.snakeBodyPositions[index] = self.nextSnakePartPosition
            self.nextSnakePartPosition = self.previousSnakePartPosition

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

    # Growing mechanism
    def eatFood(self, foodPosition_x, foodPosition_y):
        if self.snakeBodyPositions[0] == [foodPosition_x, foodPosition_y]:
            return True
        else:
            return False

    # Tail collision


# Food class
class foodClass:

    def __init__(self):
        self.foodSize = 20
        self.foodPosition = [random.randrange(1, (gameArea_x // 20)) * 20,
                             random.randrange(1, (gameArea_y // 20)) * 20]

    def addFood(self, _gameWindow, color):
        pygame.draw.rect(_gameWindow, color, pygame.Rect(
            self.foodPosition[0], self.foodPosition[1], self.foodSize, self.foodSize))

    def generateRandomFoodPosition(self):
        self.foodPosition = [random.randrange(1, (gameArea_x // 20)) * 20,
                             random.randrange(1, (gameArea_y // 20)) * 20]

    def getLastFoodPosition(self):
        return self.foodPosition

# Score
def showScore(color, font, size):
    scoreFont = pygame.font.SysFont(font, size)
    scoreSurface = scoreFont.render('Score : ' + str(score), True, color)
    scoreRect = scoreSurface.get_rect()
    pygame.draw.rect(gameWindow, white, pygame.Rect(0, 0, window_x, scoreBarSize))
    gameWindow.blit(scoreSurface, scoreRect)


# Game over
def gameOver():
    messageFont = pygame.font.SysFont('roboto', 35)
    gameOverSurface = messageFont.render('Game over. Your score is : ' + str(score), True, white)
    gameOverRect = gameOverSurface.get_rect()
    gameOverRect.midtop = (window_x / 2, window_y / 4)
    gameWindow.blit(gameOverSurface, gameOverRect)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    quit()

# Create snake instance
Snake = snakeClass()
Food = foodClass()

# Initial score
score = 0

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('Dora explora el juego de serpiente')
gameWindow = pygame.display.set_mode((window_x, window_y))

# Display window
pygame.display.flip()

# Play Dora song
mixer.init()
mixer.music.load("song.mp3")
mixer.music.set_volume(0.2)
mixer.music.play(loops=-1, start=0.0, fade_ms=0)

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
    gameWindow.fill(lavender)

    # Add food
    Food.addFood(gameWindow, salmon)

    # Draw snake
    for snakePart in Snake.snakeBodyPositions:
        pygame.draw.rect(gameWindow, magenta, pygame.Rect(
            snakePart[0], snakePart[1], Snake.snakePartSize, Snake.snakePartSize))

    # Display score
    showScore(lavender, 'roboto', 30)

    # Refresh game screen
    pygame.display.update()

    time.sleep(0.1)

    currentFoodPositionX = Food.getLastFoodPosition()[0]
    currentFoodPositionY = Food.getLastFoodPosition()[1]

    # Snake growing mechanism
    foundFood = Snake.eatFood(currentFoodPositionX, currentFoodPositionY)

    # Move snake
    Snake.moveHead()
    Snake.moveBody()

    if foundFood:
        Snake.snakeBodyPositions.append([currentFoodPositionX, currentFoodPositionY])
        Food.generateRandomFoodPosition()
        score = score + 10
        foundFood = False

    # Game over - touching the edge of the screen
    if Snake.snakeBodyPositions[0][0] >= gameArea_x or Snake.snakeBodyPositions[0][0] < 0 or Snake.snakeBodyPositions[0][
        1] >= (gameArea_y + scoreBarSize) or Snake.snakeBodyPositions[0][1] < (0 + scoreBarSize):
        gameOver()

    # Game over - touching tail

