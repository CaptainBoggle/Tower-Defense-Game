import pygame, sys
mainClock = pygame.time.Clock()
from pygame.locals import *

pygame.init()
from textRenderer import *

pygame.display.set_caption("Game base")

click = False

def main_menu(toggleMenu):
  while True:
    screen.fill((4, 67, 40))

    text_width, text_height = contrastMedFont.size("Main Menu")
    draw_text("Main Menu", contrastMedFont, (252, 244, 230), screen, (SCREEN_WIDTH/2 - text_width/2), 120)
    
    text_width, text_height = medFont.size("Main Menu")
    draw_text("Main Menu", medFont, (235, 191, 107), screen, (SCREEN_WIDTH/2 - text_width/2), 120)

    text_width, text_height = contrastLrgFont.size("CASTLE DEFENCE")
    draw_text("CASTLE DEFENCE", contrastLrgFont, (244, 197, 113), screen, (SCREEN_WIDTH/2 - text_width/2), 37)

    text_width, text_height = lrgFont.size("CASTLE DEFENCE")
    draw_text("CASTLE DEFENCE", lrgFont, (252, 247, 239), screen, (SCREEN_WIDTH/2 - text_width/2), 40)

    mx, my = pygame.mouse.get_pos()

    button_1 = pygame.Rect((SCREEN_WIDTH/2 - 100), 190, 200, 70)
    button_2 = pygame.Rect((SCREEN_WIDTH/2 - 100), 290, 200, 60)
    

    if button_1.collidepoint((mx, my)): # when they are pressed
      if click:
        toggleMenu(False) #run game
    if button_2.collidepoint((mx, my)):
      if click:
        quit() #quit game

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
          click = True #signals the button press

    pygame.display.update()
    mainClock.tick(60)


def game():
  click = False
  running = True
  while running:
    showMenu = False
    # break
    screen.fill((145, 202, 120)) #clear the screen

    menuBar = pygame.Rect(0, 0, SCREEN_WIDTH, 60)
    pygame.draw.rect(screen, (28, 73, 49), menuBar) # colour of menuBar 

    text_width, text_height = font.size("MENU")

    menuButton = pygame.Rect((SCREEN_WIDTH - text_width - 80), 0, (text_width + 80), 60)
    pygame.draw.rect(screen, (235, 191, 107), menuButton) # colour of menuButton
    
    mx, my = pygame.mouse.get_pos()
    if menuButton.collidepoint((mx, my)): # if menu button is pressed
      if click:
        main_menu()

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
    
    pygame.display.update()
    mainClock.tick(60)

  # return
def quit():
  pygame.quit()
  sys.exit()

# main_menu()