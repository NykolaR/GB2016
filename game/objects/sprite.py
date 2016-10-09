# sprite.py
# handles sprite memory

import pygame
from display import displayConstants

debug = True

loaded = []

screen = pygame.display.set_mode (displayConstants.size)

def clear ():
    screen.fill (displayConstants.palette [3])

def flip ():
    pygame.display.flip ()

def loadSprite (name, index):
    tempFile = open (name) # open file
    dat = tempFile.readlines () [index]
    if debug:
        print ("dat: " + str (dat))
    loadDat = []

    for num in dat:
        if num.isdigit (): loadDat.append (int (num))
    
    loaded.append (loadDat)
    tempFile.close () # close file
    if debug:
        print ("Texture loaded index: " + str (len(loaded) - 1))

    return len(loaded) - 1

def drawSprite (spriteIndex, position, pal, frame):
    count = frame * 64 # 8x8 tile = 64 pixels over
    for y in range (0, 8):
        for x in range (0, 8):
            if loaded [spriteIndex][count] <= 2: # if 3, is transparent pixel
                screen.set_at ((position[0] + x, position [1] + y), getColor (pal, loaded [spriteIndex][count]))
            count += 1

def drawSpriteToned (spriteIndex, position, pal, frame, tone):
    count = frame * 64 # 8x8 tile = 64 pixels over
    for y in range (0, 8):
        for x in range (0, 8):
            if loaded [spriteIndex][count] + tone <= 2: # if 3, is transparent pixel
                screen.set_at ((position[0] + x, position [1] + y), getColor (pal, loaded [spriteIndex][count] + tone))
            count += 1


def getColor (palette, index):
        return displayConstants.paletteS1 [index]

