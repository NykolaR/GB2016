import objects
from objects import gameobject
from objects import inputhandler

class Runner:
    def __init__ (self):
        self.score = 0
        self.highscore = 0

        self.player = gameobject.Player ()
        self.playerBullets = []
        self.enemyBullets = []
        self.enemies = []
        self.resetGame ()

    def update (self):
        if inputhandler.keyPressed (2): # Fire
            b = gameobject.Bullet ()
            b.set (self.player.position [0], self.player.position [1], -5)
            self.playerBullets.append (b)

        for enemy in self.enemies:
            enemy.update ()
            if not enemy.alive:
                self.enemies.remove (enemy)

        for pBullet in self.playerBullets:
            pBullet.update ()
            for enemy in self.enemies:
                if enemy.bulletCollision (pBullet):
                    self.playerBullets.remove (pBullet)
            if not pBullet.alive:
                self.playerBullets.remove (pBullet)

        for eBullet in self.enemyBullets:
            eBullet.update ()
            if self.player.bulletCollision (eBullet):
                self.enemyBullets.remove (eBullet)
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


    def gameOver (self):
        return not (self.player.alive)
