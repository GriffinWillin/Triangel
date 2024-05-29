### enemy classes & healthpack class
# Griffin Willingham 2024

import pygame, math
from random import randint
from Constants import GoodStuff
from thingclass import Thing, Groups
from bullet import Bullet
from effect import Burst
from score import ScoreGuy
from sound import SoundGuy


#### Enemy classes

### mine. Teal circle that spawns at a given xpos and accelerates slowly downward
### deployed in random clouds or formation
class Mine(Thing, pygame.sprite.Sprite):
    def __init__(self, startx:int, scorekeeper:ScoreGuy, health:int = 2):
        pygame.sprite.Sprite.__init__(self)
        Thing.__init__(self,health)
        self.xpos = startx
        self.ypos = -25
        self.friction = .95
        self.scorekeeper = scorekeeper # the scoreguy that this enemies' points should go to

        self.surf = GoodStuff.MINE
        self.mask = pygame.mask.from_surface(GoodStuff.MINE)

    @property
    def xpos(self):
        return self._xpos
    
    @xpos.setter
    def xpos(self, val):
        if(val>GoodStuff.WIDTH):
            self._xpos = GoodStuff.WIDTH
        elif(val<0):
            self._xpos = 0
        else:
            self._xpos = val

    ### misc functions
    ### needs to accelerate downwards
    def update(self):
        self.yimpulse(1,2)
        if(self.ypos > GoodStuff.HEIGHT+25):
            self.kill()
        self.newpos()

    ### enemy recoils when hit
    def injure(self):
        SoundGuy.playThis(self, GoodStuff.NME_HIT)
        self.xvel += randint(-5,5)
        self.yvel += randint(-5,-2)
        self.health -= 1

    ### makes death explosion
    def kablamo(self):
        for x in range(15):
            spark = Burst(self.xpos,self.ypos,15,15)
            Groups.fx.add(spark)
            Groups.allsprites.add(spark)
        SoundGuy.playThis(self, GoodStuff.NME_DED)
        self.scorekeeper.addScore(50)
        self.kill()

### Defender. Blue square that spawns at a given xpos and moves slowly downward
### fires randomly
class Defender(Thing, pygame.sprite.Sprite):
    def __init__(self, startx:int, scorekeeper:ScoreGuy, health:int = 3):
        pygame.sprite.Sprite.__init__(self)
        Thing.__init__(self,health)
        self.xpos = startx
        self.ypos = -25
        self.scorekeeper = scorekeeper
        
        self.surf = GoodStuff.DEFN
        self.mask = pygame.mask.from_surface(GoodStuff.DEFN)
    
    @property
    def xpos(self):
        return self._xpos
    
    @xpos.setter
    def xpos(self, val):
        if(val>GoodStuff.WIDTH):
            self._xpos = GoodStuff.WIDTH
        elif(val<0):
            self._xpos = 0
        else:
            self._xpos = val

    # misc functions
    ### moves downwards at a constant speed, shoots randomly
    def update(self):
        # controls movement and off-screen disappearance
        self.yvel = 4 
        if(self.ypos > GoodStuff.HEIGHT+25):
            self.kill()
        self.newpos()
        # firing
        should = randint(0,100)
        if(should % 12 == 0):
            self.shoot()
        if(self.firecool > 0):
            self.firecool -= 1

    def shoot(self):
        if(self.firecool == 0):
            self.firecool = 20
            newBull = Bullet((self.xpos+randint(-2,2)),self.ypos,15,-1)
            Groups.bulls.add(newBull)
            Groups.allsprites.add(newBull)

    ### enemy recoils when hit
    def injure(self):
        SoundGuy.playThis(self, GoodStuff.NME_HIT)
        self.xvel += randint(-5,5)
        self.yvel += randint(-5,-2)
        self.health -= 1

    # makes death explosion
    def kablamo(self):
        for x in range(15):
            spark = Burst(self.xpos,self.ypos,15,15)
            Groups.fx.add(spark)
            Groups.allsprites.add(spark)
        SoundGuy.playThis(self, GoodStuff.NME_DED)
        self.scorekeeper.addScore(150)
        self.kill()

    

