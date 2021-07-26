import pygame
from pygame.locals import *
import os
import sys
import random

from pygame.mixer import pause

import tower
import enemy
import player
from globs import *


pygame.init()
from textRenderer import *


def blit_alpha(target, source, location, opacity):
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (0, 0))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)
    target.blit(temp, location)

SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()

def quitgame():
    pygame.quit()
    quit()


def button(msg,x,y,w,h,bc,tc,tx,ty,tfont,action=None):
    global screen
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        if click[0] == 1 and action != None:
            action()         
    pygame.draw.rect(screen, bc,(x,y,w,h))
    draw_text(msg, tfont, tc, screen, tx, ty)


def unpause():
    global pause
    pause = False

def paused():
    blit_alpha(screen, transparentOverlay, (0, 0), 128)
    text_width, text_height = contrastMedFont.size("Main Menu")
    draw_text("Main Menu", contrastMedFont, (252, 244, 230), screen, (SCREEN_WIDTH/2 - text_width/2), 120)
    
    text_width, text_height = medFont.size("Main Menu")
    draw_text("Main Menu", medFont, (235, 191, 107), screen, (SCREEN_WIDTH/2 - text_width/2), 120)

    text_width, text_height = contrastLrgFont.size("A.I. DEFENCE")
    draw_text("A.I. DEFENCE", contrastLrgFont, (244, 197, 113), screen, (SCREEN_WIDTH/2 - text_width/2), 37)

    text_width, text_height = lrgFont.size("A.I. DEFENCE")
    draw_text("A.I. DEFENCE", lrgFont, (252, 247, 239), screen, (SCREEN_WIDTH/2 - text_width/2), 40)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        text_width, text_height = font.size("PLAY")
        button("PLAY",(SCREEN_WIDTH/2 - 100),190,200,70,(129, 185, 62),(254, 244, 228),(SCREEN_WIDTH/2 - text_width/2), 209,font,unpause)
        text_width, text_height = font.size("QUIT")
        button("QUIT",(SCREEN_WIDTH/2 - 100),290,200,60,(71, 126, 47),(254, 244, 228), (SCREEN_WIDTH/2 - text_width/2), 304,font,quitgame)
        pygame.display.update()
        clock.tick(60)   

def pauser():
    global pause 
    pause = True
    paused()

def playGame():
    global pause
    pauser()
    enemies = [enemy.AI(0, 240, 6), enemy.AI(0, 240, 1.5),
                        enemy.AI(0, 240, 2), enemy.AI(0, 240, 3)]

    test = tower.ElectricTower((350, 288))

    running = True
    while running == True:
        mx, my = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                enemies.append(enemy.AI(0, 240, random.choice([6, 1.5, 2, 3])))

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pauser()


        pygame.display.set_caption(str(pygame.mouse.get_pos()))

        screen.fill((255, 255, 255))
        screen.blit(bg, (0, 0))


        # drawing the menu bar
        menuBar = pygame.Rect(0, 0, SCREEN_WIDTH, 60)
        pygame.draw.rect(screen, (28, 73, 49), menuBar)  # colour of menuBar

        text_width, text_height = medFont.size("I I")
        button("I I",(SCREEN_WIDTH - text_width - 80),0,(text_width + 80),60,(235, 191, 107),(252, 244, 230), (SCREEN_WIDTH - text_width - 40), 8,medFont,pauser)
        

        # enemy spawning
        enemies[:] = [enemy for enemy in enemies if enemy.alive]

        enemies.sort(key=lambda e: len(e.path), reverse=True)

        for e in enemies:
            e.update()
            screen.blit(pygame.transform.rotate(
                frameprogression[e.frame], e.angle), (e.x-32, e.y-32))

        # target = test.getTarget(enemies)

        # if target: screen.blit(pygame.transform.rotate(slimetest,target.angle),(target.x-32,target.y-32))
        # pygame.draw.circle(screen, (0,0,255), (test.x,test.y), 100, 1)
        test.update(enemies)
        pygame.display.flip()

        clock.tick(60)

playGame()

