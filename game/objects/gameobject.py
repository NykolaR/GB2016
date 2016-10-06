# object.py
# Object class contains a rectangle and sprite information

import sprite

class GameObject:
    """
    object
    - Contains sprite data, and a rectangle
    - Methods: draw
    """
    def __init__ (self):
        self.spriteData = 0 # location of first pixel
        self.position = 0, 0 # x, y
        self.palette = 0

    def draw (self):
        sprite.drawSprite (self.spriteData, self.position, self.palette);

class PhysicalObject (GameObject):
    """
    - Methods: update, collision
    """
    def __init__ (self):
        GameObject.__init__ (self)
    def update (self):
        pass
    def collision (self, other):
        pass

class Player (PhysicalObject):
    """
    player
    - Contains: Health
    - Overwrides: update
    """

    def __init__ (self):
        PhysicalObject.__init__ (self)

    def update (self):
        #self.position [0] += 0
        self.draw ()

    def collision (self, other):
        #self.position [0] += 0
        pass

