import pygame
import sys, os

pygame.init()

size = width, height = 800, 800
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
black = (0,0,0)

snakeImg = pygame.image.load("snaketile.png")
snaketilerect = snakeImg.get_rect(center=(width / 20, height / 2))


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    snaketilerect = snaketilerect.move(1 , 0)
    screen.fill(black)
    screen.blit(snakeImg, snaketilerect)
    pygame.display.update()
    clock.tick(60)