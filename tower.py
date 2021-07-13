import pygame
from pygame.locals import *
import os
import sys
import globs
import math



class ElectricTower(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = globs.electricsprite
        self.rect = self.image.get_rect(center=pos)
        self.range=100
        self.x,self.y = pos
    
    def inRange(self,enemy):
        if math.sqrt((self.x-enemy.x)**2 + (self.y-enemy.y)**2) <= self.range:
            return True
        return False
    
    def getTarget(self,enemies):
        return next(filter(self.inRange, enemies[::-1]),None)



