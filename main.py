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

placingIce = False
placingFire = False
placingElec = False
import itertools


def pRect(x1, y1, x2, y2):
    return pygame.Rect((x1, y1), (x2 - x1, y2 - y1))


trackbounds = [
    pRect(0, 222, 474, 269),
    pRect(279, 98, 475, 146),
    pRect(334, 144, 277, 222),
    pRect(417, 145, 475, 225),
    pRect(332, 268, 281, 478),
    pRect(281, 435, 138, 477),
    pRect(198, 436, 138, 300),
    pRect(138, 300, 584, 353),
    pRect(584, 353, 527, 177),
    pRect(527, 177, 699, 230),
    pRect(699, 230, 636, 432),
    pRect(636, 432, 373, 375),
    pRect(373, 375, 426, 579),
    pRect(0, 55, 899, 0),
]

towerhitboxes = []

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


def button(msg, x, y, w, h, bc, tc, tx, ty, tfont, action=None):
    global screen
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        if click[0] == 1 and action != None:
            action()
    if bc:
        pygame.draw.rect(screen, bc, (x, y, w, h))
    if msg:
        draw_text(msg, tfont, tc, screen, tx, ty)


def unpause():
    global pause
    pause = False


def paused():
    global pause
    pause = True
    blit_alpha(screen, globs.transparentOverlay, (0, 0), 128)
    text_width, text_height = contrastMedFont.size("Main Menu")
    draw_text(
        "Main Menu",
        contrastMedFont,
        (252, 244, 230),
        screen,
        (SCREEN_WIDTH / 2 - text_width / 2),
        120,
    )

    text_width, text_height = medFont.size("Main Menu")
    draw_text(
        "Main Menu",
        medFont,
        (235, 191, 107),
        screen,
        (SCREEN_WIDTH / 2 - text_width / 2),
        120,
    )

    text_width, text_height = contrastLrgFont.size("A.I. DEFENCE")
    draw_text(
        "A.I. DEFENCE",
        contrastLrgFont,
        (244, 197, 113),
        screen,
        (SCREEN_WIDTH / 2 - text_width / 2),
        37,
    )

    text_width, text_height = lrgFont.size("A.I. DEFENCE")
    draw_text(
        "A.I. DEFENCE",
        lrgFont,
        (252, 247, 239),
        screen,
        (SCREEN_WIDTH / 2 - text_width / 2),
        40,
    )

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        text_width, text_height = font.size("PLAY")
        button(
            "PLAY",
            (SCREEN_WIDTH / 2 - 100),
            190,
            200,
            70,
            (129, 185, 62),
            (254, 244, 228),
            (SCREEN_WIDTH / 2 - text_width / 2),
            209,
            font,
            unpause,
        )
        text_width, text_height = font.size("QUIT")
        button(
            "QUIT",
            (SCREEN_WIDTH / 2 - 100),
            290,
            200,
            60,
            (71, 126, 47),
            (254, 244, 228),
            (SCREEN_WIDTH / 2 - text_width / 2),
            304,
            font,
            quitgame,
        )
        pygame.display.update()
        globs.clock.tick(60)


counter = 0
wavenum = 0


def nextwave():
    global wavenum
    global counter
    if wavescombined[counter + 1] == "x":
        endGame("win")
        return
    counter += 1
    wavenum += 1
    globs.playercash += 50


def newIceTower():
    global placingIce
    if placingIce:
        return
    globs.playercash -= globs.iceCost
    placingIce = True


def newFireTower():
    global placingFire
    if placingFire:
        return
    globs.playercash -= globs.fireCost
    placingFire = True


def newElecTower():
    global placingElec
    if placingElec:
        return
    globs.playercash -= globs.elecCost
    placingElec = True


