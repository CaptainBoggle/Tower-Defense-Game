import wave
import pygame
from pygame.locals import *
import os
import sys
import random
from waves import WAVES_COMBINED

import tower
import enemy
import globs
import itertools
from text import *


while True: # Loop everything to make restarting easier.
    replay = False

    def play_again(): # Restarts game
        global replay
        replay = True

    placing_ice = False # initialise variables
    placing_fire = False
    placing_electric = False

    def rect_from_points(x1, y1, x2, y2): # I needed to make rectangles with two points instead of one point and dimensions
        return pygame.Rect((x1, y1), (x2 - x1, y2 - y1))

    TRACK_BOUNDS = [ # Rects that cover track to prevent towers being placed on track
        rect_from_points(0, 222, 474, 269),
        rect_from_points(279, 98, 475, 146),
        rect_from_points(334, 144, 277, 222),
        rect_from_points(417, 145, 475, 225),
        rect_from_points(332, 268, 281, 478),
        rect_from_points(281, 435, 138, 477),
        rect_from_points(198, 436, 138, 300),
        rect_from_points(138, 300, 584, 353),
        rect_from_points(584, 353, 527, 177),
        rect_from_points(527, 177, 699, 230),
        rect_from_points(699, 230, 636, 432),
        rect_from_points(636, 432, 373, 375),
        rect_from_points(373, 375, 426, 579),
        rect_from_points(0, 55, 899, 0),
    ]

    tower_hitboxes = []
    showing_guide = False
    pygame.init() # initialise pygame
    save_background = None
    
    # sound manager
    pygame.mixer.music.load(os.path.join("files","music.wav"))
    CLICK_SOUND = pygame.mixer.Sound(os.path.join("files","click.wav"))
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)


    def blit_alpha(target, source, location, opacity): # helps with transparency overlay
        temp = pygame.Surface((source.get_width(), source.get_height())).convert()
        temp.blit(target, (0, 0))
        temp.blit(source, (0, 0))
        temp.set_alpha(opacity)
        target.blit(temp, location)

    SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size() # get constants for screen dimensions

    def quit_game(): # exit the game
        pygame.quit()
        quit()

    def button(msg, x, y, w, h, bc, tc, tx, ty, tfont, action=None): # general button function, best function ever
        global screen
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            if click[0] == 1 and action != None:
                CLICK_SOUND.play()
                action()
        if bc:
            pygame.draw.rect(screen, bc, (x, y, w, h))
        if msg:
            draw_text(msg, tfont, tc, screen, tx, ty)

    def unpause(): # call to unpause
        global pause
        pause = False
        pygame.mixer.music.unpause()

    def hide_guide(): # call to go from guide page to pause menu
        global save_background
        global showing_guide
        showing_guide = False
        screen.blit(
            pygame.image.fromstring(save_background, (900, 580), "RGBA"), (0, 0)
        )
        paused(True)

    def show_guide(): # call to go from pause menu to guide page
        global showing_guide
        global save_background
        save_background = pygame.image.tostring(globs.SCREEN, "RGBA")
        showing_guide = True
        while showing_guide:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            globs.SCREEN.fill((4, 67, 40))
            SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()
            text_width, text_height = CONTRAST_MEDIUM_FONT.size("Guide")
            draw_text(
                "Guide",
                CONTRAST_MEDIUM_FONT,
                (235, 191, 107),
                globs.SCREEN,
                (SCREEN_WIDTH / 2 - text_width / 2),
                54,
            )
            text_width, text_height = MEDIUM_FONT.size("Guide")
            draw_text(
                "Guide",
                MEDIUM_FONT,
                (252, 244, 230),
                globs.SCREEN,
                (SCREEN_WIDTH / 2 - text_width / 2),
                54,
            )

            text_width, text_height = FONT.size(
                "AIM: Stop incoming AI from corrupting the system"
            )
            draw_text(
                "AIM: to stop incoming AI from corrupting the system",
                FONT,
                (235, 191, 107),
                globs.SCREEN,
                (SCREEN_WIDTH / 2 - text_width / 2),
                110,
            )

            text_width, text_height = INFO_FONT.size(
                "Place towers on the map by clicking once to select - once more to place down"
            )
            draw_text(
                "Place towers on the map by clicking once to select - once more to place down",
                INFO_FONT,
                (252, 244, 230),
                globs.SCREEN,
                (SCREEN_WIDTH / 2 - text_width / 2),
                160,
            )

            text_width, text_height = INFO_FONT.size(
                "This will cost money as indicated next to the icons"
            )
            draw_text(
                "This will cost money as indicated next to the icons",
                INFO_FONT,
                (252, 244, 230),
                globs.SCREEN,
                (SCREEN_WIDTH / 2 - text_width / 2),
                200,
            )

            text_width, text_height = INFO_FONT.size(
                "ICE TOWER: Slows nearby enemies"
            )
            draw_text(
                "ICE TOWER: Slows nearby enemies",
                INFO_FONT,
                (252, 244, 230),
                globs.SCREEN,
                (SCREEN_WIDTH / 2 - text_width / 2),
                240,
            )

            text_width, text_height = INFO_FONT.size(
                "FIRE: Damages nearby enemies"
            )
            draw_text(
                "FIRE TOWER: Damages nearby enemies",
                INFO_FONT,
                (252, 244, 230),
                globs.SCREEN,
                (SCREEN_WIDTH / 2 - text_width / 2),
                260,
            )

            text_width, text_height = INFO_FONT.size(
                "ELECTRIC TOWER: Slow but strong beams"
            )
            draw_text(
                "ELECTRIC TOWER: Slow but strong beams",
                INFO_FONT,
                (252, 244, 230),
                globs.SCREEN,
                (SCREEN_WIDTH / 2 - text_width / 2),
                280,
            )

            text_width, text_height = INFO_FONT.size(
                "Click a tower with an orange arrow to upgrade - COST: $100"
            )
            draw_text(
                "Click a tower with an orange arrow to upgrade - COST: $100",
                INFO_FONT,
                (252, 244, 230),
                globs.SCREEN,
                (SCREEN_WIDTH / 2 - text_width / 2),
                320,
            )

            text_width, text_height = INFO_FONT.size(
                "Press the green play icon (top right) to start the next wave"
            )
            draw_text(
                "Press the green play icon (top right) to start the next wave",
                INFO_FONT,
                (252, 244, 230),
                globs.SCREEN,
                (SCREEN_WIDTH / 2 - text_width / 2),
                360,
            )

            text_width, text_height = INFO_FONT.size(
                "Survive all 20 waves to win: If an enemy gets through - you lose lives"
            )
            draw_text(
                "Survive all 20 waves to win: If an enemy gets through - you lose lives",
                INFO_FONT,
                (252, 244, 230),
                globs.SCREEN,
                (SCREEN_WIDTH / 2 - text_width / 2),
                400,
            )

            text_width, text_height = INFO_FONT.size(
                "Enemies do damage based on their health"
            )
            draw_text(
                "Enemies do damage based on their health",
                INFO_FONT,
                (252, 244, 230),
                globs.SCREEN,
                (SCREEN_WIDTH / 2 - text_width / 2),
                440,
            )

            text_width, text_height = FONT.size("BACK")
            button(
                "BACK",
                (SCREEN_WIDTH / 2 - 100),
                485,
                200,
                60,
                (71, 126, 47),
                (254, 244, 228),
                (SCREEN_WIDTH / 2 - text_width / 2),
                495,
                FONT,
                hide_guide,
            )
            pygame.display.update()
            globs.CLOCK.tick(60)

    def paused(from_guide=False): # does this while paused, also call to pause
        global pause
        pause = True
        pygame.mixer.music.pause()
        if not from_guide:
            blit_alpha(screen, globs.TRANSPARENT_OVERLAY, (0, 0), 128)
        text_width, text_height = CONTRAST_MEDIUM_FONT.size("Main Menu")
        draw_text(
            "Main Menu",
            CONTRAST_MEDIUM_FONT,
            (252, 244, 230),
            screen,
            (SCREEN_WIDTH / 2 - text_width / 2),
            120,
        )

        text_width, text_height = MEDIUM_FONT.size("Main Menu")
        draw_text(
            "Main Menu",
            MEDIUM_FONT,
            (235, 191, 107),
            screen,
            (SCREEN_WIDTH / 2 - text_width / 2),
            120,
        )

        text_width, text_height = CONTRAST_LARGE_FONT.size("A.I. DEFENCE")
        draw_text(
            "A.I. DEFENCE",
            CONTRAST_LARGE_FONT,
            (244, 197, 113),
            screen,
            (SCREEN_WIDTH / 2 - text_width / 2),
            37,
        )

        text_width, text_height = LARGE_FONT.size("A.I. DEFENCE")
        draw_text(
            "A.I. DEFENCE",
            LARGE_FONT,
            (252, 247, 239),
            screen,
            (SCREEN_WIDTH / 2 - text_width / 2),
            40,
        )

        while pause: # Loop while paused
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            text_width, text_height = FONT.size("PLAY")
            button(
                "PLAY",
                (SCREEN_WIDTH / 2 - 100),
                190,
                200,
                70,
                (71, 126, 47),
                (254, 244, 228),
                (SCREEN_WIDTH / 2 - text_width / 2),
                209,
                FONT,
                unpause,
            )
            text_width, text_height = FONT.size("HELP")
            button(
                "HELP",
                (SCREEN_WIDTH / 2 - 100),
                290,
                200,
                60,
                (71, 126, 47),
                (254, 244, 228),
                (SCREEN_WIDTH / 2 - text_width / 2),
                304,
                FONT,
                show_guide,
            )

            text_width, text_height = FONT.size("QUIT")
            button(
                "QUIT",
                (SCREEN_WIDTH / 2 - 100),
                390,
                200,
                60,
                (71, 126, 47),
                (254, 244, 228),
                (SCREEN_WIDTH / 2 - text_width / 2),
                404,
                FONT,
                quit_game,
            )
            pygame.display.update()
            globs.CLOCK.tick(60)

    counter = 0
    wave_num = 0

    def next_wave(): # Call to go to next wave
        global wave_num
        global counter
        if WAVES_COMBINED[counter + 1] == "x":
            end_game("win")
            return
        globs.player_cash += 100
        counter += 1
        wave_num += 1

    def new_ice_tower(): # Create new ice tower
        global placing_ice
        if placing_ice:
            return
        globs.player_cash -= globs.ICE_COST
        placing_ice = True

    def new_fire_tower(): # Create new fire tower
        global placing_fire
        if placing_fire:
            return
        globs.player_cash -= globs.FIRE_COST
        placing_fire = True

    def new_electric_tower(): # Create new electric tower
        global placing_electric
        if placing_electric:
            return
        globs.player_cash -= globs.ELECTRIC_COST
        placing_electric = True

    def end_game(scenario): # Call at the end of the game, win or lose.
        global replay
        if scenario == "win":
            while True:
                screen.fill((1, 50, 24))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                text_width, text_height = FONT.size("Congratulations! You win!")
                draw_text(
                    "Congratulations! You win!",
                    FONT,
                    (254, 244, 228),
                    screen,
                    (SCREEN_WIDTH / 2 - text_width / 2),
                    110,
                )
                text_width, text_height = FONT.size(
                    "You had "
                    + str(globs.player_health)
                    + " lives left, and "
                    + str(globs.player_cash)
                    + " leftover coins."
                )
                draw_text(
                    "You had "
                    + str(globs.player_health)
                    + " lives left, and "
                    + str(globs.player_cash)
                    + " leftover coins.",
                    FONT,
                    (254, 244, 228),
                    screen,
                    (SCREEN_WIDTH / 2 - text_width / 2),
                    200,
                )
                text_width, text_height = FONT.size("QUIT")
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
                    FONT,
                    quit_game,
                )

                text_width, text_height = FONT.size("PLAY AGAIN?")
                button(
                    "PLAY AGAIN?",
                    (SCREEN_WIDTH / 2 - 100),
                    370,
                    200,
                    60,
                    (71, 126, 47),
                    (254, 244, 228),
                    (SCREEN_WIDTH / 2 - text_width / 2),
                    384,
                    FONT,
                    play_again,
                )
                if replay:
                    return
                pygame.display.update()
                globs.CLOCK.tick(60)
        else:
            while True:
                screen.fill((1, 50, 24))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                text_width, text_height = FONT.size("Oh no! You lost!")
                draw_text(
                    "Oh no! You lost!",
                    FONT,
                    (254, 244, 228),
                    screen,
                    (SCREEN_WIDTH / 2 - text_width / 2),
                    110,
                )
                text_width, text_height = FONT.size(
                    "You made it to wave " + str(wave_num) + " out of 20."
                )
                draw_text(
                    "You made it to wave " + str(wave_num) + " out of 20.",
                    FONT,
                    (254, 244, 228),
                    screen,
                    (SCREEN_WIDTH / 2 - text_width / 2),
                    200,
                )
                text_width, text_height = FONT.size("QUIT")
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
                    FONT,
                    quit_game,
                )

                text_width, text_height = FONT.size("PLAY AGAIN?")
                button(
                    "PLAY AGAIN?",
                    (SCREEN_WIDTH / 2 - 100),
                    370,
                    200,
                    60,
                    (71, 126, 47),
                    (254, 244, 228),
                    (SCREEN_WIDTH / 2 - text_width / 2),
                    384,
                    FONT,
                    play_again,
                )
                if replay:
                    return
                pygame.display.update()
                globs.CLOCK.tick(60)

    def play_game(): # main gameplay loop
        global replay 
        global pause
        global counter
        global placing_ice
        global placing_fire
        global placing_electric
        global TRACK_BOUNDS
        global tower_hitboxes
        global wave_num
        wavelength = len(WAVES_COMBINED) - 1
        screen.fill((4, 67, 40))
        paused()

        enemies = []

        towers = []
        running = True
        while running:
            if replay:
                globs.clicked = False
                globs.player_cash = 450
                globs.player_health = 200
                return

            waiting = False
            mx, my = pygame.mouse.get_pos()
            for event in pygame.event.get(): # input handling
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONUP:
                    globs.clicked = False

                elif (
                    event.type == pygame.MOUSEBUTTONDOWN
                    and pygame.Rect(mx - 13, my, 26, 21).collidelist(
                        TRACK_BOUNDS + tower_hitboxes
                    )
                    == -1
                ):

                    if placing_electric:
                        CLICK_SOUND.play()
                        placing_electric = False
                        towers.append(
                            tower.electric_tower(
                                (mx, my), pygame.Rect(mx - 13, my, 26, 21)
                            )
                        )
                        tower_hitboxes.append(pygame.Rect(mx - 13, my, 26, 21))

                    elif placing_ice:
                        CLICK_SOUND.play()
                        placing_ice = False
                        towers.append(
                            tower.ice_tower((mx, my), pygame.Rect(mx - 13, my, 26, 21))
                        )
                        tower_hitboxes.append(pygame.Rect(mx - 13, my, 26, 21))

                    elif placing_fire:
                        CLICK_SOUND.play()
                        placing_fire = False
                        towers.append(
                            tower.fire_tower((mx, my), pygame.Rect(mx - 13, my, 26, 21))
                        )
                        tower_hitboxes.append(pygame.Rect(mx - 13, my, 26, 21))

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        paused()

            if globs.player_health <= 0:
                end_game("lose")

            if replay:
                globs.clicked = False
                globs.player_cash = 450
                globs.player_health = 200
                return

            # wave handling


            if WAVES_COMBINED[counter] == "n":
                counter += 1
            elif WAVES_COMBINED[counter] == "w":
                if len(enemies) == 0:
                    text_width, text_height = MEDIUM_FONT.size("I I")
                    waiting = True
            else:
                enemies.append(enemy.AI(WAVES_COMBINED[counter]))
                counter += 1

            # draw background

            screen.fill((255, 255, 255))
            screen.blit(globs.BACKGROUND, (0, 0))

            # drawing the menu bar
            menu_bar = pygame.Rect(0, 0, SCREEN_WIDTH, 55)
            pygame.draw.rect(screen, (1, 50, 24), menu_bar)  # colour of menu_bar

            text_width, text_height = MEDIUM_FONT.size("I I")
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
                MEDIUM_FONT,
                paused,
            )

            # drawing stuff while next wave incoming

            if waiting:
                if not placing_electric and not placing_fire and not placing_ice:
                    button(
                        "",
                        (SCREEN_WIDTH - 2 * text_width - 200 + 60),
                        0,
                        (text_width + 60),
                        55,
                        (170, 221, 119),
                        (252, 244, 230),
                        (SCREEN_WIDTH - 2 * text_width - 80 + 60),
                        8,
                        MEDIUM_FONT,
                        next_wave,
                    )
                else:
                    button(
                        "",
                        (SCREEN_WIDTH - 2 * text_width - 200 + 60),
                        0,
                        (text_width + 60),
                        55,
                        (170, 221, 119),
                        (252, 244, 230),
                        (SCREEN_WIDTH - 2 * text_width - 80 + 60),
                        8,
                        MEDIUM_FONT,
                    )

                pygame.draw.polygon(
                    screen,
                    (252, 244, 230),
                    [
                        (
                            (SCREEN_WIDTH - 2 * text_width - 180 + 70),
                            (55 - text_height),
                        ),
                        (
                            (SCREEN_WIDTH - 2 * text_width - 180 + 70),
                            55 - (55 - text_height),
                        ),
                        ((SCREEN_WIDTH - text_width - 180 + 70), 27),
                    ],
                )

                if globs.player_cash < globs.ICE_COST:
                    pygame.draw.rect(screen, (226, 54, 54), (340, 5, 80, 45), 3)
                    pygame.draw.line(screen, (226, 54, 54), (340, 5), (420, 50), 3)
                    pygame.draw.line(screen, (226, 54, 54), (340, 50), (420, 5), 3)
                elif not placing_ice and not placing_electric and not placing_fire:
                    button(
                        "", 340, 5, 80, 45, (1, 50, 24), 0, 0, 0, FONT, new_ice_tower
                    )

                if globs.player_cash < globs.FIRE_COST:
                    pygame.draw.rect(screen, (226, 54, 54), (440, 5, 80, 45), 3)
                    pygame.draw.line(screen, (226, 54, 54), (440, 5), (520, 50), 3)
                    pygame.draw.line(screen, (226, 54, 54), (440, 50), (520, 5), 3)
                elif not placing_ice and not placing_electric and not placing_fire:
                    button(
                        "", 440, 5, 80, 45, (1, 50, 24), 0, 0, 0, FONT, new_fire_tower
                    )

                if globs.player_cash < globs.ELECTRIC_COST:
                    pygame.draw.rect(screen, (226, 54, 54), (540, 5, 80, 45), 3)
                    pygame.draw.line(screen, (226, 54, 54), (540, 5), (620, 50), 3)
                    pygame.draw.line(screen, (226, 54, 54), (540, 50), (620, 5), 3)
                elif not placing_ice and not placing_electric and not placing_fire:
                    button(
                        "",
                        540,
                        5,
                        80,
                        45,
                        (1, 50, 24),
                        0,
                        0,
                        0,
                        FONT,
                        new_electric_tower,
                    )

                screen.blit(globs.ICE_SPRITE, ((350), (55 - text_height)))

                screen.blit(globs.FIRE_SPRITE, ((450), (55 - text_height)))

                screen.blit(globs.ELECTRIC_SPRITE, ((550), (55 - text_height)))

                text_height, text_width = SMALL_FONT.size("200")
                draw_text(
                    str(globs.ICE_COST),
                    SMALL_FONT,
                    (235, 191, 107),
                    screen,
                    380,
                    (54 - text_height) / 2,
                )  
                draw_text(
                    str(globs.FIRE_COST),
                    SMALL_FONT,
                    (235, 191, 107),
                    screen,
                    480,
                    (54 - text_height) / 2,
                )  
                draw_text(
                    str(globs.ELECTRIC_COST),
                    SMALL_FONT,
                    (235, 191, 107),
                    screen,
                    580,
                    (54 - text_height) / 2,
                )  
                if placing_ice:
                    screen.blit(globs.ICE_SPRITE, (mx - 16, my - 11))

                elif placing_electric:
                    screen.blit(globs.ELECTRIC_SPRITE, (mx - 16, my - 11))

                elif placing_fire:
                    screen.blit(globs.FIRE_SPRITE, (mx - 16, my - 11))

            # drawing player health and player currency
            screen.blit(globs.coin, (45, 19))
            text_width, text_height = FONT.size(str(globs.player_cash))
            draw_text(
                str(globs.player_cash),
                FONT,
                (235, 191, 107),
                screen,
                75,
                (54 - text_height) / 2,
            )

            screen.blit(globs.heart, (150, 19))
            text_width, text_height = FONT.size(str(globs.player_health))
            draw_text(
                str(globs.player_health),
                FONT,
                (235, 191, 107),
                screen,
                180,
                (54 - text_height) / 2,
            )

            text_width, text_height = FONT.size(str(wave_num))
            draw_text(
                str(str(wave_num) + "/20"),
                FONT,
                (235, 191, 107),
                screen,
                260,
                (54 - text_height) / 2,
            )

            # enemy culling
            enemies[:] = [enemy for enemy in enemies if enemy.alive]

            enemies.sort(key=lambda e: len(e.path), reverse=True) # enemy sorting

            for e in enemies: # enemy updating and drawing
                e.update()
                if e.type == "s":
                    screen.blit(
                        pygame.transform.rotate(globs.SLIME_FRAMES[e.frame], e.angle),
                        (e.x - 32, e.y - 32),
                    )
                elif e.type == "c":
                    screen.blit(
                        pygame.transform.rotate(globs.CRAB_FRAMES[e.frame], e.angle),
                        (e.x - 16, e.y - 16),
                    )
                else:
                    screen.blit(
                        pygame.transform.rotate(globs.PYTHON_FRAMES[e.frame], e.angle),
                        (e.x - 16, e.y - 16),
                    )
            for t in towers:
                t.update(enemies)

            if waiting: # draw upgrade buttons if available
                if globs.player_cash >= 100:
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
                                    t.level_up,
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

            pygame.display.flip() # update screen   

            globs.CLOCK.tick(60) # set fps to 60

    play_game() # start game
