import pygame
from pygame import mixer
import random
#Icons made by https://www.flaticon.com/authors/freepik, flaticon.com
#Background vector created by pikisuperstar - www.freepik.com
pygame.init()

caption = "Space invaders"
icon = pygame.image.load('img/spaceship.png')
playerImage = pygame.image.load('img/player.png')
enemyImage = pygame.image.load("img/invader.png")
backgroundImage = pygame.image.load("img/background.jpg")
bullet = pygame.image.load("img/bullet.png")
clock = pygame.time.Clock()
tickRate = 60

screenWidth = 1024
screenHeight = 800

bulletX = 0
bulletY = 0
bulletChange = -1

playerX = 482
playerY = 650
playerChangeX = 0

enemyX = random.randint(0, 600) - 25
enemyY = random.randint(50, 300)
enemyChangeX = 6

score_value = 0
textX = 10
textY = 10


running = True
shot = False
multipleShot = False

