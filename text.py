import pygame
import globs
import os

screen = globs.SCREEN # localise screen
SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size() # get screen sizes

pygame.font.init()  # initialise font engine

# load fonts
SMALL_FONT = pygame.font.Font(os.path.join("files","retro.ttf"), 25)
FONT = pygame.font.Font(os.path.join("files","retro.ttf"), 35)
MEDIUM_FONT = pygame.font.Font(os.path.join("files","retro.ttf"), 50)
LARGE_FONT = pygame.font.Font(os.path.join("files","retro.ttf"), 80)
CONTRAST_MEDIUM_FONT = pygame.font.Font(os.path.join("files","retro.ttf"), 51)
CONTRAST_LARGE_FONT = pygame.font.Font(os.path.join("files","retro.ttf"), 83)

INFO_FONT = pygame.font.Font(os.path.join("files","data-latin.ttf"), 18)


def draw_text(text, font, color, surface, x, y): # general text draw function
    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)
