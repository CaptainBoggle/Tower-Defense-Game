import pygame
from pygame.locals import *
import os
import sys
import random

import tower
import enemy
import player
import menu
from globs import *

pygame.init()
from textRenderer import *

SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()


# showMenu = True

# if showMenu == True:
#     menu.main_menu()
# else:
#     pygame.init()
#     playGame()

def toggleMenu(showMenu):
    if(showMenu):  
        menu.main_menu(toggleMenu)
    else:
        playGame(toggleMenu)


def playGame(toggleMenu):
    slimetest.fill("RED")

    enemies = [enemy.AI(0,240,6),enemy.AI(0,240,1.5),enemy.AI(0,240,2),enemy.AI(0,240,3)]

    test = tower.ElectricTower((350,288))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                enemies.append(enemy.AI(0,240,random.choice([6,1.5,2,3])))

        pygame.display.set_caption(str(pygame.mouse.get_pos()))
                

        screen.fill((255,255,255))
        screen.blit(bg, (0,0))

        click = False

        showMenu = False

        # drawing the menu bar
        menuBar = pygame.Rect(0, 0, SCREEN_WIDTH, 60)
        pygame.draw.rect(screen, (28, 73, 49), menuBar) # colour of menuBar 

        text_width, text_height = font.size("MENU")

        menuButton = pygame.Rect((SCREEN_WIDTH - text_width - 80), 0, (text_width + 80), 60)
        pygame.draw.rect(screen, (235, 191, 107), menuButton) # colour of menuButton
        
        mx, my = pygame.mouse.get_pos()
        if menuButton.collidepoint((mx, my)): # if menu button is pressed
            if click:
                print("CLick")
                menu.main_menu(toggleMenu)

        draw_text("MENU", font, (252, 244, 230), screen, (SCREEN_WIDTH - text_width - 40), 14)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True #signals the button press

        #enemy spawning
        enemies[:] = [enemy for enemy in enemies if enemy.alive]
        
        enemies.sort(key=lambda e: len(e.path), reverse=True)
        
        for e in enemies:
            e.update()
            screen.blit(pygame.transform.rotate(frameprogression[e.frame],e.angle),(e.x-32,e.y-32))
        
        #target = test.getTarget(enemies)

        #if target: screen.blit(pygame.transform.rotate(slimetest,target.angle),(target.x-32,target.y-32))
        #pygame.draw.circle(screen, (0,0,255), (test.x,test.y), 100, 1)
        test.update(enemies)
        

        clock.tick(60)
        pygame.display.flip()

# playGame()
menu.main_menu(toggleMenu)