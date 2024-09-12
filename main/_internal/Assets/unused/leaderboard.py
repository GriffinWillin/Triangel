# for testing out leaderboard functionality
import os, random

names = [
    "ALE",
    "BET",
    "CAT",
    "DAR",
    "EGG",
    "FAT",
    "GOR",
    "HIT",
    "IOU",
    "JAZ",
    "KIK",
    "LOL"
]

file = open(os.path.join("leaderboard.txt"),"r+")

class LeaderboardEntry:
    def __init__(self, name:str, score:int):
        self.name = name
        self.score = score

    ##### acc/mut
    ### name

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self,value:str):
        if(len(value) != 3):
            self._name = "ERR"
        else:
            self._name = value.upper()

    ### score

    @property
    def score(self) -> int:
        return self._score
    
    @score.setter
    def score(self,value:int):
        if(value<0):
            self._score = 0
        else:
            self._score = value

    ### get entry
    def getThis(self) -> tuple:
        return(self.name,self.score)
    
    ### str
    def __str__(self):
        return(f"{self.name} | {self.score:06d}\n")
    
    ### comparators
    def __gt__(self,other)-> bool:
        return (self.score > other.score)
    def __lt__(self,other)-> bool:
        return (self.score < other.score)
    
class Leaderboard:
    def __init__(self):
        self.current_board = []
    
    def addEntry(self, name:str = "N/A", score:int = 0):
        K = LeaderboardEntry(name,score)
        self.current_board.append(K)

    def order(self):
        self.current_board.sort(reverse = True)

    def loadFromFile(self, source = file): # fills out current_board from given source file
        from_file = source.readlines()
        for line in from_file:
            name = (line.split(" | "))[0]
            score = (line.split(" | "))[1]
            score = int(score.replace("\n",""))
            self.addEntry(name,score)

    def present(self)-> list: # arranges and returns the current scoreboard as a list
        self.order()
        board_str = []
        for entry in self.current_board:
            if(len(board_str)<10):
                new = str(entry)
                board_str.append(new)

        return board_str

    def overwriteFile(self, dest = file):
        #update file
        dest.writelines(self.present())

    def displayToTerminal(self): #prints the current-board as terminal text, for debug

        for entry in self.present():
            print(entry.replace("\n",""))
        
        print("")

########
