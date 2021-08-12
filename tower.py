import pygame
from pygame.locals import *
import os
import sys
import globs
import math
import enemy
import itertools
import random


class ElectricTower(pygame.sprite.Sprite):
    def __init__(self, pos, hitbox):
        pygame.sprite.Sprite.__init__(self)
        self.level = 0
        self.image = globs.electricsprite
        self.rect = self.image.get_rect(center=pos)
        self.range = 100
        self.x, self.y = pos
        self.damage = 100
        self.cooldowntime = 30
        self.cooldown = self.cooldowntime
        self.lines = []
        self.hitbox = hitbox

    def inRange(self, enemy):
        if math.sqrt((self.x - enemy.x) ** 2 + (self.y - enemy.y) ** 2) <= self.range:
            return True
        return False

    def lineRendering(self, line):
        if pygame.time.get_ticks() - line[1] < (self.cooldowntime / 60 * 1000):
            return True
        return False

    def getTarget(self, enemies):
        return next(filter(self.inRange, enemies[::-1]), None)

    def updateLines(self):
        self.lines = [i for i in self.lines if self.lineRendering(i)]
        for line in self.lines:
            pygame.draw.line(globs.screen, (255, 215, 0), (self.x, self.y), line[0], 3)

    def update(self, e):
        globs.screen.blit(self.image, (self.x - 16, self.y - 11))
        pygame.draw.circle(globs.screen, (0, 0, 255), (self.x, self.y), self.range, 1)
        if self.cooldown > 0:
            self.cooldown -= 1
        if self.cooldown <= 0 and self.getTarget(e):
            target = self.getTarget(e)
            self.cooldown = self.cooldowntime
            target.takedamage(self.damage)
            stime = pygame.time.get_ticks()
            self.lines.append([(target.x, target.y), stime])
        self.updateLines()

    def levelup(self):
        globs.clicked = True
        globs.playercash -= 100
        self.level += 1
        self.cooldown -= 1
        self.range += 10
        self.damage += 50


class IceTower(pygame.sprite.Sprite):
    def __init__(self, pos, hitbox):
        pygame.sprite.Sprite.__init__(self)
        self.level = 0
        self.image = globs.icesprite
        self.rect = self.image.get_rect(center=pos)
        self.range = 80
        self.x, self.y = pos
        self.intensity = 0
        self.cycle = itertools.cycle(range(self.intensity + 2))
        self.hitbox = hitbox

    def inRange(self, enemy):
        if math.sqrt((self.x - enemy.x) ** 2 + (self.y - enemy.y) ** 2) <= self.range:
            return True
        return False

    def getTargets(self, enemies):
        return next(filter(self.inRange, enemies[::-1]), None)

    def update(self, e):
        globs.screen.blit(self.image, (self.x - 16, self.y - 11))
        pygame.draw.circle(globs.screen, (0, 0, 255), (self.x, self.y), self.range, 1)
        nextcycle = next(self.cycle)
        for enemy in e:
            if self.inRange(enemy):
                globs.screen.blit(globs.cold, (enemy.x - 16, enemy.y - 16))
                # pygame.draw.polygon(surface=screen, color=(0,206,209), points=[(enemy.x+5,enemy.y), (enemy.x,enemy.y+5), (enemy.x,enemy.y-5)])
                enemy.slow = nextcycle
            else:
                enemy.slow = 0

    def levelup(self):
        globs.clicked = True
        globs.playercash -= 100
        self.level += 1
        self.range += 5
        if self.level % 2 == 0:
            self.intensity += 1
            self.cycle = itertools.cycle(range(self.intensity + 2))


class FireTower(pygame.sprite.Sprite):
    def __init__(self, pos, hitbox):
        pygame.sprite.Sprite.__init__(self)
        self.level = 0
        self.image = globs.firesprite
        self.rect = self.image.get_rect(center=pos)
        self.range = 60
        self.x, self.y = pos
        self.targets = 4
        self.damage = 2
        self.hitbox = hitbox

    def inRange(self, enemy):
        if math.sqrt((self.x - enemy.x) ** 2 + (self.y - enemy.y) ** 2) <= self.range:
            return True
        return False

    def getTargets(self, enemies):
        return list(filter(self.inRange, enemies[::-1]))

    def update(self, e):
        targs = self.getTargets(e)
        globs.screen.blit(self.image, (self.x - 16, self.y - 11))
        pygame.draw.circle(globs.screen, (0, 0, 255), (self.x, self.y), self.range, 1)
        for enemy in targs[: min(self.targets, len(targs))]:
            if self.inRange(enemy):
                pygame.draw.line(
                    globs.screen, (215, 0, 64), (self.x, self.y), (enemy.x, enemy.y), 3
                )
                enemy.takedamage(self.damage)

    def levelup(self):
        globs.clicked = True
        globs.playercash -= 100
        self.level += 1
        self.range += 10
        self.targets += 1
        self.damage += 1
