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
        self.damage = 5
        self.cooldowntime = 30
        self.cooldown = self.cooldowntime
        self.lines = []

    def inRange(self,enemy):
        if math.sqrt((self.x-enemy.x)**2 + (self.y-enemy.y)**2) <= self.range:
            return True
        return False
    
    def getTarget(self,enemies):
        return next(filter(self.inRange, enemies[::-1]),None)

    def updateLines(self):
        for line in self.lines:
            

    def update(self,e):
        self.cooldown -= 1
        if self.cooldown == 0:
            target = self.getTarget(e)
            self.cooldown = self.cooldowntime







