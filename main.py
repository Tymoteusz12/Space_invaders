from conditions import *
import functions

mainPlayer = functions.Player(playerX, playerY, playerChangeX, playerImage)
mainEnemy = []
giveX = []
repeat = True
exitVar = False
lastX = 0
lastFrame = 0
deltaTime = 0
for i in range(6):
    if i == 0:
        enemy = functions.Enemy(enemyX, enemyY, enemyChangeX, enemyImage)
    else:
        enemyX += 50
        enemyY = random.randint(50, 400)
        enemy = functions.Enemy(enemyX, enemyY, enemyChangeX, enemyImage)
    mainEnemy.append(enemy)

while running:
    screen.fill((0, 0, 0))
    functions.drawBackground()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bulletSound = mixer.Sound('wav/laser.wav')
            bulletSound.play()
            if not shot:
                bulletPos = [[mainPlayer.posX, mainPlayer.posY]]
                shot = True
                multipleShots = False
            if shot and not multipleShots:
                bulletPos.append([mainPlayer.posX, mainPlayer.posY])

        mainPlayer.processMovement(event)

    for enemy in mainEnemy:
        enemy.processEnemyMovement()

    if shot is True:
        for bullets in bulletPos:
            for enemy in mainEnemy:
                collision = functions.isCollision(bullets, enemy)
                if collision:
                    explosionSound = mixer.Sound('wav/explosion.wav')
                    explosionSound.play()
                    bulletPos.remove(bullets)
                    score_value += 1
                    enemy.increaseSpeed()
                    enemy.posX = random.randint(10, 900)
                    enemy.posY = random.randint(50, 400)
                if not collision:
                    shot = functions.drawBullet(bullets)

    mainPlayer.move()
    for enemy in mainEnemy:
        enemy.move()

    mainPlayer.drawPlayer()
    for enemy in mainEnemy:
        enemy.drawPlayer()

    functions.showScore(textX, textY, score_value)

    for enemy in mainEnemy:
        if enemy.posY + 32 >= mainPlayer.posY and mainPlayer.posX - 32 <= enemy.posX <= mainPlayer.posX + 32:
            while not exitVar:
                functions.gameOver(score_value)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exitVar = True
                        running = False
    pygame.display.update()
