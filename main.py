from cgitb import small
import wave
import pygame
from pygame.locals import *
import os
import sys
import random
from waves import wavescombined
from pygame.mixer import pause

import tower
import enemy
import player
import globs


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
    blit_alpha(screen, globs.transparentOverlay, (0, 0), 128)
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
        globs.clock.tick(60)   

counter = 0

def pauser():
    global pause 
    pause = True
    paused()

def youwin():
    pygame.quit()

def nextwave():
    global counter
    counter += 1

def playGame():
    global pause
    global counter
    pauser()
    #enemies = [enemy.AI(0, 240, 6), enemy.AI(0, 240, 1.5),enemy.AI(0, 240, 2), enemy.AI(0, 240, 3)]
    enemies = []
    
    
    
    towers = [tower.FireTower((350, 288)),tower.IceTower((460,288)),tower.FireTower((350,382))]
    running = True
    while running == True:
        waiting = False
        mx, my = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                pass


            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pauser()
                elif event.key == pygame.K_SPACE:
                    random.choice(towers).levelup(type="range")

        # wave handling
        
        if wavescombined[counter] == "n":
            counter+=1
        elif wavescombined[counter] == "w":
            text_width, text_height = medFont.size("I I")
            waiting = True
        else:
            enemies.append(enemy.AI(wavescombined[counter]))
            counter += 1

        screen.fill((255, 255, 255))
        screen.blit(globs.bg, (0, 0))

        # drawing the menu bar
        menuBar = pygame.Rect(0, 0, SCREEN_WIDTH, 55)
        pygame.draw.rect(screen, (1, 50, 24), menuBar)  # colour of menuBar

        text_width, text_height = medFont.size("I I")
        button("I I",(SCREEN_WIDTH - text_width - 80),0,(text_width + 80),55,(235, 191, 107),(252, 244, 230), (SCREEN_WIDTH - text_width - 40), 8,medFont,pauser)
        
        # drawing stuff while next wave incoming
        

        if waiting:
            button("",(SCREEN_WIDTH - 2*text_width - 200+60),0,(text_width+60),55,(255, 191, 107),(252, 244, 230), (SCREEN_WIDTH - 2*text_width - 80+60), 8,medFont,nextwave)
            pygame.draw.polygon(screen,(252, 244, 230),[((SCREEN_WIDTH - 2*text_width - 180+70),(55-text_height)),((SCREEN_WIDTH - 2*text_width - 180+70),55-(55-text_height)),((SCREEN_WIDTH - text_width - 180+70),27)])
            
            screen.blit(globs.icesprite,((350),(55-text_height)))
            
            screen.blit(globs.firesprite,((450),(55-text_height)))
            
            screen.blit(globs.electricsprite,((550),(55-text_height)))

            text_height,text_width = smallFont.size("200")
            draw_text("200", smallFont, (235, 191, 107), screen, 380, (54-text_height)/2) # ice cost
            draw_text("200", smallFont, (235, 191, 107), screen, 480, (54-text_height)/2) # fire cost
            draw_text("200", smallFont, (235, 191, 107), screen, 580, (54-text_height)/2) # elec cost
            
            if globs.playercash < 2000: # replace 2000 with ice cost
                pygame.draw.rect(screen, (226,54,54), (340, 5, 80, 45),3)
                pygame.draw.line(screen, (226,54,54), (340, 5), (420, 50), 3)
                pygame.draw.line(screen, (226,54,54), (340, 50), (420, 5), 3)

            if globs.playercash < 2000: # replace 2000 with fire cost
                pygame.draw.rect(screen, (226,54,54), (440, 5, 80, 45),3)
                pygame.draw.line(screen, (226,54,54), (440, 5), (520, 50), 3)
                pygame.draw.line(screen, (226,54,54), (440, 50), (520, 5), 3)

            if globs.playercash < 2000: # replace 2000 with elec cost
                pygame.draw.rect(screen, (226,54,54), (540, 5, 80, 45),3)
                pygame.draw.line(screen, (226,54,54), (540, 5), (620, 50), 3)
                pygame.draw.line(screen, (226,54,54), (540, 50), (620, 5), 3)

        # drawing player health and player currency
        screen.blit(globs.coin,(45,19))
        text_width, text_height = font.size(str(globs.playercash))
        draw_text(str(globs.playercash), font, (235, 191, 107), screen, 75, (54-text_height)/2)
        
        screen.blit(globs.heart,(150,19))
        text_width, text_height = font.size(str(globs.playerhealth))
        draw_text(str(globs.playerhealth), font, (235, 191, 107), screen, 180, (54-text_height)/2)

        

        # enemy culling
        enemies[:] = [enemy for enemy in enemies if enemy.alive]

        enemies.sort(key=lambda e: len(e.path), reverse=True)

        for e in enemies:
            e.update()
            if e.type == "s":
                screen.blit(pygame.transform.rotate(globs.sframeprogression[e.frame], e.angle), (e.x-32, e.y-32))
            elif e.type == "c":
                screen.blit(pygame.transform.rotate(globs.cframeprogression[e.frame], e.angle), (e.x-16, e.y-16))
            else: 
                screen.blit(pygame.transform.rotate(globs.pframeprogression[e.frame], e.angle), (e.x-16, e.y-16))
        # target = test.getTarget(enemies)

        # if target: screen.blit(pygame.transform.rotate(slimetest,target.angle),(target.x-32,target.y-32))
        # pygame.draw.circle(screen, (0,0,255), (test.x,test.y), 100, 1)
        for t in towers:
            t.update(enemies)

        pygame.display.flip()

        globs.clock.tick(60)

playGame()

