import pygame
from pygame.locals import *
import os
import sys
import globs
import random
import itertools


class AI(object):  # Class for all enemies
    def __init__(self, type):
        self.x = 0
        self.y = 240
        self.path = [  # Coordinates to turn at
            (444, 246, 270),
            (444, 114, 0),
            (300, 114, 90),
            (300, 462, 180),
            (168, 462, 90),
            (168, 342, 0),
            (558, 342, 270),
            (558, 204, 0),
            (672, 204, 270),
            (672, 414, 180),
            (402, 414, 90),
            (402, 570, 180),
        ]
        self.alive = True
        self.frame = 0
        self.angle = 270
        self.slow = 0
        self.type = type
        self.frames_total = 19
        if self.type == "p":
            self.worth = 2
            self.frames_total = 34
            self.speed = 6
            self.hp = 350
        elif self.type == "s":
            self.worth = 1
            self.speed = 3
            self.hp = 500
        else:
            self.worth = 5
            self.speed = 1.5
            self.hp = 2000

    def remove(
        self, reason
    ):  # Handle removing for either death or getting to the end of the path
        self.alive = False
        if reason == "getthrough":
            globs.player_health -= round(self.hp / 10)
        else:
            globs.player_cash += self.worth  # give player some cash money

    def update(self):  # Run every frame, moves and animates.
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
        if self.frame < self.frames_total:
            self.frame += 1
        else:
            self.frame = 0

    def take_damage(self, amount):  # Reduce health by amount
        self.hp -= amount
        if self.hp <= 0:
            self.remove("dead")
