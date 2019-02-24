import pygame, sys
from pygame.locals import *

# set up pygame
pygame.init()

screenDim = {'width':800, 'height':600}

# set up the window
windowSurface = pygame.display.set_mode((screenDim['width'], screenDim['height']))

from classes import *
clock = pygame.time.Clock()


# draw the white background onto the surface
windowSurface.fill(Color(255, 255, 255))


###### CHANGE THIS TO MAKE TITLE SCREEN ################
# ENTER TITLE SCREEN
inTitle = 0  # Stay in the title screen until start clicked 
while inTitle == 1:  # Enter title screen


    for event in pygame.event.get():
        if event.type == pg.MOUSEBUTTONUP:
            mouse = pygame.mouse.get_pos()  # Get our mouse position

            if titlePos.collidepoint(mouse):
                inTitle = 0  # Exit loop when we click start

        if event.type == pygame.QUIT:  # Quit if we want to
            pygame.quit()


game = Game(windowSurface)




# draw the window onto the screen
pygame.display.init()

# run the game loop
while True:

    game.run()
    clock.tick(60)

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
