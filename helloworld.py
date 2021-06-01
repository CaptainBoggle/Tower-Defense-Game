import pygame
from pygame.locals import *
import os
import sys

pygame.init()

screen = pygame.display.set_mode((900,580))

bg1 = pygame.image.load(os.path.join("mapideas", "hedge.png"))
bg2 = pygame.image.load(os.path.join("mapideas", "meadow.png"))
bg3 = pygame.image.load(os.path.join("mapideas", "rake.png"))
bg = bg1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            if bg == bg1:
                bg = bg2
            elif bg == bg2:
                bg = bg3
            else:
                bg = bg1

    screen.fill((255,255,255))
    screen.blit(bg, (0,0))

    pygame.display.flip()