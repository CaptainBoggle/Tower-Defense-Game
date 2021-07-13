import pygame
from pygame.locals import *
import os
import sys
import tower
import enemy
import player
import globs
import random

pygame.init()

screen = pygame.display.set_mode((900,580), pygame.SCALED, pygame.RESIZABLE)
clock=pygame.time.Clock()

bg = pygame.image.load(os.path.join("mapideas", "meadow.png"))


firesprite = pygame.image.load(os.path.join("towers", "fire.png")).convert_alpha()
electricsprite = pygame.image.load(os.path.join("towers", "electric.png")).convert_alpha()



slimef1 = pygame.transform.scale2x(pygame.image.load(os.path.join("characters", "enemyslime","sprite_0.png")).convert_alpha())
slimef2 = pygame.transform.scale2x(pygame.image.load(os.path.join("characters", "enemyslime","sprite_1.png")).convert_alpha())
slimetest = pygame.transform.scale2x(pygame.image.load(os.path.join("characters", "enemyslime","sprite_1.png")).convert_alpha())
slimetest.fill("RED")


frameprogression = ([slimef1]*10)+([slimef2]*10)

enemies = [enemy.AI(0,240,6),enemy.AI(0,240,1.5),enemy.AI(0,240,2),enemy.AI(0,240,3)]

test = tower.Tower(slimef1,(350,288))

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