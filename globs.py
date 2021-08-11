import pygame
from pygame.locals import *
import os
import sys

playercash = 150
playerhealth = 200
transparentOverlay = pygame.image.load(os.path.join("mapideas", "dgBackground.png"))
screen = pygame.display.set_mode((900,580), pygame.SCALED, pygame.RESIZABLE)
clock=pygame.time.Clock()

bg = pygame.image.load(os.path.join("mapideas", "map2.png"))
bg = pygame.transform.scale(bg, (900, 580))

icesprite = pygame.image.load(os.path.join("towers", "ice.png")).convert_alpha()
firesprite = pygame.image.load(os.path.join("towers", "fire.png")).convert_alpha()
electricsprite = pygame.image.load(os.path.join("towers", "electric.png")).convert_alpha()

iceCost = 150
elecCost = 150
fireCost = 150

slimef1 = pygame.transform.scale2x(pygame.image.load(os.path.join("characters", "enemyslime","sprite_0.png")).convert_alpha())
slimef2 = pygame.transform.scale2x(pygame.image.load(os.path.join("characters", "enemyslime","sprite_1.png")).convert_alpha())
slimetest = pygame.transform.scale2x(pygame.image.load(os.path.join("characters", "enemyslime","sprite_1.png")).convert_alpha())

crabf1 = pygame.transform.scale2x(pygame.image.load(os.path.join("characters", "Crab","Crab0.png")).convert_alpha())
crabf2 = pygame.transform.scale2x(pygame.image.load(os.path.join("characters", "Crab","Crab1.png")).convert_alpha())
crabf3 = pygame.transform.scale2x(pygame.image.load(os.path.join("characters", "Crab","Crab2.png")).convert_alpha())
crabf4 = pygame.transform.scale2x(pygame.image.load(os.path.join("characters", "Crab","Crab3.png")).convert_alpha())

pythonf1 = pygame.transform.scale2x(pygame.image.load(os.path.join("characters", "Snake","snake0.png")).convert_alpha())
pythonf2 = pygame.transform.scale2x(pygame.image.load(os.path.join("characters", "Snake","snake1.png")).convert_alpha())
pythonf3 = pygame.transform.scale2x(pygame.image.load(os.path.join("characters", "Snake","snake2.png")).convert_alpha())
pythonf4 = pygame.transform.scale2x(pygame.image.load(os.path.join("characters", "Snake","snake3.png")).convert_alpha())
pythonf5 = pygame.transform.scale2x(pygame.image.load(os.path.join("characters", "Snake","snake4.png")).convert_alpha())
pythonf6 = pygame.transform.scale2x(pygame.image.load(os.path.join("characters", "Snake","snake5.png")).convert_alpha())
pythonf7 = pygame.transform.scale2x(pygame.image.load(os.path.join("characters", "Snake","snake6.png")).convert_alpha())


cold = pygame.image.load(os.path.join("towers","Snowflake.png"))
coin = pygame.image.load(os.path.join("mapideas","coin.png"))
heart = pygame.image.load(os.path.join("mapideas","heart.png"))




sframeprogression = ([slimef1]*10)+([slimef2]*10)
cframeprogression = ([crabf1]*5)+([crabf2]*5)+([crabf3]*5)+([crabf4]*5)
pframeprogression = ([pythonf1]*5)+([pythonf2]*5)+([pythonf3]*5)+([pythonf4]*5) + ([pythonf5]*5)+([pythonf6]*5)+([pythonf7]*5)

