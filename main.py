import sys, pygame # imports
import game # my import
from game import objects
pygame.init ()

# This is the main program that runs the game
# It manages the game loop, as well as the game state
# I haven't used Python in quite some time, so go easy on me
# Written for: GBJam, Itch.io
# By: NykolaR

clock = pygame.time.Clock ()
running = True
logging = False

state = True # False, main, True, running

runner = game.gamerunner.Runner ()
runner.resetGame ()

def resetGame ():
    runner.resetGame ()

def runGame ():
    runner.update ()

def mainMenu ():
    pass

resetGame ()

while running:
    objects.inputhandler.updateKeyboard ()
    for pyEvent in pygame.event.get ():
        if pyEvent.type == pygame.QUIT: running = False # Exit game
        else:
            objects.inputhandler.handle (pyEvent)

    clock.tick_busy_loop (60)
    if logging: print (clock.get_fps ())

    objects.sprite.clear ()
    if state:
        runner.update ()
        if runner.gameOver ():
            runner.resetGame ()
            state = False
    else:
        pass
    objects.sprite.flip ()

pygame.quit ()
