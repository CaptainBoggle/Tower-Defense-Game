import pygame
from pygame.locals import *
import os
import sys

playerhealth = 100
playercash = 150
transparentOverlay = pygame.image.load(os.path.join("mapideas", "dgBackground.png"))
screen = pygame.display.set_mode((900,580), pygame.SCALED, pygame.RESIZABLE)
clock=pygame.time.Clock()

bg = pygame.image.load(os.path.join("mapideas", "map.png"))

icesprite = pygame.image.load(os.path.join("towers", "ice.png")).convert_alpha()
firesprite = pygame.image.load(os.path.join("towers", "fire.png")).convert_alpha()
electricsprite = pygame.image.load(os.path.join("towers", "electric.png")).convert_alpha()



slimef1 = pygame.transform.scale2x(pygame.image.load(os.path.join("characters", "enemyslime","sprite_0.png")).convert_alpha())
slimef2 = pygame.transform.scale2x(pygame.image.load(os.path.join("characters", "enemyslime","sprite_1.png")).convert_alpha())
slimetest = pygame.transform.scale2x(pygame.image.load(os.path.join("characters", "enemyslime","sprite_1.png")).convert_alpha())

frameprogression = ([slimef1]*10)+([slimef2]*10)