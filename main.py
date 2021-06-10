import pygame
from pygame.locals import *
import os
import sys
from tower import Tower
from enemy import AI
import player

pygame.init()

screen = pygame.display.set_mode((900,580))
clock=pygame.time.Clock()

bg1 = pygame.image.load(os.path.join("mapideas", "meadow.png"))
bg2 = pygame.image.load(os.path.join("mapideas", "rake.png"))

ts1 = pygame.image.load(os.path.join("towers", "drafts","t1.png")).convert_alpha()
ts2 = pygame.image.load(os.path.join("towers", "drafts","t1o.png")).convert_alpha()
ts3 = pygame.image.load(os.path.join("towers", "drafts","t2.png")).convert_alpha()
ts4 = pygame.image.load(os.path.join("towers", "drafts","t2o.png")).convert_alpha()


bg = bg1

enemies = [AI(0,240,6),AI(0,240,1.5),AI(0,240,2),AI(0,240,3)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            if bg == bg1:
                bg = bg2
            else: bg = bg1

    pygame.display.set_caption(str(pygame.mouse.get_pos()))

            

    screen.fill((255,255,255))
    screen.blit(bg, (0,0))
    enemies[:] = [enemy for enemy in enemies if enemy.alive]
    for e in enemies:
    	e.update()

    clock.tick(60)
    pygame.display.flip()