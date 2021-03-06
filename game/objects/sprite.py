# sprite.py
# handles sprite memory

import pygame
from display import displayConstants

debug = False

loaded = []

screen = pygame.display.set_mode (displayConstants.size)
pygame.display.set_caption ("HI SPACE")


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

numbersIndex = loadSprite ("game/resources/numbers.hex", 0)
lettersIndex = loadSprite ("game/resources/letters.hex", 0)

def drawSprite (spriteIndex, position, pal, frame):
    count = frame * 64 # 8x8 tile = 64 pixels over
    for y in range (0, 8):
        for x in range (0, 8):
            if loaded [spriteIndex][count] <= 2: # if 3, is transparent pixel
                screen.set_at ((position[0] + x, position [1] + y), getColor (pal, loaded [spriteIndex][count]))
            count += 1

def drawSpriteToned (spriteIndex, position, pal, frame, tone):
    if tone < 0:
        tone = 0
    count = frame * 64 # 8x8 tile = 64 pixels over
    for y in range (0, 8):
        for x in range (0, 8):
            if loaded [spriteIndex][count] + tone <= 2: # if 3, is transparent pixel
                screen.set_at ((position[0] + x, position [1] + y), getColor (pal, loaded [spriteIndex][count] + tone))
            count += 1

def drawNumber (position, pal, number):
    numString = str (number)
    count = 0
    for char in numString:
        drawSprite (numbersIndex, (position [0] + count * 8, position [1]), pal, int (char))
        count += 1

letters = {
        'H' : 0,
        'I' : 1,
        'P' : 2,
        'A' : 3,
        'C' : 4,
        'E' : 5
        }

def drawLetters (position, pal, string, fade):
    count = 0
    for char in string:
        if char.isdigit ():
            drawNumber ((position [0] + count * 8, position [1]), pal, int (char))
        else:
            drawSpriteToned (lettersIndex, (position [0] + count * 8, position [1]), pal, letters [char], fade)
        count += 1

def getColor (palette, index):
        return displayConstants.paletteS1 [index]