def endGame(scenario):
    if scenario == "win":
        while True:
            screen.fill((1, 50, 24))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            text_width, text_height = font.size("Congratulations! You win!")
            draw_text(
                "Congratulations! You win!",
                font,
                (254, 244, 228),
                screen,
                (SCREEN_WIDTH / 2 - text_width / 2),
                110,
            )
            text_width, text_height = font.size(
                "You had "
                + str(globs.playerhealth)
                + " lives left, and "
                + str(globs.playercash)
                + " leftover coins."
            )
            draw_text(
                "You had "
                + str(globs.playerhealth)
                + " lives left, and "
                + str(globs.playercash)
                + " leftover coins.",
                font,
                (254, 244, 228),
                screen,
                (SCREEN_WIDTH / 2 - text_width / 2),
                200,
            )
            text_width, text_height = font.size("QUIT")
            button(
                "QUIT",
                (SCREEN_WIDTH / 2 - 100),
                290,
                200,
                60,
                (71, 126, 47),
                (254, 244, 228),
                (SCREEN_WIDTH / 2 - text_width / 2),
                304,
                font,
                quitgame,
            )
            pygame.display.update()
            globs.clock.tick(60)
    else:
        while True:
            screen.fill((1, 50, 24))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            text_width, text_height = font.size("Oh no! You lost!")
            draw_text(
                "Oh no! You lost!",
                font,
                (254, 244, 228),
                screen,
                (SCREEN_WIDTH / 2 - text_width / 2),
                110,
            )
            text_width, text_height = font.size(
                "You made it to wave " + str(wavenum) + " out of 20."
            )
            draw_text(
                "You made it to wave " + str(wavenum) + " out of 20.",
                font,
                (254, 244, 228),
                screen,
                (SCREEN_WIDTH / 2 - text_width / 2),
                200,
            )
            text_width, text_height = font.size("QUIT")
            button(
                "QUIT",
                (SCREEN_WIDTH / 2 - 100),
                290,
                200,
                60,
                (71, 126, 47),
                (254, 244, 228),
                (SCREEN_WIDTH / 2 - text_width / 2),
                304,
                font,
                quitgame,
            )
            pygame.display.update()
            globs.clock.tick(60)


