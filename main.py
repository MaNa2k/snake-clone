import pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 120

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

xPos = 30
yPos = 30
rectWidth=100
rectHeight=100
player = pygame.Rect((xPos, yPos, rectWidth, rectHeight))

run = True
currentDirection = 3
xDir = 1
yDir = 0

while run:
    clock.tick(FPS)

    player.move_ip(xDir,yDir)

    screen.fill((0,0,0))
    pygame.draw.rect(screen, (100, 100, 100), player)

    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT] == True:
        currentDirection = 2
        xDir=-1
        yDir=0
    elif key[pygame.K_RIGHT] == True:
        currentDirection = 3
        xDir=1
        yDir=0
    elif key[pygame.K_UP] == True:
        currentDirection = 0
        xDir=-0
        yDir=-1
    elif key[pygame.K_DOWN] == True:
        currentDirection = 1
        xDir=0
        yDir=1


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()