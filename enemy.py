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
    def __init__(self, type):
        self.x = 0
        self.y = 240
        # self.speed = speed
        # self.defspeed = speed
        self.path = [
            (444, 246, 270),
            (444, 114, 0),
            (294, 114, 90),
            (294, 462, 180),
            (150, 462, 90),
            (150, 342, 0),
            (570, 342, 270),
            (570, 204, 0),
            (672, 204, 270),
            (672, 414, 180),
            (402, 414, 90),
            (402, 570, 180),
        ]
        self.alive = True
        # self.hp = health # implement later
        # self.worth = worth
        self.frame = 0
        self.angle = 270
        self.slow = 0
        self.type = type
        self.ftotal = 19
        if self.type == "p":
            self.worth = 2
            self.ftotal = 34
            self.speed = 6
            self.hp = 200
        elif self.type == "s":
            self.worth = 1
            self.speed = 3
            self.hp = 500
        else:
            self.worth = 4
            self.speed = 1.5
            self.hp = 1000

    def remove(self, reason):
        self.alive = False
        if reason == "getthrough":
            globs.playerhealth -= round(self.hp/10)
        else:
            globs.playercash += self.worth  # give player some cash money

    def update(self):
        if self.slow != 0:
            return

        if len(self.path) == 0:
            self.remove("getthrough")
            return
        self.angle = (self.path[0])[2]
        if self.x < (self.path[0])[0]:
            self.x += self.speed
        if self.x > (self.path[0])[0]:
            self.x -= self.speed
        if self.y < (self.path[0])[1]:
            self.y += self.speed
        if self.y > (self.path[0])[1]:
            self.y -= self.speed
        z = (self.x - (self.path[0])[0], self.y - (self.path[0])[1])
        if (z[0] / -self.speed, z[1] / -self.speed) == (0, 0):
            self.path = self.path[1:]
        if self.frame < self.ftotal:
            self.frame += 1
        else:
            self.frame = 0
        # print(self.x,self.y)

    def takedamage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.remove("dead")
