import pygame, sys
from pygame.locals import *
from classes import *

# set up pygame
pygame.init()

screenDim = {'width':1200, 'height':700}

# set up the window
windowSurface = pygame.display.set_mode((screenDim['width'], screenDim['height']), 0, 32)


# draw the white background onto the surface
windowSurface.fill(Color(255, 255, 255))


###### CHANGE THIS TO MAKE TITLE SCREEN ################
# ENTER TITLE SCREEN
inTitle = 0  # Stay in the title screen until start clicked 
while inTitle == 1:  # Enter title screen

    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # CAN I MAKE ANIMATION WHERE CLICKED? EXTRA
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    for event in pygame.event.get():
        if event.type == pg.MOUSEBUTTONUP:
            mouse = pygame.mouse.get_pos()  # Get our mouse position

            if titlePos.collidepoint(mouse):
                inTitle = 0  # Exit loop when we click start

        if event.type == pygame.QUIT:  # Quit if we want to
            pygame.quit()


game = Game(windowSurface)




# draw the window onto the screen
pygame.display.update()

# run the game loop
while True:

    game.run()

    for event in pygame.event.get():

        game.player.move(event)

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
