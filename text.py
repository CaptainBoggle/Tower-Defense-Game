import pygame
import globs

screen = globs.SCREEN
SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()

pygame.font.init()


SMALL_FONT = pygame.font.Font("retro.ttf", 25)
FONT = pygame.font.Font("retro.ttf", 35)
MEDIUM_FONT = pygame.font.Font("retro.ttf", 50)
LARGE_FONT = pygame.font.Font("retro.ttf", 80)
CONTRAST_MEDIUM_FONT = pygame.font.Font("retro.ttf", 51)
CONTRAST_LARGE_FONT = pygame.font.Font("retro.ttf", 83)

INFO_FONT = pygame.font.Font("data-latin.ttf",18)


def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)
