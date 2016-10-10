import objects, pygame
from objects import gameobject
from objects import inputhandler

import random

class Runner:
    def __init__ (self):
        self.score = 0
        self.highscore = 0
        self.enemyROF = 2500
        self.defaultEnemyROF = 2500

        self.pshoot = pygame.mixer.Sound ("game/resources/sounds/pshoot.ogg")
        self.phit = pygame.mixer.Sound ("game/resources/sounds/phit.ogg")
        self.eshoot = pygame.mixer.Sound ("game/resources/sounds/eshoot.ogg")
        self.ehit = pygame.mixer.Sound ("game/resources/sounds/ehit.ogg")
        self.vhit = pygame.mixer.Sound ("game/resources/sounds/vhit.ogg")
        
        """
        Number of sprite objects:
        Player + Shadow = 2
        Player bullets = 2
        Enemy bullets = 10
        Enemies = 10
        HUD = 1 + 4 + 4 = 9
        Total = 34
        """
        self.player = gameobject.Player ()
        self.numBullets = 1
        self.playerBullets = []
        self.enemyBullets = []
        self.enemies = []
        self.barriers = []
        self.vitals = []
        self.board = 0

    def update (self):
        gameobject.Enemy.animationUpdate ()
        gameobject.Enemy.actionUpdate ()

        if gameobject.Enemy.bigAct ():
            for enemy in self.enemies:
                enemy.position [1] += 8
                if enemy.position [1] > 14 * 8:
                    self.player.alive = False
            for enemy in self.barriers:
                enemy.position [1] += 8
                if enemy.position [1] > 14 * 8:
                    self.player.alive = False
            for enemy in self.vitals:
                enemy.position [1] += 8
                if enemy.position [1] > 14 * 8:
                    self.player.alive = False
            gameobject.Enemy.bigActCount = 0

        if inputhandler.key (2): # Fire
            if len (self.playerBullets) < self.numBullets:
                b = gameobject.Bullet ()
                b.set (self.player.position [0], self.player.position [1], -3)
                self.playerBullets.append (b)
                self.pshoot.stop ()
                self.pshoot.play ()

        for enemy in self.enemies:
            enemy.update ()
            if not enemy.alive:
                self.score += enemy.score
                self.enemies.remove (enemy)
            else:
                if len (self.enemyBullets) <= 10 and random.randint (0, self.enemyROF) == 0:
                    b = gameobject.Bullet ()
                    b.set (enemy.position [0], enemy.position [1], 1)
                    self.enemyBullets.append (b)
                    self.eshoot.stop ()
                    self.eshoot.play ()

        for vital in self.vitals:
            vital.update ()
            if not vital.alive:
                self.score += vital.score
                self.vitals.remove (vital)

        if len (self.vitals) == 0:
            self.board += 1
            if self.enemyROF > 500:
                self.enemyROF -= 200
            gameobject.Enemy.difficultyIncrease ()
            self.player.health = self.player.initialHealth
            self.loadLevel ()

        for barrier in self.barriers:
            barrier.update ()
            if not barrier.alive:
                self.score += barrier.score
                self.barriers.remove (barrier)

        for pBullet in self.playerBullets:
            pBullet.update ()
            for enemy in self.enemies:
                if pBullet.alive and enemy.bulletCollision (pBullet):
                    pBullet.alive = False
                    self.ehit.stop ()
                    self.ehit.play ()
            if not pBullet.alive:
                self.playerBullets.remove (pBullet)

            for barrier in self.barriers:
                if barrier.bulletCollision (pBullet) and pBullet.alive:
                    self.enemyBullets.append (pBullet)
                    pBullet.invertSpeed ()
                    pBullet.alive = False
                    self.playerBullets.remove (pBullet)
                    self.ehit.stop ()
                    self.ehit.play ()
            if not pBullet.alive:
                pBullet.alive = True

            for vital in self.vitals:
                if vital.bulletCollision (pBullet) and pBullet.alive:
                    pBullet.alive = False
                    self.vhit.stop ()
                    self.vhit.play ()
            if not pBullet.alive:
                if self.playerBullets.count (pBullet) > 0:
                    self.playerBullets.remove (pBullet)

        for eBullet in self.enemyBullets:
            eBullet.update ()
            if eBullet.alive and self.player.bulletCollision (eBullet):
                eBullet.alive = False
                self.phit.stop ()
                self.phit.play ()
            if not eBullet.alive:
                self.enemyBullets.remove (eBullet)
        
        self.player.update ()

        if self.score > self.highscore:
            self.highscore = self.score

    def resetGame (self):
        """
        Resets player position,
        game score,
        and bullets/enemies
        """

        self.enemyROF = self.defaultEnemyROF

        # Reset player
        self.player.reset ()

        # Reset score
        self.score = 0
        
        # Reset lists
        self.playerBullets = []
        self.enemyBullets = []
        self.enemies = []

        self.board = 0

        self.loadLevel ()
        gameobject.Enemy.resetThings ()

    def gameOver (self):
        return not (self.player.alive)

    boards = {
            0 : "5.hex",
            1 : "4.hex",
            2 : "3.hex",
            3 : "2.hex",
            4 : "1.hex"
            }

    def loadLevel (self):
        loadBoard = self.boards [4 - (self.board % 5)] # file string
        boardLevel = self.board / 5 # Number of reps

        if loadBoard == 0 and boardLevel > 1: # score bonus, speed up
            self.score += 10000 * boardLevel

        """
        File legend:
        0 = add nothing
        1 = barrier (1 HP, 200pts)
        2 = barrier (2 HP, 400pts)
        3 = barrier (3 HP, 600pts)
        4 = looper (2 HP, 200pts, LEFT)
        5 = looper (2 HP, 200pts, RIGHT)
        6 = looper (3 HP, 300pts, LEFT)
        7 = looper (3 HP, 300pts, RIGHT)
        8 = flipper (2 HP, 200pts, LEFT)
        9 = flipper (2 HP, 200pts, RIGHT)
        A = flipper (3 HP, 300pts, LEFT)
        B = flipper (3 HP, 300pts, RIGHT)
        C = vitals (1 HP, 600pts)
        D = vitals (2 HP, 1200pts)
        E = vitals (3 HP, 2400pts)

        NOTE: All points multiplied by boardLevel + 1.
        All HP increased by boardLevel
        """

        self.enemies = []
        self.barriers = []
        self.vitals = []
        tempFile = open ("game/resources/boards/" + loadBoard) # open file
        dat = tempFile.readlines () [0]
        count = 0
        
        for num in dat:
            if num != '0':
                if num == '1' or num == '2' or num == '3':
                    self.addBarrier (num, count, False, boardLevel)
                if num=='4' or num=='5' or num=='6' or num=='7':
                    self.addLooper (num, count, boardLevel)
                if num=='8' or num=='9' or num=='A' or num=='B':
                    self.addFlipper (num, count, boardLevel)
                if num=='C' or num=='D' or num=='E':
                    self.addBarrier (num, count, True, boardLevel)
            count += 1

    def addBarrier (self, num, count, vitals, scale):
        e = gameobject.Brick ()
        e.set ((count % 20) * 8, (count / 20 + 2) * 8, self.hitPoints [num] + scale, self.scores [num] * (scale + 1))
        if vitals:
            self.vitals.append (e)
        else:
            self.barriers.append (e)

    def addFlipper (self, num, count, scale):
        e = gameobject.Flipper ()
        e.set ((count % 20) * 8, (count / 20 + 2) * 8, self.hitPoints [num] + scale, self.scores [num] * (scale + 1))
        if num=='9' or num=='B':
            e.direction = True
        self.enemies.append (e)

    def addLooper (self, num, count, scale):
        e = gameobject.Looper ()
        e.set ((count % 20) * 8, (count / 20 + 2) * 8, self.hitPoints [num] + scale, self.scores [num] * (scale + 1))
        if num=='5' or num=='7':
            e.direction = True
        self.enemies.append (e)


    scores = {
            '1' : 100,
            '2' : 200,
            '3' : 300,
            '4' : 100,
            '5' : 100,
            '6' : 150,
            '7' : 150,
            '8' : 100,
            '9' : 100,
            'A' : 150,
            'B' : 150,
            'C' : 250,
            'D' : 500,
            'E' : 1000
            }
     
    hitPoints = {
            '1' : 1,
            '2' : 2,
            '3' : 3,
            '4' : 2,
            '5' : 2,
            '6' : 3,
            '7' : 3,
            '8' : 2,
            '9' : 2,
            'A' : 3,
            'B' : 3,
            'C' : 1,
            'D' : 2,
            'E' : 3
            }