def playGame():
    global pause
    global counter
    global placingIce
    global placingFire
    global placingElec
    global trackbounds
    global towerhitboxes
    global wavenum
    wavelength = len(wavescombined) - 1
    paused()

    # enemies = [enemy.AI(0, 240, 6), enemy.AI(0, 240, 1.5),enemy.AI(0, 240, 2), enemy.AI(0, 240, 3)]
    enemies = []

    towers = []
    # towers = [tower.FireTower((350, 288)),tower.IceTower((460,288)),tower.FireTower((350,382))]
    running = True
    while running == True:
        waiting = False
        mx, my = pygame.mouse.get_pos()
        mpos = str(mx) + " " + str(my)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONUP:
                globs.clicked = False

            elif (
                event.type == pygame.MOUSEBUTTONDOWN
                and pygame.Rect(mx - 13, my, 26, 21).collidelist(
                    trackbounds + towerhitboxes
                )
                == -1
            ):

                if placingElec:
                    placingElec = False
                    towers.append(
                        tower.ElectricTower((mx, my), pygame.Rect(mx - 13, my, 26, 21))
                    )
                    towerhitboxes.append(pygame.Rect(mx - 13, my, 26, 21))

                elif placingIce:
                    placingIce = False
                    towers.append(
                        tower.IceTower((mx, my), pygame.Rect(mx - 13, my, 26, 21))
                    )
                    towerhitboxes.append(pygame.Rect(mx - 13, my, 26, 21))

                elif placingFire:
                    placingFire = False
                    towers.append(
                        tower.FireTower((mx, my), pygame.Rect(mx - 13, my, 26, 21))
                    )
                    towerhitboxes.append(pygame.Rect(mx - 13, my, 26, 21))

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused()

        # wave handling

        if globs.playerhealth <= 0:
            endGame("lose")

        if wavescombined[counter] == "n":
            counter += 1
        elif wavescombined[counter] == "w":
            if len(enemies) == 0:
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
        button(
            "I I",
            (SCREEN_WIDTH - text_width - 80),
            0,
            (text_width + 80),
            55,
            (235, 191, 107),
            (252, 244, 230),
            (SCREEN_WIDTH - text_width - 40),
            8,
            medFont,
            paused,
        )

        # drawing stuff while next wave incoming

        if waiting:
            if not placingElec and not placingFire and not placingIce:
                button(
                    "",
                    (SCREEN_WIDTH - 2 * text_width - 200 + 60),
                    0,
                    (text_width + 60),
                    55,
                    (255, 191, 107),
                    (252, 244, 230),
                    (SCREEN_WIDTH - 2 * text_width - 80 + 60),
                    8,
                    medFont,
                    nextwave,
                )
            else:
                button(
                    "",
                    (SCREEN_WIDTH - 2 * text_width - 200 + 60),
                    0,
                    (text_width + 60),
                    55,
                    (255, 191, 107),
                    (252, 244, 230),
                    (SCREEN_WIDTH - 2 * text_width - 80 + 60),
                    8,
                    medFont,
                )

            pygame.draw.polygon(
                screen,
                (252, 244, 230),
                [
                    ((SCREEN_WIDTH - 2 * text_width - 180 + 70), (55 - text_height)),
                    (
                        (SCREEN_WIDTH - 2 * text_width - 180 + 70),
                        55 - (55 - text_height),
                    ),
                    ((SCREEN_WIDTH - text_width - 180 + 70), 27),
                ],
            )

            if globs.playercash < globs.iceCost:
                pygame.draw.rect(screen, (226, 54, 54), (340, 5, 80, 45), 3)
                pygame.draw.line(screen, (226, 54, 54), (340, 5), (420, 50), 3)
                pygame.draw.line(screen, (226, 54, 54), (340, 50), (420, 5), 3)
            elif not placingIce and not placingElec and not placingFire:
                button("", 340, 5, 80, 45, (1, 50, 24), 0, 0, 0, font, newIceTower)

            if globs.playercash < globs.fireCost:
                pygame.draw.rect(screen, (226, 54, 54), (440, 5, 80, 45), 3)
                pygame.draw.line(screen, (226, 54, 54), (440, 5), (520, 50), 3)
                pygame.draw.line(screen, (226, 54, 54), (440, 50), (520, 5), 3)
            elif not placingIce and not placingElec and not placingFire:
                button("", 440, 5, 80, 45, (1, 50, 24), 0, 0, 0, font, newFireTower)

            if globs.playercash < globs.elecCost:
                pygame.draw.rect(screen, (226, 54, 54), (540, 5, 80, 45), 3)
                pygame.draw.line(screen, (226, 54, 54), (540, 5), (620, 50), 3)
                pygame.draw.line(screen, (226, 54, 54), (540, 50), (620, 5), 3)
            elif not placingIce and not placingElec and not placingFire:
                button("", 540, 5, 80, 45, (1, 50, 24), 0, 0, 0, font, newElecTower)

            screen.blit(globs.icesprite, ((350), (55 - text_height)))

            screen.blit(globs.firesprite, ((450), (55 - text_height)))

            screen.blit(globs.electricsprite, ((550), (55 - text_height)))

            text_height, text_width = smallFont.size("200")
            draw_text(
                str(globs.iceCost),
                smallFont,
                (235, 191, 107),
                screen,
                380,
                (54 - text_height) / 2,
            )  # ice cost
            draw_text(
                str(globs.fireCost),
                smallFont,
                (235, 191, 107),
                screen,
                480,
                (54 - text_height) / 2,
            )  # fire cost
            draw_text(
                str(globs.elecCost),
                smallFont,
                (235, 191, 107),
                screen,
                580,
                (54 - text_height) / 2,
            )  # elec cost

            if placingIce:
                screen.blit(globs.icesprite, (mx - 16, my - 11))

            elif placingElec:
                screen.blit(globs.electricsprite, (mx - 16, my - 11))

            elif placingFire:
                screen.blit(globs.firesprite, (mx - 16, my - 11))

        # drawing player health and player currency
        screen.blit(globs.coin, (45, 19))
        text_width, text_height = font.size(str(globs.playercash))
        draw_text(
            str(globs.playercash),
            font,
            (235, 191, 107),
            screen,
            75,
            (54 - text_height) / 2,
        )

        screen.blit(globs.heart, (150, 19))
        text_width, text_height = font.size(str(globs.playerhealth))
        draw_text(
            str(globs.playerhealth),
            font,
            (235, 191, 107),
            screen,
            180,
            (54 - text_height) / 2,
        )

        text_width, text_height = font.size(str(wavenum))
        draw_text(
            str(str(wavenum) + "/20"),
            font,
            (235, 191, 107),
            screen,
            260,
            (54 - text_height) / 2,
        )

        # enemy culling
        enemies[:] = [enemy for enemy in enemies if enemy.alive]

        enemies.sort(key=lambda e: len(e.path), reverse=True)

        for e in enemies:
            e.update()
            if e.type == "s":
                screen.blit(
                    pygame.transform.rotate(globs.sframeprogression[e.frame], e.angle),
                    (e.x - 32, e.y - 32),
                )
            elif e.type == "c":
                screen.blit(
                    pygame.transform.rotate(globs.cframeprogression[e.frame], e.angle),
                    (e.x - 16, e.y - 16),
                )
            else:
                screen.blit(
                    pygame.transform.rotate(globs.pframeprogression[e.frame], e.angle),
                    (e.x - 16, e.y - 16),
                )
        # target = test.getTarget(enemies)

        # if target: screen.blit(pygame.transform.rotate(slimetest,target.angle),(target.x-32,target.y-32))
        # pygame.draw.circle(screen, (0,0,255), (test.x,test.y), 100, 1)
        for t in towers:
            t.update(enemies)

        if waiting:
            if globs.playercash >= 100:
                for t in towers:
                    if t.level < 5:
                        if not globs.clicked:
                            button(
                                None,
                                t.hitbox.x,
                                t.hitbox.y,
                                t.hitbox.w,
                                t.hitbox.h,
                                None,
                                None,
                                None,
                                None,
                                None,
                                t.levelup,
                            )

                        pygame.draw.polygon(
                            screen,
                            (235, 191, 107),
                            [
                                t.hitbox.bottomleft,
                                t.hitbox.midtop,
                                t.hitbox.bottomright,
                                t.hitbox.center,
                            ],
                        )

        pygame.display.flip()

        globs.clock.tick(60)


playGame()
