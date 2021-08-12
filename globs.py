import pygame
from pygame.locals import *
import os
import sys
import itertools

debounce = itertools.cycle(range(10))

clicked = False
player_cash = 450
player_health = 200
TRANSPARENT_OVERLAY = pygame.image.load(os.path.join("mapideas", "dgBackground.png"))
SCREEN = pygame.display.set_mode((900, 580), pygame.SCALED, pygame.RESIZABLE)
CLOCK = pygame.time.Clock()

BACKGROUND = pygame.image.load(os.path.join("mapideas", "map2.png"))
BACKGROUND = pygame.transform.scale(BACKGROUND, (900, 580))

ICE_SPRITE = pygame.image.load(os.path.join("towers", "ice.png")).convert_alpha()
FIRE_SPRITE = pygame.image.load(os.path.join("towers", "fire.png")).convert_alpha()
ELECTRIC_SPRITE = pygame.image.load(
    os.path.join("towers", "electric.png")
).convert_alpha()

ICE_COST = 175
ELECTRIC_COST = 125
FIRE_COST = 150

SLIME_FRAME_1 = pygame.transform.scale2x(
    pygame.image.load(
        os.path.join("characters", "enemyslime", "sprite_0.png")
    ).convert_alpha()
)
SLIME_FRAME_2 = pygame.transform.scale2x(
    pygame.image.load(
        os.path.join("characters", "enemyslime", "sprite_1.png")
    ).convert_alpha()
)


CRAB_FRAME_1 = pygame.transform.scale2x(
    pygame.image.load(os.path.join("characters", "Crab", "Crab0.png")).convert_alpha()
)
CRAB_FRAME_2 = pygame.transform.scale2x(
    pygame.image.load(os.path.join("characters", "Crab", "Crab1.png")).convert_alpha()
)
CRAB_FRAME_3 = pygame.transform.scale2x(
    pygame.image.load(os.path.join("characters", "Crab", "Crab2.png")).convert_alpha()
)
CRAB_FRAME_4 = pygame.transform.scale2x(
    pygame.image.load(os.path.join("characters", "Crab", "Crab3.png")).convert_alpha()
)

PYTHON_FRAME_1 = pygame.transform.scale2x(
    pygame.image.load(os.path.join("characters", "Snake", "snake0.png")).convert_alpha()
)
PYTHON_FRAME_2 = pygame.transform.scale2x(
    pygame.image.load(os.path.join("characters", "Snake", "snake1.png")).convert_alpha()
)
PYTHON_FRAME_3 = pygame.transform.scale2x(
    pygame.image.load(os.path.join("characters", "Snake", "snake2.png")).convert_alpha()
)
PYTHON_FRAME_4 = pygame.transform.scale2x(
    pygame.image.load(os.path.join("characters", "Snake", "snake3.png")).convert_alpha()
)
PYTHON_FRAME_5 = pygame.transform.scale2x(
    pygame.image.load(os.path.join("characters", "Snake", "snake4.png")).convert_alpha()
)
PYTHON_FRAME_6 = pygame.transform.scale2x(
    pygame.image.load(os.path.join("characters", "Snake", "snake5.png")).convert_alpha()
)
PYTHON_FRAME_7 = pygame.transform.scale2x(
    pygame.image.load(os.path.join("characters", "Snake", "snake6.png")).convert_alpha()
)


cold = pygame.image.load(os.path.join("towers", "Snowflake.png"))
coin = pygame.image.load(os.path.join("mapideas", "coin.png"))
heart = pygame.image.load(os.path.join("mapideas", "heart.png"))


SLIME_FRAMES = ([SLIME_FRAME_1] * 10) + ([SLIME_FRAME_2] * 10)
CRAB_FRAMES = ([CRAB_FRAME_1] * 5) + ([CRAB_FRAME_2] * 5) + ([CRAB_FRAME_3] * 5) + ([CRAB_FRAME_4] * 5)
PYTHON_FRAMES = (
    ([PYTHON_FRAME_1] * 5)
    + ([PYTHON_FRAME_2] * 5)
    + ([PYTHON_FRAME_3] * 5)
    + ([PYTHON_FRAME_4] * 5)
    + ([PYTHON_FRAME_5] * 5)
    + ([PYTHON_FRAME_6] * 5)
    + ([PYTHON_FRAME_7] * 5)
)
