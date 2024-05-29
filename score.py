### scorekeeping/HUD class and menu class
# Griffin Willingham 2024
import pygame
from Constants import Colors

# serves as scorekeeper. Holds score value and renders the HUD, which has health and score
class ScoreGuy:

    def __init__(self):
        pygame.font.init()
        self.disp = pygame.font.Font(pygame.font.match_font('consolas',True), 24) # load up the font object
        self.score = 0


    ### add score to the current game
    def addScore(self, value:int):
        if(value>0):
            self.score += value

    ### display score
    def display(self, health:int = -1) -> list:
        output = []
        score = (f"SCORE  : {self.score:06d}")
        health = (f"HEALTH : {health}")
        output.append(self.disp.render(score, False, Colors.WHITE))
        output.append(self.disp.render(health, False, Colors.WHITE))
        return output
    
    ### inform the player they are, in fact, not on the mortal plane
    def death(self) -> list:
        output = []
        score = (f"YOU HAVE DIED")
        health =(f"  PRESS ESC  ")
        output.append(self.disp.render(score, False, Colors.WHITE))
        output.append(self.disp.render(health, False, Colors.WHITE))
        return output
    
    ### display starting message
    def startmessage(self) -> pygame.font.Font:
        output = ("PRESS ANY KEY TO BEGIN")
        return self.disp.render(output, False, Colors.WHITE)

    ### dump score/health to terminal, for debug purposes
    def __str__(self)-> str:
        return (f"SCORE: {self.score:06d}")
    
