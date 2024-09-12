### visual effect classes
# Griffin Willingham 2024

from Constants import GoodStuff
from thingclass import Thing
import pygame, random

# Burst; fireworks-like explosion effect for added visual feedback
class Burst(Thing, pygame.sprite.Sprite):
    def __init__(self, spawn_x, spawn_y, power, lifetime):
        Thing.__init__(self, 1)
        pygame.sprite.Sprite.__init__(self)
        self.xpos = spawn_x
        self.ypos = spawn_y
        # power determines "spread", or more literally movement speed
        self.xvel = (random.randint(-1*power,power))
        self.yvel = (random.randint(-1*power,power))
        # lifetime measures how long the effect is rendered
        self.age = 0
        self.lifetime = lifetime

        self.friction = .995
        self.surf = random.choice([GoodStuff.P_BUL_EX,GoodStuff.P_BUL_EX2])
        # no mask because Burst has no collision

    
    def update(self):
        if(self.age <= self.lifetime):
            self.newpos()
            self.age += 1
        else:
            self.injure()

# scrolling white specks in the background; does nothing but appear at the top
# and floatdownwards until it disappears
class Stars(Thing, pygame.sprite.Sprite):
    def __init__(self):
        Thing.__init__(self, 1)
        pygame.sprite.Sprite.__init__(self)
        self.xpos = (random.randint(0,GoodStuff.WIDTH))
        self.ypos = -5
        self.speed = (random.randint(7,15))

        self.friction = 1
        self.surf = GoodStuff.STAR

    def update(self):
        self.yvel = self.speed
        self.newpos()
        if(self.ypos > GoodStuff.HEIGHT):
            self.injure()
        