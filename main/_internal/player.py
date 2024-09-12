### player class
# Griffin Willingham 2024

from Constants import GoodStuff
from thingclass import Thing, Groups
from bullet import Bullet
from effect import Burst
from random import randint
from sound import SoundGuy
import pygame, math

### the player class
class Me(Thing, pygame.sprite.Sprite):

    def __init__(self, health:int):
        pygame.sprite.Sprite.__init__(self)
        Thing.__init__(self,5)
        self.health = health
        self.surf = GoodStuff.PLAY
        self.friction = .9

        self.stunlock = 0 # used for I-frames/stunlock
        self.mask = pygame.mask.from_surface(GoodStuff.PLAY)

        # music (I couldn't find anywhere better to put it)
                           
    def update(self,keys,oomph:int):
        # control the player, if they are not stunlocked
        if(self.stunlock == 0):
            if(keys[GoodStuff.K_LEFT]):
                self.ximpulse(-1,oomph)
            if(keys[GoodStuff.K_RIGHT]):
                self.ximpulse(1,oomph)
            if(keys[GoodStuff.K_UP]):
                self.yimpulse(-1,oomph)
            if(keys[GoodStuff.K_DOWN]):
                self.yimpulse(1,oomph)

            # check for shootin'
            if(keys[GoodStuff.K_SPACE]):
                self.shoot()

            # normal friction:
            self.friction = .9
            # stop flashing
            self.surf.set_alpha(255)

        # update position
        self.newpos()

        # keep player onscreen 
        if(self.xpos < 0):
            self.xpos = 0
        if(self.xpos > GoodStuff.WIDTH):
            self.xpos = GoodStuff.WIDTH
        if(self.ypos <= 0):
            self.ypos = 0
        if(self.ypos >= GoodStuff.HEIGHT):
            self.ypos = GoodStuff.HEIGHT

        # update gun cooldown
        if(self.firecool>0):
            self.firecool -= 1

        # update stunlock timer, flash, and friction
        if(self.stunlock > 0):
            self.stunlock -= 1
            self.friction = .95
            self.surf.set_alpha((math.sin(self.stunlock))*255)

    ### handling shooting
    def shoot(self):
        if(self.firecool == 0):
            SoundGuy.playThis(self, GoodStuff.SHOOT)
            self.firecool = 5
            newBull = Bullet((self.xpos+randint(-2,2)),self.ypos,-15,-1)
            Groups.bulls.add(newBull)
            Groups.allsprites.add(newBull)

    ### when hit, player is stunlocked for a few seconds; during stunlock, the player is:
    ###     - the player input is halted temporarily
    ###     - transparency flash
    ###     - friction drops, causing the player to slide around
    ###     - the player is invulnerable
    
    def injure(self):
        if(self.stunlock == 0):
            self.stunlock = 30
            self.health -= 1
            SoundGuy.playThis(self,GoodStuff.NME_HIT)

    def healthup(self):
        self.health += 1

    ### death explosion
    def kablamo(self):
        for x in range(25):
            spark = Burst(self.xpos,self.ypos,15,25)
            Groups.fx.add(spark)
            Groups.allsprites.add(spark)
        SoundGuy.playThis(self,GoodStuff.PLAYDED)
        self.kill()

#### ideas for other mechanics
# - WASD control options; still space to shoot :P
# - "Dodge"; by pressing X (or Lshift for WASD) and then a direction the player rapidly
#   jolts in that direction by temporarily dropping friction an applying a large impulse
#   has a cooldown like shooting
# - Timer in the UI (Like classic Sonic)
# - 