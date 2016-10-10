import objects

class Main:
    def __init__ (self):
        self.fade = 0
        self.fadecount = 0
        self.faderate = 30
        self.fadecounter = 1

    def update (self):
        self.updateFade ()

        objects.sprite.drawLetters ((8 * 7, 8 * 8), 0, "HI5PACE", self.fade)

    def updateFade (self):
        self.fadecount += 1

        if self.fadecount == self.faderate:
            self.fade += self.fadecounter
            self.fadecount = 0

        if self.fade > 3:
            self.fade = 2
            self.fadecounter *= -1
            
        if self.fade < 0:
            self.fade = 0
            self.fadecounter *= -1


