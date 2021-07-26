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
        self.level = 0
        self.image = electricsprite
        self.rect = self.image.get_rect(center=pos)
        self.range=100
        self.x,self.y = pos
        self.damage = 5
        self.cooldowntime = 15
        self.cooldown = self.cooldowntime
        self.lines = []
        

    def inRange(self,enemy):
        if math.sqrt((self.x-enemy.x)**2 + (self.y-enemy.y)**2) <= self.range:
            return True
        return False
    
    def lineRendering(self,line):
        if pygame.time.get_ticks()-line[1] < (self.cooldowntime/60*1000):
            return True
        return False

    def getTarget(self,enemies):
        return next(filter(self.inRange, enemies[::-1]),None)

    def updateLines(self):
        self.lines = [i for i in self.lines if self.lineRendering(i)]
        for line in self.lines:
            pygame.draw.line(screen,(255,215,0),(self.x,self.y),line[0],3)

    def update(self,e):
        screen.blit(self.image,(self.x-16,self.y-11))
        if self.cooldown>0:
            self.cooldown -= 1
        if (self.cooldown == 0 and self.getTarget(e)):
            target = self.getTarget(e)
            self.cooldown = self.cooldowntime
            target.takedamage(self.damage)
            stime = pygame.time.get_ticks()
            self.lines.append([(target.x,target.y),stime])
        self.updateLines()

    def levelup(self):
        self.level += 1
        self.damage += self.level
        self.range += self.level*10

slow = {
    6:3,3:2,2:1.5,1.5:0.5
}

class IceTower(pygame.sprite.Sprite):
    def __init__(self,pos):
        pygame.sprite.Sprite.__init__(self)
        self.level = 0
        self.image = icesprite
        self.rect = self.image.get_rect(center=pos)
        self.range=100
        self.x,self.y = pos

    def inRange(self,enemy):
        if math.sqrt((self.x-enemy.x)**2 + (self.y-enemy.y)**2) <= self.range:
            return True
        return False
    
    def getTargets(self,enemies):
        return next(filter(self.inRange, enemies[::-1]),None)
            
    def update(self,e):
        screen.blit(self.image,(self.x-16,self.y-11))
        for enemy in e:
            if self.inRange(enemy):
                pygame.draw.line(screen,(0,206,209),(self.x,self.y),(enemy.x,enemy.y),3)
                enemy.speed = slow[enemy.defspeed]
            else:
                enemy.speed = enemy.defspeed

    def levelup(self):
        self.level += 1
        self.range += self.level*20






