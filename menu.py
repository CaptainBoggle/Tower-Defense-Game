import pygame, sys
mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
from textRenderer import *

pygame.display.set_caption("Game base")

click = False

def main_menu(toggleMenu):
  click = False
  while True:
    screen.fill((4, 67, 40))

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

    if button_1.collidepoint((mx, my)): # when they are pressed
      if click:
        toggleMenu(False) #run game
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
          pygame.quit()
          sys.exit()

      if event.type == MOUSEBUTTONDOWN:
        if event.button == 1:
          click = True # signals the button press

    pygame.display.update()
    mainClock.tick(60)