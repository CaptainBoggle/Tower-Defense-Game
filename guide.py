import pygame
import text
import globs


def showguide():
    global showing_guide
    showing_guide = True
    while showing_guide:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        globs.SCREEN.fill((4, 67, 40))

        SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()

        text_width, text_height = text.CONTRAST_MEDIUM_FONT.size("Guide")
        text.draw_text(
            "Guide",
            text.CONTRAST_MEDIUM_FONT,
            (235, 191, 107),
            globs.SCREEN,
            (SCREEN_WIDTH / 2 - text_width / 2),
            37,
        )
        text_width, text_height = text.MEDIUM_FONT.size("Guide")
        text.draw_text(
            "Guide",
            text.MEDIUM_FONT,
            (252, 244, 230),
            globs.SCREEN,
            (SCREEN_WIDTH / 2 - text_width / 2),
            37,
        )

        text_width, text_height = text.INFO_FONT.size(
            "AIM: Stop incoming AI from corrupting the system"
        )
        text.draw_text(
            "AIM: to stop incoming AI from corrupting the system",
            text.INFO_FONT,
            (235, 191, 107),
            globs.SCREEN,
            (SCREEN_WIDTH / 2 - text_width / 2),
            110,
        )

        text_width, text_height = text.INFO_FONT.size(
            "Place towers on the map by clicking once to select, and once more to place down. This will cost money as indicated next to the icons."
        )
        text.draw_text(
            "Place towers on the map by clicking once to select, and once more to place down. This will cost money as indicated next to the icons.",
            text.INFO_FONT,
            (252, 244, 230),
            globs.SCREEN,
            (SCREEN_WIDTH / 2 - text_width / 2),
            160,
        )

        text_width, text_height = text.INFO_FONT.size(
            "The three towers are ice, fire, and electric. The ice tower slows all enemies in range, the fire tower burns multiple enemies at once, and the electric tower shoots slowly with high damage."
        )
        text.draw_text(
            "The three towers are ice, fire, and electric. The ice tower slows all enemies in range, the fire tower burns multiple enemies at once, and the electric tower shoots slowly with high damage.",
            text.INFO_FONT,
            (252, 244, 230),
            globs.SCREEN,
            (SCREEN_WIDTH / 2 - text_width / 2),
            200,
        )

        text_width, text_height = text.INFO_FONT.size(
            "Placed towers with an orange up-arrow on them can be upgraded for 100 coins by clicking on the arrow. Upgrading a tower will boost almost all aspects of it!"
        )
        text.draw_text(
            "Placed towers with an orange up-arrow on them can be upgraded for 100 coins by clicking on the arrow. Upgrading a tower will boost almost all aspects of it!",
            text.INFO_FONT,
            (252, 244, 230),
            globs.SCREEN,
            (SCREEN_WIDTH / 2 - text_width / 2),
            240,
        )

        text_width, text_height = text.INFO_FONT.size(
            "Once you are happy with your defence, press the orange play icon in the top right. This will give you a nice cash injection, but also send enemies through the circuit."
        )
        text.draw_text(
            "Once you are happy with your defence, press the orange play icon in the top right. This will give you a nice cash injection, but also send enemies through the circuit. Remember, you cannot place or upgrade towers during a wave!",
            text.INFO_FONT,
            (252, 244, 230),
            globs.SCREEN,
            (SCREEN_WIDTH / 2 - text_width / 2),
            280,
        )

        text_width, text_height = text.INFO_FONT.size(
            "To win the game, survive all 20 waves. The three types of enemy you will see are the slime, the python, and the crab. The slime is the basic enemy, the python is weaker but fast, and the crab is stronger but slow."
        )
        text.draw_text(
            "To win the game, survive all 20 waves. The three types of enemy you will see are the slime, the python, and the crab. The slime is the basic enemy, the python is weaker but fast, and the crab is stronger but slow.",
            text.INFO_FONT,
            (252, 244, 230),
            globs.SCREEN,
            (SCREEN_WIDTH / 2 - text_width / 2),
            320,
        )

        text_width, text_height = text.INFO_FONT.size(
            "If an enemy manages to get through, you will lose lives. The amount of lives lost is equal to the amount of health the enemy had left. Once your lives reach zero, you lose!"
        )
        text.draw_text(
            "If an enemy manages to get through, you will lose lives. The amount of lives lost is equal to the amount of health the enemy had left. Once your lives reach zero, you lose!",
            text.INFO_FONT,
            (252, 244, 230),
            globs.SCREEN,
            (SCREEN_WIDTH / 2 - text_width / 2),
            360,
        )

        pygame.display.update()
        globs.CLOCK.tick(60)
