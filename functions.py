from conditions import *
import math
def deltaTimeFunction():
    deltaTime = 0
    while deltaTime < 1000/tickRate:
        deltaTime += clock.tick()

def drawBackground():
    screen.blit(backgroundImage, (0, 0))

def drawBullet(bulletPos):
    if bulletPos[1] >= 50:
        screen.blit(bullet, (bulletPos[0] + 26, bulletPos[1] + 16))
        bulletPos[1] += bulletChange
        return True
    elif bulletPos[1] < 50:
        return False

def isCollision(bulletPos, enemy):
    distance = math.sqrt(math.pow(bulletPos[0] - enemy.posX, 2.0) + math.pow(bulletPos[1] - enemy.posY, 2.0))
    if distance < 27:
        return True
    else:
        return False

def showScore(x, y, score_value):
    score = font.render("Score : " + str(score_value), True,  (0, 0, 0))
    screen.blit(score, (x, y))

def gameOver(score_value):
    font = pygame.font.Font('freesansbold.ttf', 48)
    over_text = font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (380, 300))

class Player:
    def __init__(self, xPos, yPos, posChangeX, Image):
        self.posX = xPos
        self.posY = yPos
        self.posChangeX = posChangeX
        self.Image = Image

    def drawPlayer(self):
        screen.blit(self.Image, (self.posX, self.posY))

    def processMovement(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.posChangeX = -6
            elif event.key == pygame.K_RIGHT:
                self.posChangeX = 6

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.posChangeX *= 0
            elif event.key == pygame.K_RIGHT:
                self.posChangeX *= 0

    def move(self):
        self.posX += self.posChangeX

class Enemy(Player):

    speedIncrease = 1
    def __init__(self, xPos, yPos, posChangeX, Image):
        super().__init__(xPos, yPos, posChangeX, Image)
    def processEnemyMovement(self):
        if self.posX >= 956:
            self.posChangeX *= -1
            self.posY += 50
        elif self.posX <= -2:
            self.posChangeX *= -1
            self.posY += 50
        if self.posY >= 700:
            self.posY = random.randint(50, 400)

    def move(self):
        self.posX += Enemy.speedIncrease * self.posChangeX

    @classmethod
    def increaseSpeed(cls):
        cls.speedIncrease += 0.03