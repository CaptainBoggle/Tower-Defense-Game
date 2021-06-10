import pygame
from pygame.locals import *
import os
import sys
import tower
import enemy
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

enemies = [enemy.AI(0,240,6),enemy.AI(0,240,1.5),enemy.AI(0,240,2),enemy.AI(0,240,3)]

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
        pygame.draw.circle(screen,((255,0,0)),(e.x,e.y),8)

    clock.tick(60)
    pygame.display.flip()