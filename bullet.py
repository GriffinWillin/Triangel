### projectile/bullet class
# Griffin Willingham 2024

from Constants import GoodStuff
from thingclass import Thing, Groups
from sound import SoundGuy
from effect import Burst
import pygame

# helpful for orientation checking
def sign(value:int)->int:
    if(value >0 ):
        return 1
    elif(value < 0):
        return -1
    else:
        return 0

class Bullet(Thing, pygame.sprite.Sprite):
    def __init__(self, spawn_x:float, spawn_y:float, initial_vel:int, accel:int):
        Thing.__init__(self, 1)
        pygame.sprite.Sprite.__init__(self)
        self.accel = accel  # how quickly bullet accelerates 
        self.initial_vel = initial_vel # inital velocity and direction
        self.yvel = initial_vel
        self.xpos = spawn_x + (1*sign(initial_vel))
        self.ypos = spawn_y + (25*sign(initial_vel))
        self.friction = .99
        self.fromplay = False
        

        ### flips sprite and sets player/enemy flag (as well as fire noise)
        if(self.initial_vel < 0):
            self.surf = (GoodStuff.P_BUL)
            self.fromplay = True
            
        else:
            self.surf = (pygame.transform.flip(GoodStuff.P_BUL,False,True))
            self.fromplay = False

        self.mask = pygame.mask.from_surface(GoodStuff.P_BUL)

    def update(self):
        self.newpos()
        self.yimpulse(-sign(self.initial_vel),self.accel)
        # check if bullet is onscreen still
        if(self.ypos < -25 or self.ypos > GoodStuff.HEIGHT+25):
            self.kill()

    ## override kablamo function to switch to an explosion frame
    def kablamo(self):
        for x in range(15):
            spark = Burst(self.xpos,self.ypos,20,2)
            Groups.fx.add(spark)
            Groups.allsprites.add(spark)
        self.kill()