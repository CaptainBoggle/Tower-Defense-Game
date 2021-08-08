import pygame
from pygame.locals import *
import os
import sys
import globs
import random
import itertools

def alternator():
    iterator = 0
    while True:
        value = 1 if iterator % 2 == 0 else 0
        iterator += 1
        yield value


class AI(object):

    def __init__(self,x,y,type):
        self.x=x
        self.y=y
        #self.speed = speed
        #self.defspeed = speed
        self.path=[(444,246,270),(444,114,0),(294,114,90),(294,462,180),(150,462,90),(150,342,0),(570,342,270),(570,204,0),(672,204,270),(672,414,180),(402,414,90),(402,570,180)]
        self.alive = True
        #self.hp = health # implement later
        #self.worth = worth
        self.frame = 0
        self.angle = 270
        self.slow = 0
        self.type = type
        self.ftotal = 19
        if self.type == "p":
            self.worth = 15
            self.ftotal = 20
            self.speed = 6
            self.health = 100
        elif self.type == "s":
            self.worth = 10
            self.speed = 3
            self.health = 125
        else:
            self.worth = 20
            self.speed = 1.5
            self.health = 300
    def remove(self,reason):
    	self.alive = False
    	if reason == "getthrough":
    		globs.playerhealth -= self.hp
    	else:
    		globs.playercash += self.worth # give player some cash money
    	
    def update(self):
        if self.slow != 0:
            return
        
        if len(self.path) == 0:
           self.remove("getthrough")
           return
        self.angle=(self.path[0])[2]
        if self.x<(self.path[0])[0]:
            self.x+=self.speed
        if self.x>(self.path[0])[0]:
            self.x-=self.speed
        if self.y<(self.path[0])[1]:
            self.y+=self.speed
        if self.y>(self.path[0])[1]:
            self.y-=self.speed
        z=(self.x-(self.path[0])[0],self.y-(self.path[0])[1])
        if (z[0]/-self.speed,z[1]/-self.speed)==(0,0):
            self.path=self.path[1:]
        if self.frame < self.ftotal:
            self.frame+=1
        else:
            self.frame=0
        #print(self.x,self.y)
    
    def takedamage(self,amount):
    	self.hp -= amount
    	if self.hp <= 0:
    		self.remove("dead")

