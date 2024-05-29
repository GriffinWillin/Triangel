### sound controller
# Griffin Willingham 2024
import pygame, os
from Constants import GoodStuff

# controls the playback of sounds; compiled into one class so it doesn't have to be handled in every other one
class SoundGuy:
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load(os.path.join("Assets","music.mp3"), "mp3") # load up the music

    # quick way to handle playing sounds
    def playThis(self, Tound:pygame.mixer.Sound):
        if(Tound in GoodStuff.SOUNDS):
            Tound.play()
        else:
            print("That sound doesn't exist :3") # error handling
        
    def playMusic(self):
        pygame.mixer.music.play(-1)

thisNoise = SoundGuy() # this is what's playing the music
thisNoise.playMusic()