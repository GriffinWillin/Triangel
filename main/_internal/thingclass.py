### general game object class
# Griffin Willingham 2024
from Constants import GoodStuff
import random, pygame, os


class Groups:
    ### all sprite
    allsprites = pygame.sprite.Group() # used for rendering every drawn object
    ### enemies
    enemies = pygame.sprite.Group() #
    ### bullet group                ##### isolates these for collision/updating
    bulls = pygame.sprite.Group()   #
    ### effect group
    fx = pygame.sprite.Group() # used to isolate effect objects for updating
                               # this is a seperate layer to avoid collision checks on fx
    ### background group
    bg = pygame.sprite.Group() # seperate layer to be rendered beneath others

### general thing class
class Thing:
    def __init__(self, health:int=1):
        self.xpos = GoodStuff.WIDTH/2 # x position
        self.ypos = GoodStuff.HEIGHT/2 # y position
        self.xvel = 0 # x velocity
        self.yvel = 0 # y velocity
        self.health = health # how many hits the thing can take
        self.friction = .8 # more slippery the closer to 1

        self.surf = None # rendered sprite
        self.mask = None # collision mask
        self.item = False # sets if the thing can be "collected" (IE, healthpack)
        self.firecool = 0 # limits fire rate 

    ### acc/mut
    ### xpos
    @property
    def xpos(self):
        return self._xpos
    
    @xpos.setter
    def xpos(self, val:float):
        self._xpos = round(val,2) ### this is here to deal with floating point imprecision

    ### ypos
    @property
    def ypos(self):
        return self._ypos
    
    @ypos.setter
    def ypos(self, val:float):
        self._ypos = round(val,2)

    ### xvel
    @property
    def xvel(self):
        return self._xvel
    
    @xvel.setter
    def xvel(self,val:float):
        if(abs(val)<.01):
            self._xvel = 0 # same as noted above
        else:
            self._xvel = round(val,4) # for here too

    ### yvel
    @property
    def yvel(self):
        return self._yvel
    
    @yvel.setter
    def yvel(self, val:float):
        if(abs(val)<.01):
            self._yvel = 0
        else:
            self._yvel = round(val,4)

    ### health
    @property
    def health(self):
        return self._health
    
    @health.setter # if health hits 0, activate kablamo
    def health(self, val):
        if(val <= 0):
            self.kablamo()
        self._health = val

    ### movement functions
    ### update position and apply friction
    def newpos(self):
        self.xpos += self.xvel
        self.ypos += self.yvel
        self.xvel *= self.friction
        self.yvel *= self.friction

    ### impart instantenous velocity in the x direction
    def ximpulse(self, direction:int, force:int):
        self.xvel += ((force/4)*direction)

    ### ^^^ but for y
    def yimpulse(self, direction:int, force:int):
        self.yvel += ((force/4)*direction)

    ### misc functions
    ### returns position as tuple; for drawing
    def myPos(self)->tuple:
        # self.xpos and self.ypos represent center values; this function needs to return
        # x and y of top left
        # x of top left = (x of center - (x size/2))
        # y of top left = (y of center - (y size/2))

        outx = self.xpos - (25/2)
        outy = self.ypos - (25/2)
        return (outx, outy)
    
    ### detecting a hit
    def injure(self):
        self.health -= 1
        
    ### death sequence
    def kablamo(self):
        self.kill()

    ### mainly for debug
    def __str__(self) -> str:
        return(f"{self.xpos}, {self.ypos}: {self.xvel}, {self.yvel}")
    