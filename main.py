import pygame
from pygame.locals import *
import os
import sys
import tower
import enemy
import player
from globs import *
import random

pygame.init()




slimetest.fill("RED")


enemies = [enemy.AI(0,240,6),enemy.AI(0,240,1.5),enemy.AI(0,240,2),enemy.AI(0,240,3)]

test = tower.ElectricTower((350,288))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            enemies.append(enemy.AI(0,240,random.choice([6,1.5,2,3])))

    pygame.display.set_caption(str(pygame.mouse.get_pos()))
            

    screen.fill((255,255,255))
    screen.blit(bg, (0,0))
    enemies[:] = [enemy for enemy in enemies if enemy.alive]
    
    enemies.sort(key=lambda e: len(e.path), reverse=True)
    
    for e in enemies:
        e.update()
        screen.blit(pygame.transform.rotate(frameprogression[e.frame],e.angle),(e.x-32,e.y-32))
    
    target = test.getTarget(enemies)

    if target: screen.blit(pygame.transform.rotate(slimetest,target.angle),(target.x-32,target.y-32))
    pygame.draw.circle(screen, (0,0,255), (test.x,test.y), 100, 1)
    clock.tick(60)
    pygame.display.flip()