# sprite.py
# handles sprite memory

import pygame
from display import displayConstants

cameraPos = 0, 0
loaded = []

screen = pygame.display.set_mode (displayConstants.size)

def clear ():
    screen.fill (displayConstants.palette [3])

def flip ():
    pygame.display.flip ()

def loadSprite (name, index):
    tempFile = open (name) # open file
    dat = tempFile.readlines () [index]
    print ("dat: " + dat)
    loadDat = []

    for num in dat:
        if num.isdigit (): loadDat.append (int (num))
    
    loaded.append (loadDat)
    tempFile.close () # close the file

def drawSprite (spriteIndex, position, pal):
    #for x in range (0, 32):
    #    for y in range (0, 32):
    #        screen.set_at ( (x, y), (255, 255, 255))
    count = 0
    for x in range (0, 8):
        for y in range (0, 8):
            screen.set_at ((position[0] + cameraPos [0] + x, position [1] + cameraPos [1] + y), getColor (pal, loaded [spriteIndex][count]))
            count += 1

def getColor (palette, index):
        return displayConstants.paletteS1 [index]

