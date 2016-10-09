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

    @staticmethod
    def overlap (one, two):
        """
        Return true if two objects overlap each other
        """
        return (one.position [0] < two.position [0] + 8 and one.position [0] + 8 > two.position [0] and one.position [1] < two.position [1] + 8 and one.position [1] + 8 > two.position [1])

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
        sprite.drawSpriteToned (self.spriteData, self.position, self.palette, self.frame, self.initialHealth - self.health)


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

    def invertSpeed (self):
        self.vSpeed *= -1
        self.vSpeed -= 2

    def set (self, x, y, vSpeed):
        self.position [0] = x
        self.position [1] = y
        self.vSpeed = vSpeed

    def draw (self):
        sprite.drawSprite (Bullet.bulletSprite, self.position, self.palette, Bullet.bulletFrame)

class Enemy (PhysicalObject):

    frame = 0
    animationSpeed = 10
    animationCount = 0
    actSpeed = 120
    actCount = 0
    
    @staticmethod
    def animationUpdate ():
        Enemy.animationCount += 1
        if Enemy.animationCount >= Enemy.animationSpeed:
            Enemy.animationCount = 0
            if Enemy.frame == 0:
                Enemy.frame = 1
            else:
                Enemy.frame = 0

    @staticmethod
    def actionUpdate ():
        Enemy.actCount += 1
        if Enemy.actCount > Enemy.actSpeed:
            Enemy.actCount = 0

    @staticmethod
    def act ():
        if Enemy.actCount == Enemy.actSpeed:
            return True
        return False

    def __init__ (self):
        PhysicalObject.__init__ (self)
        self.health = 1
        self.score = 100

    def set (self, x, y, health, score):
        self.position [0] = x
        self.position [1] = y
        self.health = health
        self.score = score

    def setAlive (self):
        if self.health <= 0:
            self.alive = False


class Alien (Enemy):

    alienSprite = sprite.loadSprite ("game/resources/alien.hex", 0)

    def __init__ (self):
        Enemy.__init__ (self)
        self.direction = False # Left

    def setDirection (self, direction):
        self.direction = direction

    def draw (self):
        sprite.drawSpriteToned (Alien.alienSprite, self.position, self.palette, Enemy.frame, 3 - self.health)

    def loop (self):
        if self.position [0] < 0:
            self.position [0] = displayConstants.width - 8
        if self.position [0] >= displayConstants.width:
            self.position [0] = 0

    def bulletCollision (self, other):
        if PhysicalObject.overlap (self, other):
            self.health -= 1
            return True
        return False

class Looper (Alien):
    def __init__ (self):
        Alien.__init__ (self)

    def update (self):
        if Enemy.act ():
            if self.direction:
                self.position [0] += 8
            else:
                self.position [0] -= 8

            self.loop ()
        self.draw ()

        self.setAlive ()

class Flipper (Alien):
    def _init__ (self):
        Alien.__init__ (self)

    def update (self):
        if Enemy.act ():
            if self.direction:
                self.position [0] += 8
            else:
                self.position [0] -= 8

            if self.position [0] < 0:
                self.position [0] += 16
                self.direction = not self.direction
            if self.position [0] >= displayConstants.width:
                self.position [0] -= 16
                self.direction = not self.direction
        self.draw ()
        self.setAlive ()

class Brick (Enemy):

    brickSprite = sprite.loadSprite ("game/resources/alien.hex", 1)

    def __init__ (self):
        Enemy.__init__ (self)

    def bulletCollision (self, other):
        if PhysicalObject.overlap (self, other):
            self.health -= 1
            return True
        return False

    def update (self):
        self.draw ()
        self.setAlive ()

    def draw (self):
        sprite.drawSpriteToned (Brick.brickSprite, self.position, self.palette, 0, 3 - self.health)

