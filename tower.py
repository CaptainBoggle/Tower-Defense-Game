import pygame
from pygame.locals import *
import os
import sys
import globs



class Tower(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect(center=pos)
        self.range=5

    def Targeting(enemies):
        for e in enemies:
            
