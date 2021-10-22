import os
import sys
import __main__
import pygame

#sys.path.insert(0, os.path.dirname(os.path.realpath(__main__.__file__)) + "\Screens")
#sys.path.insert(0, os.path.dirname(os.path.realpath(__main__.__file__)) + "\Classes")

#from Screen import Screen
#from Temp import drawTemp
#from Town import drawTown
#from Player import Player

#! SCREENS
# temp = Screen("Temp", drawTemp)
# town = Screen("Town", drawTown)

# temp.defineSideScreens({"left": None, "right": town})
# town.defineSideScreens({"left": temp, "right": None})

#! CURRENT SCREEN
#currentScreen = temp

#! WIDTH AND HEIGHT
WIDTH, HEIGTH = 800, 480 

#! ORIGINAL WINDOW
GWIN = pygame.display.set_mode(( WIDTH, HEIGTH ))

#! PLAYER INSTANCE
# player = Player() 
# temp.definePlayer(player)
# town.definePlayer(player)

#! FRAMES PER SECOND
FPS = 60

#! PYGAME CLOCK
clock = pygame.time.Clock()