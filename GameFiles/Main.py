import sys, pygame
from GameFiles import AutoSheep as char
from GameFiles import PlayerSheep as pSheep
from GameFiles import PlayerShepherd as pSheph
from pygame import mixer

pygame.init()

size = width, height = 1000, 700
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

black = 0, 0, 0
green = 95, 142, 41
white = 255, 255, 255


#INTRO

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

#score shit

global shepScore,sScore
shepScore = 0
sScore = 0
myfont = pygame.font.SysFont('freesansbold.ttf', 30)


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            #if event.type == MouseButtonDown:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("Thief Sheep", largeText)
        TextRect.center = ((width / 2), (height / 2))
        screen.blit(TextSurf, TextRect)

        button("Play!", width/2-100/2, 450, 100, 50, green, white, game_loop)

        pygame.display.update()
        clock.tick(5)

# MAKE AUTOSHEEP SWARM
numSheep = 35
sheepSwarm = []

for sheep in range(numSheep):
    newSheep = char.autoSheep()
    newSheep.sheep = pygame.transform.scale(newSheep.sheep,(80,80))
    sheepSwarm.append(newSheep)

# sheep player tings

# ling = char.autoSheep()
plyrSheph = pSheph.PlayerShepherd()
plyrSheep = pSheep.PlayerSheep()


def end_game(winner):



    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(white)

        largeText = pygame.font.Font('freesansbold.ttf', 80)
        TextSurf, TextRect = text_objects("The winner is :" + winner + "!", largeText)
        TextRect.center = ((width / 2), (height / 2))
        screen.blit(TextSurf, TextRect)


        button("Play Again", 150, 450, 100, 50, green, white, game_loop)
        button("Quit", 760, 450, 100, 50, green, white, quitgame)

        pygame.display.update()
        clock.tick(15)

def quitgame():
    pygame.quit()

def game_loop():

    mixer.init()
    mixer.music.load('../Sounds/backgroundMusic2.mp3')
    mixer.music.play()

    iconShep = pygame.image.load("../Sprites/whiteshep2.png")
    iconSheep = pygame.image.load("../Sprites/whitesheep.png")

    plyrSheph.capture_tokens = 5
    plyrSheph.win = False

    # iconSheep = pygame.transform.scale(iconSheep, (80, 80))
    # iconShep = pygame.transform.scale(iconShep, (80, 80))

    #time = 75
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        count = 0
        for sheep in sheepSwarm:

            if mixer.music.get_busy() == False:
                end_game('Sheep (time is up!)')

            sheep.update()

            sheepPos = sheep.sheepRect

            screen.blit(sheep.sheep, sheep.sheepRect)
            #print(sheep.speed)

            if sheepPos.left < 0 or sheepPos.right > width:
                sheep.x_speed = -sheep.x_speed
                #print(sheep.speed, sheep.sheepRect)  # personal check

            if sheepPos.top < 0 or sheepPos.bottom > height:
                sheep.y_speed = -sheep.y_speed
                #print(sheep.speed, sheep.sheepRect)  # personal check

            #screen.blit(sheep.sheep, sheep.sheepRect)

            if count == 0:
                #Following code is for player as shepherd
                shephRect = plyrSheph.plyrMove()
                plyrSheph.update(shephRect)
                screen.blit(plyrSheph.plyr,plyrSheph.plyrRect)
                #Following code if for player as sheep
                sheepRect = plyrSheep.plyrMove()
                plyrSheep.update(sheepRect)
                screen.blit(plyrSheep.plyr, plyrSheep.plyrRect)
            count += 1
            plyrSheph.capture(sheepSwarm, plyrSheep)

        #score update
        global shepScore, sScore
        shepScore = 5 - plyrSheph.capture_tokens
        sScore = plyrSheph.capture_tokens

        #iconShep = pygame.image.load("../Sprites/whiteshep2.png")
        #iconSheep = pygame.image.load("../Sprites/whitesheep.png")

        shepscoretext = myfont.render(":" + str(shepScore), 1, (255, 255, 255))
        sScoretext = myfont.render(":" + str(sScore), 1, (255, 255, 255))

        iconSheep = pygame.transform.scale(iconSheep, (80, 80))
        iconShep = pygame.transform.scale(iconShep, (80, 80))

        screen.blit(iconShep,(width*0.83,620))
        screen.blit(iconSheep,(width*0.02,620))

        screen.blit(shepscoretext, (width*0.02+90, 660))
        screen.blit(sScoretext,(width*0.83+70,660))


        pygame.display.flip()
        screen.fill(green)

        if sScore == 10000:
            end_game("sheep")

        if plyrSheph.win == True:
            end_game('Shepherd')
        elif plyrSheph.capture_tokens == 0 and plyrSheph.win == False:
            end_game('Sheep')

        # if plyrSheph.capture_tokens == 0:
        #     if plyrSheph.win == True:
        #         end_game('Shepherd')
        #     else:
        #         end_game('Sheep')

       # ling.update()  # sheep moves
       #
       #  ling_pos = ling.sheepRect  # sheep position
       #
       #  if ling_pos.left < 0 or ling_pos.right > width:
       #      ling.x_speed = -ling.x_speed
       #      print(ling.speed, ling.sheepRect)  # personal check
       #
       #  if ling_pos.top < 0 or ling_pos.bottom > height:
       #      ling.y_speed = -ling.y_speed
       #      print(ling.speed, ling.sheepRect)  # personal check
       #

       #  screen.blit(ling.sheep, ling.sheepRect)
        #pygame.display.flip()

    #
    # speed1 = [2.5, 2]
    # speed2 = [4, 4]
    # speed3 = [6,3]
    # speeds = [speed1, speed2, speed3]

    # sheepSpecs = ()

    # ball = pygame.image.load("Sprites/sheep.png")
    # ballrect = ball.get_rect()
    # ballrect2 = ball.get_rect()
    # ballrect3 = ball.get_rect()
    # while 1:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT: sys.exit()
    #
    #     ballrect = ballrect.move(speed1)
    #     ballrect2 = ballrect2.move(speed2)
    #     ballrect3 = ballrect3.move(speed3)
    #
    #     sheepList = [ballrect, ballrect2, ballrect3]
    #
    #     spec = (sheepList, speeds)
    #     for i in range(3):
    #             if spec[0][i].left < 0 or spec[0][i].right > width:
    #                 spec[1][i][0] = -spec[1][i][0]
    #             if spec[0][i].top < 0 or spec[0][i].bottom > height:
    #                 spec[1][i][1] = -spec[1][i][1]
    #
    #
    #     screen.fill(black)
    #     screen.blit(ball, ballrect3)
    #     screen.blit(ball, ballrect2)
    #     screen.blit(ball, ballrect)
    #     pygame.display.flip()

game_intro()

#game_loop()


