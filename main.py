import pygame
import random


pygame.init()

clock = pygame.time.Clock()
FPS = 120

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

xPos = 30
yPos = 30
rectWidth=25
rectHeight=25
player = pygame.Rect((xPos, yPos, rectWidth, rectHeight))

enemy1 = pygame.Rect(random.randint(0, 500), random.randint(0, 300), 25, 25)
enemy2 = pygame.Rect(random.randint(0, 500), random.randint(0, 300), 25, 25)
enemy3 = pygame.Rect(random.randint(0, 500), random.randint(0, 300), 25, 25)
enemy4 = pygame.Rect(random.randint(0, 500), random.randint(0, 300), 25, 25)

run = True
xDir = 1
yDir = 0

foodType = ["x","y","z"]
foodDuration = 4

bgColor = (0,0,0)

while run:
    clock.tick(FPS)
    screen.fill((bgColor))
    pygame.draw.rect(screen, (100, 100, 100), player)
    pygame.draw.rect(screen, (100,100,100), enemy1)
    pygame.draw.rect(screen, (100,100,100), enemy2)
    pygame.draw.rect(screen, (100,100,100), enemy3)
    pygame.draw.rect(screen, (100,100,100), enemy4)

    if player.colliderect(enemy1) or player.colliderect(enemy2) or player.colliderect(enemy3) or player.colliderect(enemy4):
        bgColor = (139,0,0)
    else:
        bgColor = (0,0,0)

        
    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT] == True and xDir!=1:
        xDir=-1
        yDir=0
    elif key[pygame.K_RIGHT] == True and xDir!=-1:
        xDir=1
        yDir=0
    elif key[pygame.K_UP] == True and yDir!=1:
        xDir=-0
        yDir=-1
    elif key[pygame.K_DOWN] == True and yDir!=-1:
        xDir=0
        yDir=1

    player.move_ip(xDir,yDir)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()