### Constants, events, images
# Griffin Willingham 2024

# import libraries
import pygame, os
from random import randint, choice

pygame.mixer.init()

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
    PLAY = pygame.image.load(os.path.join("Assets","RedTri.png"))
    MINE = pygame.image.load(os.path.join("Assets","TeaCir.png"))
    DEFN = pygame.image.load(os.path.join("Assets","BluSqr.png"))
    WAVE = pygame.image.load(os.path.join("Assets","PinWave.png"))
    P_BUL = pygame.image.load(os.path.join("Assets","Bullet.png"))
    P_BUL_EX = pygame.image.load(os.path.join("Assets","BullExp.png"))
    P_BUL_EX2 = pygame.image.load(os.path.join("Assets","BullExp2.png"))
    MEDKIT = pygame.image.load(os.path.join("Assets","Medkit.png"))
    LOGO = pygame.image.load(os.path.join("Assets","logo.png"))
    STAR = pygame.image.load(os.path.join("Assets","star.png"))

    # sounds
    SHOOT = pygame.mixer.Sound(os.path.join("Assets","bullet.wav"))
    NME_HIT = pygame.mixer.Sound(os.path.join("Assets","enemyhit.wav"))
    NME_DED = pygame.mixer.Sound(os.path.join("Assets","enemydead.wav"))
    HLTHPAK = pygame.mixer.Sound(os.path.join("Assets","healthpack.wav"))
    PLAYDED = pygame.mixer.Sound(os.path.join("Assets","playerdead.wav"))

    SOUNDS = [SHOOT, NME_HIT,NME_DED,HLTHPAK,PLAYDED]
    for s in SOUNDS:
        s.set_volume(.6)

    # music

    DEMONS = os.path.join("Assets","music.mp3")

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