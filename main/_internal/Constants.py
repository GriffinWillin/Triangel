### Constants, events, images
# Griffin Willingham 2024

# import libraries
import pygame, os, sys
from random import randint, choice

pygame.mixer.init()

## get directory
if (getattr(sys, 'frozen', False)):
    temp = sys._MEIPASS
else:
    temp = os.path.dirname(os.path.abspath(__file__))


working = os.path.join(temp,"Assets")

class Colors:
    # constants for colors
    RED = [0xeD, 0x1C, 0x24]
    BLUE = [0x3F,0x48,0xCC]
    TEAL = [0x28, 0xDA, 0xD6]
    PINK = [0xF3, 0x00, 0xE6]
    YELLOW = [0xFF, 0xF2, 0x00]

    WHITE = [0xFF, 0xFF, 0xFF]
    BLACK = [0x00, 0x00, 0x00]

    COLORS = [BLUE, RED, TEAL, PINK, YELLOW, WHITE, BLACK]

# i couldn't think of a better name :/
class GoodStuff:
    
    # other files
    #LEADER = open()

    # events
    NORMAL = pygame.USEREVENT + 1

    # images
    PLAY = pygame.image.load(os.path.join(working,"RedTri.png"))
    MINE = pygame.image.load(os.path.join(working,"TeaCir.png"))
    DEFN = pygame.image.load(os.path.join(working,"BluSqr.png"))
    WAVE = pygame.image.load(os.path.join(working,"PinWave.png"))
    P_BUL = pygame.image.load(os.path.join(working,"Bullet.png"))
    P_BUL_EX = pygame.image.load(os.path.join(working,"BullExp.png"))
    P_BUL_EX2 = pygame.image.load(os.path.join(working,"BullExp2.png"))
    MEDKIT = pygame.image.load(os.path.join(working,"Medkit.png"))
    LOGO = pygame.image.load(os.path.join(working,"logo.png"))
    STAR = pygame.image.load(os.path.join(working,"star.png"))

    # sounds
    SHOOT = pygame.mixer.Sound(os.path.join(working,"bullet.wav"))
    NME_HIT = pygame.mixer.Sound(os.path.join(working,"enemyhit.wav"))
    NME_DED = pygame.mixer.Sound(os.path.join(working,"enemydead.wav"))
    HLTHPAK = pygame.mixer.Sound(os.path.join(working,"healthpack.wav"))
    PLAYDED = pygame.mixer.Sound(os.path.join(working,"playerdead.wav"))

    SOUNDS = [SHOOT, NME_HIT,NME_DED,HLTHPAK,PLAYDED]
    for s in SOUNDS:
        s.set_volume(.6)

    # music

    DEMONS = os.path.join(working,"music.mp3")

    # constants for screen size
    WIDTH = 800
    HEIGHT = 800

    # keys from pygame
    from pygame.locals import (
        RLEACCEL,
        K_UP,
        K_DOWN,
        K_LEFT,
        K_RIGHT,
        K_ESCAPE,
        KEYDOWN,
        QUIT,
        K_SPACE,
    )