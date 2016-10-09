###
# inputhandler
# handles game input
# currently only keyboard, can be extended
###

import pygame
import numpy

# General handling
class INPUT:
    KEY_DOWN, KEY_PRESSED = range (2)

class KEYS:
    LEFT, RIGHT, FIRE, NUMKEYS = range (4)

keys = numpy.zeros ( (2, KEYS.NUMKEYS), dtype = bool)

def handle (e):
    keyboardHandle (e)

def updateKeyboard ():
    for i in range (3):
        pressed (i)

def keyboardHandle (e):
    if e.type == pygame.KEYDOWN:
        if e.key == pygame.K_LEFT or e.key == pygame.K_a:
            setKey (KEYS.LEFT, True)
        if e.key == pygame.K_RIGHT or e.key == pygame.K_d:
            setKey (KEYS.RIGHT, True)
        if e.key == pygame.K_z or e.key == pygame.K_SPACE:
            setKey (KEYS.FIRE, True)
    if e.type == pygame.KEYUP:
        if e.key == pygame.K_LEFT or e.key == pygame.K_a:
            setKey (KEYS.LEFT, False)
        if e.key == pygame.K_RIGHT or e.key == pygame.K_d:
            setKey (KEYS.RIGHT, False)
        if e.key == pygame.K_z or e.key == pygame.K_SPACE:
            setKey (KEYS.FIRE, False)


def key (key):
    return keys [INPUT.KEY_DOWN][key]

def keyPressed (key):
    return keys [INPUT.KEY_PRESSED][key]

def pressed (key):
    if keys [INPUT.KEY_PRESSED][key]:
        keys [INPUT.KEY_PRESSED][key] = False
        return True
    return False

def setKey (key, value):
    if value:
        if keys [INPUT.KEY_DOWN][key]:
            # Input is being held
            keys [INPUT.KEY_PRESSED][key] = False
            keys [INPUT.KEY_DOWN][key] = True
        else:
            # This is the first frame it was pressed
            keys [INPUT.KEY_DOWN][key] = True
            keys [INPUT.KEY_PRESSED][key] = True
    else:
        # Not pressed
        keys [INPUT.KEY_DOWN][key] = False
        keys [INPUT.KEY_PRESSED][key] = False
