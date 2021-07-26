import pygame
import globs
screen = globs.screen
SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.get_surface().get_size()

font = pygame.font.Font("retro.ttf", 35)
medFont = pygame.font.Font("retro.ttf", 50)
lrgFont = pygame.font.Font("retro.ttf", 80)
contrastMedFont = pygame.font.Font("retro.ttf", 51)
contrastLrgFont = pygame.font.Font("retro.ttf", 83)

def draw_text(text, font, color, surface, x, y):
  textobj = font.render(text, 1, color)
  textrect = textobj.get_rect()
  textrect.topleft = (x, y)
  surface.blit(textobj, textrect)