### Wave. Pink ice-cream cone shaped thing that moves L/R in a semichaotic wave
### as it moves downwards. Fires randomly.
class Wave(Thing, pygame.sprite.Sprite):
    def __init__(self, startx:int, scorekeeper:ScoreGuy, health:int = 4):
        pygame.sprite.Sprite.__init__(self)
        Thing.__init__(self,health)
        self.xpos = startx
        self.ypos = -25
        self.scorekeeper = scorekeeper
        
        self.surf = GoodStuff.WAVE
        self.mask = pygame.mask.from_surface(GoodStuff.WAVE)
    
    # acc/mut
    @property
    def xpos(self):
        return self._xpos
    
    @xpos.setter
    def xpos(self, val):
        if(val>GoodStuff.WIDTH):
            self._xpos = GoodStuff.WIDTH
        elif(val<0):
            self._xpos = 0
        else:
            self._xpos = val

    def update(self):
        # move downwards constantly at constant rate
        self.yvel = 7
        # weird sine wave thing (?)
        self.xvel += (math.sin(self.ypos*.025)*5)
        if(self.ypos > GoodStuff.HEIGHT+25):
            self.kill()
        self.newpos( )

        # firing
        should = randint(0,100)
        if(should % 25 == 0):
            self.shoot()
        if(self.firecool > 0):
            self.firecool -= 1

    ### shooting!
    def shoot(self):
        if(self.firecool == 0):
            self.firecool = 20
            newBull = Bullet((self.xpos+randint(-2,2)),self.ypos,15,-1)
            Groups.bulls.add(newBull)
            Groups.allsprites.add(newBull)

    ### enemy recoils when hit
    def injure(self):
        SoundGuy.playThis(self, GoodStuff.NME_HIT)
        self.xvel += randint(-5,5)
        self.yvel += randint(-5,-2)
        self.health -= 1

    # makes death explosion
    def kablamo(self):
        for x in range(15):
            spark = Burst(self.xpos,self.ypos,15,15)
            Groups.fx.add(spark)
            Groups.allsprites.add(spark)
        SoundGuy.playThis(self, GoodStuff.NME_DED)
        self.scorekeeper.addScore(300)
        self.kill()
        
#### HEALTH PACK
###  identical in behavior to mine, but moves slower, cannot be destroyed
#    heals player when touched
class HPack(Thing, pygame.sprite.Sprite):
    def __init__(self, startx:int, scorekeeper:ScoreGuy, health:int = 1):
        pygame.sprite.Sprite.__init__(self)
        Thing.__init__(self,health)
        self.xpos = startx
        self.ypos = -25
        self.friction = .95
        self.scorekeeper = scorekeeper 

        self.item = True

        self.surf = GoodStuff.MEDKIT
        self.mask = pygame.mask.from_surface(GoodStuff.MEDKIT)

    @property
    def xpos(self):
        return self._xpos
    
    @xpos.setter
    def xpos(self, val):
        if(val>GoodStuff.WIDTH):
            self._xpos = GoodStuff.WIDTH
        elif(val<0):
            self._xpos = 0
        else:
            self._xpos = val

    # misc functions
    ### needs to accelerate downwards
    def update(self):
        self.yimpulse(1,1)
        if(self.ypos > GoodStuff.HEIGHT+25):
            self.kill()
        self.newpos()

    ### makes death explosion
    def kablamo(self):
        for x in range(15):
            spark = Burst(self.xpos,self.ypos,5,15)
            Groups.fx.add(spark)
            Groups.allsprites.add(spark)
        SoundGuy.playThis(self, GoodStuff.HLTHPAK)
        self.scorekeeper.addScore(150)
        self.kill()
####
# ideas for more enemy types
# - Seeker that takes in the player's xpos as a parameter of its update() and attempts to
#   lock onto and rapidly accelerate into the player; weak but fast
# - Teaser that hovers near the top of the screen and moves back and forth, shooting incessantly
#   it would be rare but tanky and super annoying; double width so it's easier to hit at least
# - Frag mines; normal mines, but when destroyed they fling out indestructable, 
#   smaller enemies that can hit the player at high velocity, possibly other enemies(?)
# - Cosine wave; the same as the Wave but is moves across the screen rather than down it... lol
# - Evader is a variant of Defender (or Seeker?) that takes in the xpos and ypos of the nearest
#   player bullet and attempts to dodge it, shoots rapidly; weak but annoying

###
# ideas for more powerups
# - invulnerability; says it on the tin
# - fire-rate booster
# - peircing bullets (they are invulnerable and so aren't destroyed when hitting a target)
# - explosive bullets (not sure about this one. Could employ a variant of the Burst class?)