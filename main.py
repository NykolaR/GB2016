import sys, pygame # imports
import game # my import
from game import objects
import game.objects.display
pygame.init ()

# This is the main program that runs the game
# It manages the game loop, as well as the game state
# I haven't used Python in quite some time, so go easy on me
# Written for: GBJam, Itch.io
# By: NykolaR

clock = pygame.time.Clock ()
running = True
logging = False

state = False # False, main, True, running

pygame.mixer.music.load ("game/resources/sounds/title.ogg")
pygame.mixer.music.play ()


runner = game.gamerunner.Runner ()
runner.resetGame ()
mainmenu = game.mainmenu.Main ()

def resetGame ():
    runner.resetGame ()

def runGame ():
    runner.update ()

def updateFade ():
    fadecount += 1

def mainMenu ():
    mainmenu.update ()

def displayHUD ():
    objects.sprite.drawNumber ((0, 0), 0, runner.score)
    objects.sprite.drawNumber ((8 * 11, 0), 0, runner.highscore)

#runner.resetGame ()

framestochangecolor = 120

pal = 0

while running:
    objects.inputhandler.updateKeyboard ()
    for pyEvent in pygame.event.get ():
        if pyEvent.type == pygame.QUIT: running = False # Exit game
        else:
            objects.inputhandler.handle (pyEvent)
    pygame.display.update ()

    if framestochangecolor > 0:
        framestochangecolor -= 1
        if objects.inputhandler.keyPressed (0):
            pal += 1
        if objects.inputhandler.keyPressed (1):
            pal += 2
        if objects.inputhandler.keyPressed (2):
            pal += 3
        if pal > 8:
            pal = 0
        game.objects.display.displayConstants.setPalette (pal)


    clock.tick_busy_loop (60)
    if logging: print (clock.get_fps ())

    objects.sprite.clear ()
    if state:
        runner.update ()
        if runner.gameOver ():
            #runner.resetGame ()
            state = False
    else:
        mainMenu ()
        if  framestochangecolor <= 0 and objects.inputhandler.keyPressed (2): # Fire
            state = True
            runner.resetGame ()
    displayHUD ()
    objects.sprite.flip ()

pygame.quit ()
