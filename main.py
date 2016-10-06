import sys, pygame # imports
import game # my import
from game import objects
pygame.init ()

# This is the main program that runs the game
# It manages the game loop, as well as the game state
# I haven't used Python in quite some time, so go easy on me
# Written for: GBJam, Itch.io
# By: NykolaR

#ball = pygame.image.load ("ball.bmp")
#ballrect = ball.get_rect ()

clock = pygame.time.Clock ()
running = True
logging = False

player = objects.gameobject.Player ()

objects.sprite.loadSprite ("game/resources/char.hex", 0)

while running:
    for event in pygame.event.get ():
        if event.type == pygame.QUIT: running = False # Exit game

    clock.tick_busy_loop (60)
    if logging: print (clock.get_fps ())
    #ballrect = ballrect.move (speed)
    #if ballrect.left < 0 or ballrect.right > width:
    #    speed [0] = -speed [0]
    #if ballrect.top < 0 or ballrect.bottom > height:
    #    speed [1] = -speed [1]

    #screen.fill (palette[3])
    objects.sprite.clear ()
    player.update ()
    objects.sprite.flip ()
    #screen.blit (ball, ballrect)
    #pygame.display.flip ()

pygame.quit ()
