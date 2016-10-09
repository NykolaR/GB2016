import objects
from objects import gameobject
from objects import inputhandler

class Runner:
    def __init__ (self):
        self.score = 0
        self.highscore = 0
        
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
        self.playerBullets = []
        self.enemyBullets = []
        self.enemies = []
        self.barriers = []
        self.vitals = []
        self.resetGame ()

    def update (self):

        gameobject.Enemy.animationUpdate ()
        gameobject.Enemy.actionUpdate ()

        if inputhandler.keyPressed (2): # Fire
            if len (self.playerBullets) < 3:
                b = gameobject.Bullet ()
                b.set (self.player.position [0], self.player.position [1], -5)
                self.playerBullets.append (b)

        for enemy in self.enemies:
            enemy.update ()
            if not enemy.alive:
                self.enemies.remove (enemy)

        for barrier in self.barriers:
            barrier.update ()
            if not barrier.alive:
                self.barriers.remove (barrier)

        for pBullet in self.playerBullets:
            pBullet.update ()
            for enemy in self.enemies:
                if pBullet.alive and enemy.bulletCollision (pBullet):
                    pBullet.alive = False
            if not pBullet.alive:
                self.playerBullets.remove (pBullet)

            for barrier in self.barriers:
                if barrier.bulletCollision (pBullet) and pBullet.alive:
                    self.enemyBullets.append (pBullet)
                    pBullet.invertSpeed ()
                    pBullet.alive = False
            if not pBullet.alive:
                pBullet.alive = True

        for eBullet in self.enemyBullets:
            eBullet.update ()
            if eBullet.alive and self.player.bulletCollision (eBullet):
                eBullet.alive = False
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
        # Reset player
        self.player.reset ()

        # Reset score
        self.score = 0
        
        # Reset lists
        self.playerBullets = []
        self.enemyBullets = []
        self.enemies = []

        for i in range (2):
            e = gameobject.Scroller ()
            e.set (16 + i * 16, 32, 3)
            self.enemies.append (e)
        for i in range (2):
            e = gameobject.Brick ()
            e.set (16 + i * 32, 8, 3)
            self.barriers.append (e)

    def gameOver (self):
        return not (self.player.alive)
