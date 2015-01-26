
print("booting...")

############################################################################################################################
#                                                                                                                          #
#                                             Diggo v.1.6.9                                                             #
#                   A Python made, minecraft like, pygame picture maker made to help teach code!                           #
#                                                                                                                          #
############################################################################################################################

#How To Craft:

#To Craft press '/'
#Than Type '/craft<object>'

#TNT = 8 coal 1 lava

#Warning! Game may crash when using TNT! To prevent crashing put on Lag-Safe or do NOT use TNT!

#1.4.7 to 1.6.9

#THE BIGGEST UPDATE EVER!
 
#TNT
#Crafting
#Read 'Read Me.txt' on the shell or terminal
#Beter Looking Folder
#Texture Packs
#Minecraft Mode (May Lag because of Picture)
#music
#Drop Blocks By pressing MODE + <NUMBER BLOCK>
#Lag-Safe Mode (This is for people with Lots of Lag when playing this game, this mode takes Lagmaking stuff off like mine-
#craft mode and TNT!)
#door module added
#new command /reset
#Greeting if new user
#Clouds
#Bird
#Pytcraft Runner For Windows v2

from door import *
read()
from random import *#Random (Again)
import pygame#Pygame our main GUI
from pygame.locals import *#Pygame Locals
from PyLaunch1000 import *

#Version Number
version = '1.6.9'

#List of Modules (or Mods)
mods = ["pygame","sys","random","tkinter","dumbmenu","time","door"]


#Our Clock
fpsClock = pygame.time.Clock()


#Here is our resources
DIRT = 0
GRASS = 1
WATER = 2
COAL = 3
LAVA = 4
TNT = 5
CLOUD = 6#Ignore

