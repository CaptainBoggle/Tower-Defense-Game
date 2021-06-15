import pygame
from pygame.locals import *
import os
import sys
import globs

class AI(object):
    def __init__(self,x,y,speed):
        self.x=x
        self.y=y
        self.speed = speed
        self.path=[(444,246),(444,114),(294,114),(294,462),(150,462),(150,342),(570,342),(570,204),(672,204),(672,414),(402,414),(402,570)]
        self.alive = True
        self.hp = 1 # implement later
        self.worth = 10
    
    def remove(self,reason):
    	self.alive = False
    	if reason == "getthrough":
    		globs.playerhealth -= self.hp
    	else:
    		globs.playercash += self.worth # give player some cash money
    	
    def update(self):
        if len(self.path) == 0:
           self.remove("getthrough")
           return
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
    def takedamage(self,amount):
    	self.hp -= amount
    	if self.hp <= 0:
    		self.remove("dead")

