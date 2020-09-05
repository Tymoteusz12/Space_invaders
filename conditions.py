from variables import *

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption(caption)
pygame.display.set_icon(icon)
font = pygame.font.Font('freesansbold.ttf', 26)
mixer.music.load('wav/background.wav')
mixer.music.play(-1)
