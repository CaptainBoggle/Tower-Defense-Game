import pygame
from pygame.locals import *
import os
import sys
from globs import *
import math
import enemy




class ElectricTower(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = electricsprite
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
    
    def lineRendering(self,line):
        if pygame.time.get_ticks()-line[1] < 700:
            return True
        return False

    def getTarget(self,enemies):
        return next(filter(self.inRange, enemies[::-1]),None)

    def updateLines(self):
        self.lines = [i for i in self.lines if self.lineRendering(i)]
        print(self.lines)
        for line in self.lines:
            pygame.draw.line(screen,(204,204,102),(self.x,self.y),line[0],2)

    def update(self,e):
        if self.cooldown>0:
            self.cooldown -= 1
        if (self.cooldown == 0 and self.getTarget(e)):
            target = self.getTarget(e)
            self.cooldown = self.cooldowntime
            target.takedamage(self.damage)
            stime = pygame.time.get_ticks()
            self.lines.append([(target.x,target.y),stime])
        self.updateLines()






