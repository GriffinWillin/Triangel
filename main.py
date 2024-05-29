### TRIANGEL (formerly known as The Silly)
# MAIN GAME FILE
# Griffin Willingham, April 2024 (GTW 2024)

# imports
import pygame
from random import randint
from Constants import GoodStuff
from thingclass import Groups
from player import Me
from effect import Stars
from enemies import Mine, Defender, Wave, HPack
from score import ScoreGuy
from sound import SoundGuy

# initialize pygame, get everything goin'
pygame.init()
pygame.display.set_icon(GoodStuff.PLAY)
pygame.display.set_caption("Triangel")
screen = pygame.display.set_mode([GoodStuff.WIDTH,GoodStuff.HEIGHT])

clooc = pygame.time.Clock()

checkRate = 500
status = "going"

menu = True

# create scoreguy for font rendering
thisGame = ScoreGuy()

# menu loop
while(menu):
    # display logo
    screen.blit(GoodStuff.LOGO, (((GoodStuff.WIDTH/2)-403),((GoodStuff.HEIGHT/2)-203/2)))

    # display start message
    screen.blit(thisGame.startmessage(),(((GoodStuff.WIDTH/2)-286/2),600))
                
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # exit
            status = "out"
            menu = False
        if event.type == GoodStuff.KEYDOWN: # if literally any key is pressed, exit menu
            if(event.key == GoodStuff.K_ESCAPE): # or exit game if the key is ESC
                status = "out"
            menu = False

    pygame.display.flip()
    clooc.tick(32)

# enemy timer
pygame.time.set_timer(GoodStuff.NORMAL, checkRate)

### enemy spawn function
def spawn(enemytype):
    new = enemytype(randint(0, GoodStuff.WIDTH),thisGame)
    Groups.allsprites.add(new)
    Groups.enemies.add(new)

# create player
player = Me(5)
Groups.allsprites.add(player)



### Main game loop
while(status=="going"):
    # delete last frame
    screen.fill((0,0,0))

    # update game objects
    Groups.enemies.update()
    Groups.bulls.update()
    Groups.fx.update()
    Groups.bg.update()

    # check for enemy hits
    for enemy in Groups.enemies:

        #if player hits enemy (enemy - player)
        if (player.health > 0): # player has health 
            if player.mask.overlap(enemy.mask,(enemy.xpos - player.xpos, enemy.ypos - player.ypos)): # collision
                if(enemy.health > 0): # enemy has health
                    if(enemy.item == True): # Is tre "enemy" an item (healthpack)
                        player.healthup()
                    else:
                        player.injure() # take health from player
                    enemy.injure() # take health from enemy

        for bull in Groups.bulls: # check for bullet collisions (enemy - bullet)
            if (bull.health > 0 and (enemy.item == False) and  bull.fromplay): # make sure bullet is alive (O_o) and is from the player
                    # and also the enemy is not an item
                    if bull.mask.overlap(enemy.mask,(enemy.xpos - bull.xpos, enemy.ypos - bull.ypos)): # collision
                        if (enemy.health>0):
                            thisGame.addScore(15)
                            bull.injure()
                            enemy.injure()
    
    # check for hits on the player (bullet - player)
    for bull in Groups.bulls:
        if (bull.health>0 and bull.fromplay == False): # make sure bullet is alive (O_o) and is NOT from the player
            if bull.mask.overlap(player.mask,(player.xpos - bull.xpos, player.ypos - bull.ypos)):
                if(player.health > 0):
                    bull.injure()
                    player.injure()

    # check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # exit
            status = "out"
        elif event.type == GoodStuff.KEYDOWN: # also exit
            if(event.key == GoodStuff.K_ESCAPE):
                status = "out"
            if(menu):
                menu = False
    
        elif event.type == GoodStuff.NORMAL:     # normal gameplay
            spawn(Mine)                     # Spawn a new mine every 500 ms
            should = randint(0,20)          # roll for other enemy spawns

            if(thisGame.score > 1000 and thisGame.score < 4000): # wait until score is within 1000-3000
                ## Tier 2
                if(should % 20 == 0):       # 1/10 for spawning a Defender
                    spawn(Defender)
                elif(should == 7):          # 1/20 for spawning a Wave
                    spawn(Wave)

            elif(thisGame.score > 4000):    # wait until score exceeds 3000
                if(should % 2 == 0):        # spawn ANOTHER mine half the time
                    spawn(Mine)
                if(should % 6 == 0):        # 3/20 for spawning a Defender
                    spawn(Defender)
                elif(should % 10 == 0):     # 1/10 for spawning a Wave
                    spawn(Wave)
            
            should = randint(0,200)
            if(should == 30):
                spawn(HPack)
        
    # stars :D
    new = Stars()
    Groups.bg.add(new)
    
    
    # render bg
    for thing in Groups.bg:
        screen.blit(thing.surf, thing.myPos())

    # render everything else
    for thing in Groups.allsprites:
        screen.blit(thing.surf, thing.myPos())
    
    # render hud
    out = thisGame.display(player.health)
    screen.blit(out[0],(10,30))
    screen.blit(out[1], (10,50))

    # is player alive?
    if(player.health>0):
        pressedKeys = pygame.key.get_pressed()
        player.update(pressedKeys,6) # update player
    else: # player is dead
        out = thisGame.death() # call death text
        pygame.mixer.music.stop() # stop music
        screen.blit(out[0],(GoodStuff.WIDTH/2-(169/2), GoodStuff.HEIGHT/2)) # display death text
        screen.blit(out[1], (GoodStuff.WIDTH/2-(169/2), GoodStuff.HEIGHT/2 + 25))

    pygame.display.flip()
    clooc.tick(33) # lock FPS at 33 (so the game doesn't wet itself)

    #print(thisGame)

# exit game when loop breaks
pygame.quit()