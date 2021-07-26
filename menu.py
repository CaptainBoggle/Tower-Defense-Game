import pygame, sys, os
mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
from textRenderer import *

transparentOverlay = pygame.image.load(os.path.join("mapideas", "dgBackground.png"))
# transparentOverlay.set_alpha(128)

def blit_alpha(target, source, location, opacity):
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (0, 0))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)
    target.blit(temp, location)

click = False

def main_menu(toggleMenu, menuOpenCount):
  click = False

  if menuOpenCount <= 1:
    screen.fill((4, 67, 40))
  else:
    blit_alpha(screen, transparentOverlay, (0, 0), 128)

  while True:

    text_width, text_height = contrastMedFont.size("Main Menu")
    draw_text("Main Menu", contrastMedFont, (252, 244, 230), screen, (SCREEN_WIDTH/2 - text_width/2), 120)
    
    text_width, text_height = medFont.size("Main Menu")
    draw_text("Main Menu", medFont, (235, 191, 107), screen, (SCREEN_WIDTH/2 - text_width/2), 120)

    text_width, text_height = contrastLrgFont.size("A.I. DEFENCE")
    draw_text("A.I. DEFENCE", contrastLrgFont, (244, 197, 113), screen, (SCREEN_WIDTH/2 - text_width/2), 37)

    text_width, text_height = lrgFont.size("A.I. DEFENCE")
    draw_text("A.I. DEFENCE", lrgFont, (252, 247, 239), screen, (SCREEN_WIDTH/2 - text_width/2), 40)

    mx, my = pygame.mouse.get_pos()

    button_1 = pygame.Rect((SCREEN_WIDTH/2 - 100), 190, 200, 70)
    button_2 = pygame.Rect((SCREEN_WIDTH/2 - 100), 290, 200, 60)

    if button_1.collidepoint((mx, my)): # when buttons are pressed
      if click:
        toggleMenu(False, menuOpenCount) #run game
    if button_2.collidepoint((mx, my)):
      if click:
        quit() # quit game

    pygame.draw.rect(screen, (129, 185, 62), button_1) # colour of buttons 
    text_width, text_height = font.size("PLAY")
    draw_text("PLAY", font, (254, 244, 228), screen, (SCREEN_WIDTH/2 - text_width/2), 209)

    pygame.draw.rect(screen, (71, 126, 47), button_2)
    text_width, text_height = font.size("QUIT")
    draw_text("QUIT", font, (254, 244, 228), screen, (SCREEN_WIDTH/2 - text_width/2), 304)

    click = False
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      
      if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
          if menuOpenCount > 1:
            toggleMenu(False, menuOpenCount) #return to game if game is paused
          else:
            pygame.quit()
            sys.exit()

      if event.type == MOUSEBUTTONDOWN:
        if event.button == 1:
          click = True # signals the button press

    pygame.display.update()
    mainClock.tick(60)