#Rainbow of Colors
red   = 255,  0,  0
green =   0,255,  0
blue  =   0,  0,255
BLACK = (0,0,0)
BROWN = (153,76,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

colours = {#Old version Ignore
    DIRT : BROWN,
    GRASS : GREEN,
    WATER : BLUE,
    COAL : BLACK
    }

inventory = {
    #Numbers of how much you have in inventory
    DIRT : 0,
    GRASS : 0,
    WATER : 0,
    LAVA : 0,
    TNT : 0,
    COAL : 0
    }

TILESIZE = 30#Tilesize do not change game may Crash

def lagfree():
    
    import sys#sys stands for system
    import random#Our random Generater
    import dumbmenu as dm#The Menu
    import time#Do I have to explain it?
    import os#os checks if your os is compatible
    from os.path import exists
    
    DIRTT = 'Pics/dirt.png'
    GRASSS = 'Pics/grass.png'
    WATERR = 'Pics/water.png'
    COALL = 'Pics/coal.png'
    LAVAA = 'Pics/lava.png'
    TNTT = 'Pics/tnt.png'
    print('')
    
    if (exists(TNTT) == False):
        TNTT = 'Pics/texturenotfound.png'
    if (exists(LAVAA) == False):
        LAVAA = 'Pics/texturenotfound.png'
    if (exists(COALL) == False):
        COALL = 'Pics/texturenotfound.png'
    if (exists(WATERR) == False):
        WATERR = 'Pics/texturenotfound.png'
    if (GRASSS == "skip"):
        GRASSS = 'Pics/grass.png'
    if (exists(DIRTT) == False):
        DIRTT = 'Pics/texturenotfound.png'
    textures = {#YAY PICTURES!
        DIRT : pygame.image.load(DIRTT),
        GRASS : pygame.image.load(GRASSS),
        WATER : pygame.image.load(WATERR),
        COAL : pygame.image.load(COALL),
        LAVA : pygame.image.load(LAVAA),
        TNT : pygame.image.load(TNTT),
        CLOUD : pygame.image.load('Pics/cloud.png')
        }

    DEBUG = False

    #Starts Pygame
    pygame.init()
    
    #Size of screen
    size = width, height = 340,240
    #The Screen
    screen = pygame.display.set_mode(size)
    #The Screen Background
    screen.fill(blue)
    #Updates Display
    pygame.display.update()
    pygame.key.set_repeat(500,30)
    #Title
    pygame.display.set_caption('Pytcraft 2D')
    #Icon
    pygame.display.set_icon(pygame.image.load('Pics/Logo.png'))
    #THE MENU
    choose = dm.dumbmenu(screen, [
                        'Start Game',
                        
                        'QUIT'], 64,64,None,32,1.4,green,red)
    
    
    if choose == 1:
        #Quits Game
            pygame.quit()
            sys.exit()
            return
    if choose == 0:
        #Quits Menu
        pygame.quit()
        #Input
        
        MAPWIDTH = int(input("Put in width put 0 to set it to normal!"))

        if (MAPWIDTH == 0):
            MAPWIDTH = 20

       #Input
        MAPHEIGHT = int(input("Put in height put 0 to set it to normal!"))

        if (MAPHEIGHT == 0):
            MAPHEIGHT = 20

        #All Resources
        resources = [DIRT,GRASS,WATER,COAL,LAVA,TNT]
        #Tilemap
        tilemap = [[DIRT for w in range(MAPWIDTH)]for h in range(MAPHEIGHT)]
        #Starts Pygame (Again)
        pygame.init()

        #Display Stuff
        DISPLAYSURF = pygame.display.set_mode((MAPWIDTH * TILESIZE,MAPHEIGHT * TILESIZE + 50))
        INVFONT = pygame.font.Font(pygame.font.get_default_font(),18)
        PLAYER = pygame.image.load('Pics/player.png').convert_alpha()
        playerPos = [0,0]

        #Continued...
        pygame.display.set_caption('Pytcraft 2D')
        pygame.display.set_icon(pygame.image.load('Pics/Logo.png'))

        pygame.joystick.init()
        joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
        
        #Random seed Generater
        for rw in range(MAPHEIGHT):
            for cl in range(MAPWIDTH):
                print("Getting Random Stuff")
                randomnumber = randint(0,15)
                if (randomnumber == 0):
                    tile = COAL
                    print("COAL")
                elif (randomnumber == 1 or randomnumber == 2):
                    tile = WATER
                    print("WATER")
                elif (randomnumber >= 1 and randomnumber <= 7):
                    tile = GRASS
                    print("GRASS")
                elif (randomnumber >= 8 and randomnumber <= 9):
                    tile = LAVA
                    print("LAVA")
                else:
                    tile = DIRT
                    print("DIRT")
                tilemap[rw][cl] = tile
        music = pygame.mixer.music.load('Music/Interference.wav')
        pygame.mixer.music.play(-1)

        while True:
            #The Main Game
            
                
            for event in pygame.event.get():

                DISPLAYSURF.fill(BLACK)
                #Screen Background

                if (DEBUG):
                    #DEBUGer
                    print(event)
                
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    
                    
                elif (event.type == KEYDOWN):
                    
                    if (event.key == K_RIGHT and playerPos[0] < MAPWIDTH - 1):
                        #Player Moves RIGHT
                        playerPos[0] += 1
                    if (event.key == K_LEFT and playerPos[0] > 0):
                        #Player Moves LEFT
                        playerPos[0] -= 1
                    if (event.key == K_UP and playerPos[1] > 0):
                        #Player Moves UP
                        playerPos[1] -= 1
                    if (event.key == K_DOWN and playerPos[1] < MAPWIDTH - 1):
                        #Player Moves DOWN
                        playerPos[1] += 1
                    if (event.key == K_SPACE):
                        #Player Places Block
                        currentTile = tilemap[playerPos[1]][playerPos[0]]
                        inventory[currentTile] += 1
                        what = randint(1,10)
                        if (what >= 1 and what <= 4):
                            tilemap[playerPos[1]][playerPos[0]] = LAVA
                        
                        if (what >= 5 and what <= 7):
                            tilemap[playerPos[1]][playerPos[0]] = COAL
                            
                        else:
                            tilemap[playerPos[1]][playerPos[0]] = DIRT
                        
                    if (event.key == K_1):
                        #Player Places Dirt
                        currentTile = tilemap[playerPos[1]][playerPos[0]]
                        if (inventory[DIRT] > 0):
                             inventory[DIRT] -= 1
                             tilemap[playerPos[1]][playerPos[0]] = DIRT
                             inventory[currentTile] += 1
                        else:
                            if (DEBUG):
                                print(Fore.RED + "NO DIRT")
                    if (event.key == K_1 and event.key == K_MODE):
                        if (inventory[DIRT] > 0):
                             inventory[DIRT] -= 1
                        else:
                            if (DEBUG):
                                print("NO DIRT")
                    if (event.key == K_2):
                        #Player Places Grass
                        if (inventory[GRASS] > 0):
                            inventory[GRASS] -= 1
                            tilemap[playerPos[1]][playerPos[0]] = GRASS
                            inventory[currentTile] += 1
                        else:
                            if (DEBUG):
                                print("NO GRASS")
                    if (event.key == K_2 and event.key == K_MODE):
                        if (inventory[GRASS] > 0):
                             inventory[GRASS] -= 1
                        else:
                            if (DEBUG):
                                print("NO GRASS")
                    if (event.key == K_4):
                        #Player Places Coal
                        if (inventory[COAL] > 0):
                            inventory[COAL] -= 1
                            tilemap[playerPos[1]][playerPos[0]] = COAL
                            inventory[currentTile] += 1
                        else:
                            if (DEBUG):
                                print("NO COAL")
                    if (event.key == K_4 and event.key == K_MODE):
                        if (inventory[COAL] > 0):
                             inventory[COAL] -= 1
                        else:
                            if (DEBUG):
                                print("NO COAL")
                    if (event.key == K_3):
                        #Player Places Water
                        if (inventory[WATER] > 0):
                            inventory[WATER] -= 1
                            tilemap[playerPos[1]][playerPos[0]] = WATER
                            inventory[currentTile] += 1
                        else:
                            if (DEBUG):
                                print("NO WATER")
                    if (event.key == K_3 and event.key == K_MODE):
                        if (inventory[DIRT] > 0):
                             inventory[DIRT] -= 1
                        else:
                            if (DEBUG):
                                print("NO WATER")
                    if (event.key == K_5):
                        #Player Places Lava
                        if (inventory[LAVA] > 0):
                            inventory[LAVA] -= 1
                            tilemap[playerPos[1]][playerPos[0]] = LAVA
                            inventory[currentTile] += 1
                        else:
                            if (DEBUG):
                                print("NO LAVA")
                    if (event.key == K_5 and event.key == K_MODE):
                        if (inventory[LAVA] > 0):
                             inventory[LAVA] -= 1
                        else:
                            if (DEBUG):
                                print("NO LAVA")
                    if (event.key == K_6):
                        #Player Places TNT
                        print("NO TNT LAG-FREE ON!")
                    if (event.key == K_6 and event.key == K_MODE):
                        print("NO TNT LAG-FREE ON!")
                    if (event.key == K_SLASH):
                        #Commands
                        command = input("use /help for more info")

                        if (command == "/help"):
                            print("/kill")
                            print("/mods")
                            print("/playerinfo")
                            print("/playerchange")
                            print("/debugtoggle")
                            print("/random")
                            print("/ct")
                            print("/crafttnt")
                            print("/read")
                            print("/soundoff")
                            print("/soundon")

                        elif (command == "/soundoff"):
                            pygame.mixer.music.stop()
                        elif (command == "/soundon"):
                            pygame.mixer.music.play()
                        elif (command == "/read"):
                            read = open("Info/Read Me.txt")
                            read = read.read()
                            print(read)
                        elif (command == "/crafttnt"):
                            while True:
                                print("NO TNT LAG-FREE ON!")
                                
                        elif (command == "/kill"):
                            pygame.quit()
                        elif (command == "/mods"):
                            print(mods)
                        elif (command == "/playerinfo"):
                            print(username.read())
                        elif (command == "/playerchange"):
                            usernam = input()
                            username = username.write(usernam)
                            username.close()
                            print("Username is now " + username)
                        elif (command == "/debugtoggle"):
                            if (DEBUG):
                                DEBUG = False
                            else:
                                DEBUG = True
                        elif (command == "/random"):
                            print("How Much?")
                            a = input()
                            a = int(a)
                            print("Lowest Number?")
                            b = input()
                            b = int(b)
                            print("Highest Number?")
                            c = input()
                            c = int(c)
                            print("wait...")
                            for i in a:
                                print(randint(b,c))
                            print("wait...")
                            print("DONE!")
                        
                        elif (command == "/ct"):
                            if os.name == "posix":
                                 os.system('clear')
                            elif os.name in ("nt", "dos", "ce"):
                                 os.system('CLS')
                            else:
                                print("Your System is unknown!")

                        else:
                            print("Command " + command + " does not exist!")
                        
            for row in  range(MAPHEIGHT):
                #MAP Generater

                for column in range(MAPWIDTH):
                    
                    DISPLAYSURF.blit(textures[tilemap[row][column]],(column * TILESIZE, row * TILESIZE))
                DISPLAYSURF.blit(PLAYER,(playerPos[0] * TILESIZE, playerPos[1] * TILESIZE))
                
                

                
                
                placePosition = 10 
                for item in resources:
                    DISPLAYSURF.blit(textures[item],(placePosition, MAPHEIGHT * TILESIZE + 20))
                    textObj = INVFONT.render(str(inventory[item]), True, BROWN, BLACK)
                    DISPLAYSURF.blit(textObj,(placePosition,MAPHEIGHT * TILESIZE + 20))
                    placePosition += 50

            pygame.display.update()
            fpsClock.tick(24)
        if choose == 3:
            print("Instructions:")
            print()
            print("Pytcraft is simple!")
            print()
            print("up = up key")
            print("left = left key")
            print("right = rightkey")
            print("down = down key")
            print("press the number of block order to place")
            print("space to collect")
            print("press MODE and the the number of block to drop")
            print("/ to open command center")
        if choose == 2:
            pygame.quit()
            sys.exit()
            return
     

def main():

    import sys#sys stands for system
    import random#Our random Generater
    import dumbmenu as dm#The Menu
    import time#Do I have to explain it?
    import os#os checks if your os is compatible
    from os.path import exists
    global username
    #The Username
    username = open("info/username.txt")#Put your username here

    if (username.read() == "guest"):
        print("Wellcome to Pytcraft! You do not have a login! Just put in a username: ")
        a = input("")
        username = username.write(a)
        username.close()
        print("Thanks!")
        main()
        
    print("Do you want to do lag-free mode? y for yes!")
    ask = input()
    if (ask == "y"):
        print("please wait...")
        lagfree()
    print("Do to u want to change the textures? n for no m for minecraft styled")
    ask = input()
    
    if (ask == "n"):
        DIRTT = 'Pics/dirt.png'
        GRASSS = 'Pics/grass.png'
        WATERR = 'Pics/water.png'
        COALL = 'Pics/coal.png'
        LAVAA = 'Pics/lava.png'
        TNTT = 'Pics/tnt.png'
        print('')
    elif (ask == "m"):
        DIRTT = 'Pics/Textures/MinecraftStyled/dirt.png'
        GRASSS = 'Pics/Textures/MinecraftStyled/grass.png'
        WATERR = 'Pics/Textures/MinecraftStyled/water.png'
        COALL = 'Pics/Textures/MinecraftStyled/coal.png'
        LAVAA = 'Pics/Textures/MinecraftStyled/lava.png'
        TNTT = 'Pics/Textures/MinecraftStyled/tnt.png'
        print('')
        
    else:
        print("Ok Put the directory to the picture .png works best! Type \'skip\' to set to defalt!")
        print("DIRT?")
        DIRTT = input()
        if (DIRTT == "skip"):
            DIRTT = 'Pics/dirt.png'
        if (exists(DIRTT) == False):
            DIRTT = 'Pics/texturenotfound.png'
        print("GRASS?")
        GRASSS = input()
        if (GRASSS == "skip"):
            GRASSS = 'Pics/grass.png'
        if (exists(GRASSS) == False):
            GRASSS = 'Pics/texturenotfound.png'
        print("WATER?")
        WATERR = input()
        if (WATERR == "skip"):
            WATERR = 'Pics/water.png'
        if (exists(WATERR) == False):
            WATERR = 'Pics/texturenotfound.png'
        print("COAL?")
        COALL = input()
        if (COALL == "skip"):
            COALL = 'Pics/coal.png'
        if (exists(COALL) == False):
            COALL = 'Pics/texturenotfound.png'
        print("LAVA?")
        LAVAA = input()
        if (LAVAA == "skip"):
            LAVAA == 'Pics/lava.png'
        if (exists(LAVAA) == False):
            LAVAA = 'Pics/texturenotfound.png'
        print("TNT?")
        TNTT = input()
        if (TNTT == "skip"):
            TNTT = 'Pics/tnt.png'
        if (exists(TNTT) == False):
            TNTT = 'Pics/texturenotfound.png'
    if (exists(TNTT) == False):
        TNTT = 'Pics/texturenotfound.png'
    if (exists(LAVAA) == False):
        LAVAA = 'Pics/texturenotfound.png'
    if (exists(COALL) == False):
        COALL = 'Pics/texturenotfound.png'
    if (exists(WATERR) == False):
        WATERR = 'Pics/texturenotfound.png'
    if (GRASSS == "skip"):
        GRASSS = 'Pics/grass.png'
    if (exists(DIRTT) == False):
        DIRTT = 'Pics/texturenotfound.png'
    birds = "Pics/bord2.png"
    bird = pygame.image.load("Pics/bird2.png")
    textures = {#YAY PICTURES!
        DIRT : pygame.image.load(DIRTT),
        GRASS : pygame.image.load(GRASSS),
        WATER : pygame.image.load(WATERR),
        COAL : pygame.image.load(COALL),
        LAVA : pygame.image.load(LAVAA),
        TNT : pygame.image.load(TNTT),
        CLOUD : pygame.image.load('Pics/cloud.png')
        
        }

    DEBUG = False

    #Starts Pygame
    pygame.init()
    
    #Size of screen
    size = width, height = 340,240
    #The Screen
    screen = pygame.display.set_mode(size)
    #The Screen Background
    screen.fill(blue)
    #Updates Display
    pygame.display.update()
    pygame.key.set_repeat(500,30)
    #Title
    pygame.display.set_caption('Pytcraft 2D')
    #Icon
    pygame.display.set_icon(pygame.image.load('Pics/Logo.png'))
    #THE MENU
    choose = dm.dumbmenu(screen, [
                        'Start Game',
                        
                        'Instructions',
                        'QUIT'], 64,64,None,32,1.4,green,red)
    
    if choose == 1:
            #Instructions
            print("Instructions:")
            print()
            print("Pytcraft is simple!")
            print()
            print("up = up key")
            print("left = left key")
            print("right = rightkey")
            print("down = down key")
            print("press the number of block order to place")
            print("space to collect")
            print("press MODE and the the number of block to drop")
            print("/ to open command center")
            main()
    if choose == 2:
        #Quits Game
            pygame.quit()
            sys.exit()
            return
    if choose == 0:
        #Quits Menu
        pygame.quit()
        #Input
        
        MAPWIDTH = int(input("Put in width put 0 to set it to normal!"))

        if (MAPWIDTH == 0):
            MAPWIDTH = 20

       #Input
        MAPHEIGHT = int(input("Put in height put 0 to set it to normal!"))

        if (MAPHEIGHT == 0):
            MAPHEIGHT = 20

        #All Resources
        resources = [DIRT,GRASS,WATER,COAL,LAVA,TNT]
        #Tilemap
        tilemap = [[DIRT for w in range(MAPWIDTH)]for h in range(MAPHEIGHT)]
        #Starts Pygame (Again)
        pygame.init()

        #Display Stuff
        DISPLAYSURF = pygame.display.set_mode((MAPWIDTH * TILESIZE,MAPHEIGHT * TILESIZE + 50))
        INVFONT = pygame.font.Font(pygame.font.get_default_font(),18)
        PLAYER = pygame.image.load('Pics/player.png').convert_alpha()
        playerPos = [0,0]

        #Continued...
        pygame.display.set_caption('Pytcraft 2D')
        pygame.display.set_icon(pygame.image.load('Pics/Logo.png'))

        pygame.joystick.init()
        joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
        
        #Random seed Generater
        for rw in range(MAPHEIGHT):
            for cl in range(MAPWIDTH):
                print("Getting Random Stuff")
                randomnumber = randint(0,15)
                if (randomnumber == 0):
                    tile = COAL
                    print("COAL")
                elif (randomnumber == 1 or randomnumber == 2):
                    tile = WATER
                    print("WATER")
                elif (randomnumber >= 1 and randomnumber <= 7):
                    tile = GRASS
                    print("GRASS")
                elif (randomnumber >= 8 and randomnumber <= 9):
                    tile = LAVA
                    print("LAVA")
                else:
                    tile = DIRT
                    print("DIRT")
                tilemap[rw][cl] = tile
        music = pygame.mixer.music.load('Music/Interference.wav')
        pygame.mixer.music.play(-1)
        cloudx = -200
        cloudy = 0
        cloudx2 = -200
        cloudy2 = 50
        birdx = 0
        birdy = -600

        while True:
            #The Main Game
            if (pygame.mixer.music.get_busy == False):
                pygame.mixer.music.play()
                
            for event in pygame.event.get():

                DISPLAYSURF.blit(textures[CLOUD].convert_alpha(),(cloudx,cloudy))
                cloudx += 1
                if cloudx > MAPWIDTH*TILESIZE:

                    cloudy = random.randint(0,MAPHEIGHT * TILESIZE)
                    cloudx = -200

                DISPLAYSURF.fill(BLACK)
                #Screen Background

                if (DEBUG):
                    #DEBUGer
                    print(event)
                
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    
                    
                elif (event.type == KEYDOWN):
                    if (event.key == K_s):
                        #Screenshots
                        name = input("What do you want to name this screenshot? ")
                        pygame.image.save(screen,name + ".png")
                    if (event.key == K_RIGHT and playerPos[0] < MAPWIDTH - 1):
                        #Player Moves RIGHT
                        playerPos[0] += 1
                    if (event.key == K_LEFT and playerPos[0] > 0):
                        #Player Moves LEFT
                        playerPos[0] -= 1
                    if (event.key == K_UP and playerPos[1] > 0):
                        #Player Moves UP
                        playerPos[1] -= 1
                    if (event.key == K_DOWN and playerPos[1] < MAPWIDTH - 1):
                        #Player Moves DOWN
                        playerPos[1] += 1
                    if (event.key == K_SPACE):
                        #Player Places Block
                        currentTile = tilemap[playerPos[1]][playerPos[0]]
                        inventory[currentTile] += 1
                        what = randint(1,10)
                        if (what >= 1 and what <= 4):
                            tilemap[playerPos[1]][playerPos[0]] = LAVA
                        
                        if (what >= 5 and what <= 7):
                            tilemap[playerPos[1]][playerPos[0]] = COAL
                            
                        else:
                            tilemap[playerPos[1]][playerPos[0]] = DIRT
                        
                    if (event.key == K_1):
                        #Player Places Dirt
                        currentTile = tilemap[playerPos[1]][playerPos[0]]
                        if (inventory[DIRT] > 0):
                             inventory[DIRT] -= 1
                             tilemap[playerPos[1]][playerPos[0]] = DIRT
                             inventory[currentTile] += 1
                        else:
                            if (DEBUG):
                                print("NO DIRT")
                    if (event.key == K_1 and event.key == K_MODE):
                        if (inventory[DIRT] > 0):
                             inventory[DIRT] -= 1
                        else:
                            if (DEBUG):
                                print("NO DIRT")
                    if (event.key == K_2):
                        #Player Places Grass
                        if (inventory[GRASS] > 0):
                            inventory[GRASS] -= 1
                            tilemap[playerPos[1]][playerPos[0]] = GRASS
                            inventory[currentTile] += 1
                        else:
                            if (DEBUG):
                                print("NO GRASS")
                    if (event.key == K_2 and event.key == K_MODE):
                        if (inventory[GRASS] > 0):
                             inventory[GRASS] -= 1
                        else:
                            if (DEBUG):
                                print("NO GRASS")
                    if (event.key == K_4):
                        #Player Places Coal
                        if (inventory[COAL] > 0):
                            inventory[COAL] -= 1
                            tilemap[playerPos[1]][playerPos[0]] = COAL
                            inventory[currentTile] += 1
                        else:
                            if (DEBUG):
                                print("NO COAL")
                    if (event.key == K_4 and event.key == K_MODE):
                        if (inventory[COAL] > 0):
                             inventory[COAL] -= 1
                        else:
                            if (DEBUG):
                                print("NO COAL")
                    if (event.key == K_3):
                        #Player Places Water
                        if (inventory[WATER] > 0):
                            inventory[WATER] -= 1
                            tilemap[playerPos[1]][playerPos[0]] = WATER
                            inventory[currentTile] += 1
                        else:
                            if (DEBUG):
                                print("NO WATER")
                    if (event.key == K_3 and event.key == K_MODE):
                        if (inventory[DIRT] > 0):
                             inventory[DIRT] -= 1
                        else:
                            if (DEBUG):
                                print("NO WATER")
                    if (event.key == K_5):
                        #Player Places Lava
                        if (inventory[LAVA] > 0):
                            inventory[LAVA] -= 1
                            tilemap[playerPos[1]][playerPos[0]] = LAVA
                            inventory[currentTile] += 1
                        else:
                            if (DEBUG):
                                print("NO LAVA")
                    if (event.key == K_5 and event.key == K_MODE):
                        if (inventory[LAVA] > 0):
                             inventory[LAVA] -= 1
                        else:
                            if (DEBUG):
                                print("NO LAVA")
                    if (event.key == K_6):
                        #Player Places TNT
                        if (inventory[TNT] > 0):
                            inventory[TNT] -= 1
                            tilemap[playerPos[1]][playerPos[0]] = DIRT
                            tilemap[playerPos[1] * 2][playerPos[0] *2] = DIRT
                            tilemap[playerPos[1] * 3][playerPos[0] *3] = DIRT
                            tilemap[playerPos[1] * -4][playerPos[0] *-4] = DIRT
                            tilemap[playerPos[1] * -5][playerPos[0] *-5] = DIRT
                            
                        else:
                            if (DEBUG):
                                print("NO TNT BUT YOU CAN CRAFT TNT")
                    if (event.key == K_6 and event.key == K_MODE):
                        if (inventory[TNT] > 0):
                             inventory[TNT] -= 1
                        else:
                            if (DEBUG):
                                print("NO TNT")
                    if (event.key == K_SLASH):
                        #Commands
                        command = input("use /help for more info")

                        if (command == "/help"):
                            print("/kill")
                            print("/mods")
                            print("/playerinfo")
                            print("/playerchange")
                            print("/debugtoggle")
                            print("/random")
                            print("/ct")
                            print("/crafttnt")
                            print("/read")
                            print("/reload")
                            print("/soundoff")
                            print("/soundon")

                        elif (command == "/soundoff"):
                            pygame.mixer.music.stop()
                        elif (command == "/soundon"):
                            pygmae.mixer.music.play()

                        elif (command == "/reload"):
                            print("Please wait...")
                            time.sleep(2)
                            pygame.quit()
                            print("pygame.quit()")
                            time.sleep(2)
                            main()

                        elif (command == "/read"):
                            read = open("Info/Read Me.txt")
                            read = read.read()
                            print(read)
                        elif (command == "/crafttnt"):
                            while True:
                                print("Crafting...")
                                if (inventory[LAVA] >= 1 and inventory[COAL] >= 8):
                                    inventory[LAVA] -= 1
                                    inventory[COAL] -= 8
                                    inventory[TNT] += 1
                                    h = input("Wana Make Another n for no")
                                    if (h == "n"):
                                        break
                                else:
                                    print("You need 1 lava and 8 coal to make!")
                                    break
                        elif (command == "/kill"):
                            pygame.quit()
                        elif (command == "/mods"):
                            print(mods)
                        elif (command == "/playerinfo"):
                            print(username.read())
                        elif (command == "/playerchange"):
                            usernam = input()
                            username = username.write(usernam)
                            username.close()
                            print("Username is now " + username)
                        elif (command == "/debugtoggle"):
                            if (DEBUG):
                                DEBUG = False
                            else:
                                DEBUG = True
                        elif (command == "/random"):
                            print("How Much?")
                            a = input()
                            a = int(a)
                            print("Lowest Number?")
                            b = input()
                            b = int(b)
                            print("Highest Number?")
                            c = input()
                            c = int(c)
                            print("wait...")
                            for i in a:
                                print(randint(b,c))
                            print("wait...")
                            print("DONE!")
                        elif (command == "/ct"):
                            if os.name == "posix":
                                 os.system('clear')
                            elif os.name in ("nt", "dos", "ce"):
                                 os.system('CLS')
                            else:
                                print("Your System is unknown!")

                        else:
                            print("Command " + command + " does not exist!")
                        
            for row in  range(MAPHEIGHT):
                #MAP Generater

                for column in range(MAPWIDTH):
                    
                    DISPLAYSURF.blit(textures[tilemap[row][column]],(column * TILESIZE, row * TILESIZE))
                DISPLAYSURF.blit(PLAYER,(playerPos[0] * TILESIZE, playerPos[1] * TILESIZE))
                
                

                
                
                placePosition = 10 
                for item in resources:
                    DISPLAYSURF.blit(textures[item],(placePosition, MAPHEIGHT * TILESIZE + 20))
                    textObj = INVFONT.render(str(inventory[item]), True, BROWN, BLACK)
                    DISPLAYSURF.blit(textObj,(placePosition,MAPHEIGHT * TILESIZE + 20))
                    placePosition += 50

            DISPLAYSURF.blit(textures[CLOUD].convert_alpha(),(cloudx,cloudy))
            cloudx += 1
            if cloudx > MAPWIDTH*TILESIZE:

                cloudy = random.randint(0,MAPHEIGHT * TILESIZE)
                cloudx = -200
            DISPLAYSURF.blit(textures[CLOUD].convert_alpha(),(cloudx2,cloudy2))
            cloudx2 += 1
            if cloudx2 > MAPWIDTH*TILESIZE:

                cloudy2 = random.randint(0,MAPHEIGHT * TILESIZE)
                cloudx2 = -200
            if (birds == "Pics/bird1.png"):
                bird = pygame.image.load("Pics/bird2.png")
                birds = "Pics/bird2.png"
            if (birds == "Pics/bird2.png"):
                bird = pygame.image.load("Pics/bird1.png")
                birds = "Pics/bird1.png"
            else:
                bird = pygame.image.load("Pics/bird1.png")
                birds = "Pics/bird1.png"
            birdx += 5
            if birdx > MAPWIDTH*TILESIZE:

                birdy = random.randint(0,MAPHEIGHT * TILESIZE)
                birdx = -200
            DISPLAYSURF.blit(bird.convert_alpha(),(birdx,birdy))
            pygame.display.update()
            pygame.display.flip()
            fpsClock.tick(24)
        if choose == 3:
            print("Instructions:")
            print()
            print("Pytcraft is simple!")
            print()
            print("up = up key")
            print("left = left key")
            print("right = rightkey")
            print("down = down key")
            print("press the number of block order to place")
            print("space to collect")
            print("press shift and the the number of block to drop")
            print("/ to open command center")
        if choose == 2:
            pygame.quit()
            sys.exit()
            return
     


if __name__ == '__main__':
    print("Redirecting...")
    time.sleep(1.5)
    game()
 

#END OF GAME!
