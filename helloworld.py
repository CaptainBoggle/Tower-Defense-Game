import pygame
from pygame.locals import *
import os
import sys

pygame.init()

screen = pygame.display.set_mode((900,580))

bg1 = pygame.image.load(os.path.join("mapideas", "hedge.png"))
bg2 = pygame.image.load(os.path.join("mapideas", "meadow.png"))
bg3 = pygame.image.load(os.path.join("mapideas", "rake.png"))

ts1 = pygame.image.load(os.path.join("towers", "drafts","t1.png")).convert_alpha()
ts2 = pygame.image.load(os.path.join("towers", "drafts","t1o.png")).convert_alpha()
ts3 = pygame.image.load(os.path.join("towers", "drafts","t2.png")).convert_alpha()
ts4 = pygame.image.load(os.path.join("towers", "drafts","t2o.png")).convert_alpha()
bg = bg1

class Tower(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect(center=pos)


        
dragging = False
while True:
    mx, my = pygame.mouse.get_pos()
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