# object.py
# Object class contains a rectangle and sprite information

import pygame
import sprite
import inputhandler
from display import displayConstants


class GameObject:
    """
    object
    - Contains sprite data, and a rectangle
    - Methods: draw
    """
    def __init__ (self):
        self.spriteData = 0 # location of first pixel
        self.position = [16, 16] # x, y
        self.palette = 0
        self.frame = 0

    def draw (self):
        sprite.drawSprite (self.spriteData, self.position, self.palette, self.frame);

class PhysicalObject (GameObject):
    """
    - Methods: update, collision
    """
    def __init__ (self):
        GameObject.__init__ (self)
        self.alive = True

    def update (self):
        pass

    def collision (self, other):
        pass

    def bulletCollision (self, other):
        pass

    def overlap (one, two):
        """
        Return true if two objects overlap each other
        """
        return (two.position [0] > one.position [0] and two.position [0] < one.position [0] + 8) and (two.position [1] > one.position [1] and two.position [1] < one.position [1] + 8)
        

class Player (PhysicalObject):
    """
    player
    - Contains: Health
    - Overwrides: update
    """
    dashTime = 15
    animationSpeed = 10
    shadowSpeed = 7

    def __init__ (self):
        PhysicalObject.__init__ (self)
        self.spriteData = sprite.loadSprite ("game/resources/char.hex", 0)
        self.initialHealth = 3
        self.dash = 0
        self.shadow = 0
        self.shadowPos = [0, 0]
        self.animationCounter = 0
        self.shadowCounter = 0
        self.health = self.initialHealth

    def update (self):
        if inputhandler.key (0): #LEFT
            self.position [0] -= 2
        if inputhandler.key (1): #RIGHT
            self.position [0] += 2

        if inputhandler.keyPressed (0):
            if self.dash != 0:
                self.shadowPos [0] = self.position [0]
                self.shadowPos [1] = self.position [1]
                self.position [0] -= 24
                self.dash = 0
                self.shadow = self.health
            else:
                self.dash = Player.dashTime

        if inputhandler.keyPressed (1):
            if self.dash != 0:
                self.shadowPos [0] = self.position [0]
                self.shadowPos [1] = self.position [1]
                self.position [0] += 24
                self.dash = 0
                self.shadow = self.health
            else:
                self.dash = Player.dashTime

        self.dash -= 1
        if (self.dash < 0):
            self.dash = 0
        
        
        self.horiLimits ()

        self.shadowCounter += 1

        if self.shadowCounter == Player.shadowSpeed:
            self.shadow -= 1
            if (self.shadow < 0):
                self.shadow = 0
            self.shadowCounter = 0
        
        self.animationCounter += 1

        if self.animationCounter == Player.animationSpeed:
            if self.frame == 0:
                self.frame = 1
            else:
                self.frame = 0
            self.animationCounter = 0

        self.draw ()

    def collision (self, other):
        pass

    def bulletCollision (self, other):
        if PhysicalObject.overlap (self, other):
            self.health -= 1
            if self.health < 1:
                self.alive = False

            return True
        return False

    def horiLimits (self):
        if self.position [0] < 0: # off screen to left
            self.position [0] = 0 # hug left
        if self.position [0] > displayConstants.width - 8: # off right
            self.position [0] = displayConstants.width - 8 # hug

    def reset (self):
        self.health = self.initialHealth
        self.position [0] = 9 * 8 + 4
        self.position [1] = 16 * 8
        self.alive = True

    def draw (self):
        if self.shadow > 0:
            sprite.drawSpriteToned (self.spriteData, self.shadowPos, self.palette, self.frame, 3 - self.shadow)
        sprite.drawSprite (self.spriteData, self.position, self.palette, self.frame)


class Bullet (PhysicalObject):
    bulletFrame = 0
    bulletSprite = sprite.loadSprite ("game/resources/bullet.hex", 0)
    def __init__ (self):
        PhysicalObject.__init__ (self)
        self.vSpeed = 0

    def update (self):
        self.position [1] += self.vSpeed
        self.draw ()

        if (self.position [1] < -8) | (self.position [1] > displayConstants.height + 8):
            self.alive = False

    def set (self, x, y, vSpeed):
        self.position [0] = x
        self.position [1] = y
        self.vSpeed = vSpeed

    def draw (self):
        sprite.drawSprite (Bullet.bulletSprite, self.position, self.palette, Bullet.bulletFrame);

