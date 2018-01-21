import pygame as pg
import math
import random
import numpy as np


class PlayerShepherd():
    plyr = None
    plyrRect = None
    speedRight = [3, 0]
    speedLeft = [-3, 0]
    speedUp = [0, -3]
    speedDown = [0, 3]
    speedUpLeft = [-2.0, -2.0]
    speedUpRight = [2.0, -2.0]
    speedDownLeft = [-2.0, 2.0]
    speedDownRight = [2.0, 2.0]
    capture_tokens = 5
    win = False;

    def __init__(self, imgURL = "../Sprites/shephard .png"):
        self.plyr = pg.image.load(imgURL)  # sheep.png, shepherd.png
        self.plyr = pg.transform.scale(self.plyr, (100, 100))
        self.plyrRect = self.plyr.get_rect()
        self.plyrRect.x = random.randint(1, 1000)  # 500
        self.plyrRect.y = random.randint(1, 700)  # 350


    def plyrMove(self):

        kDict = pg.key.get_pressed()
        # detect up,down,left,right keypresses.
        # Returns a rect object with coordinates after movement

        if (kDict[pg.K_UP] != 0) and (kDict[pg.K_LEFT] != 0):
            return self.plyrRect.move(self.speedUpLeft)
        if (kDict[pg.K_DOWN] != 0) and (kDict[pg.K_LEFT] != 0):
            return self.plyrRect.move(self.speedDownLeft)
        if (kDict[pg.K_UP] != 0) and (kDict[pg.K_RIGHT] != 0):
            return self.plyrRect.move(self.speedUpRight)
        if (kDict[pg.K_DOWN] != 0) and (kDict[pg.K_RIGHT] != 0):
            return self.plyrRect.move(self.speedDownRight)
        if (kDict[pg.K_UP] != 0):
            return self.plyrRect.move(self.speedUp)
        if (kDict[pg.K_DOWN] != 0):
            return self.plyrRect.move(self.speedDown)
        if (kDict[pg.K_RIGHT] != 0):
            return self.plyrRect.move(self.speedRight)
        if (kDict[pg.K_LEFT] != 0):
            return self.plyrRect.move(self.speedLeft)

        return self.plyrRect

    def update(self, newPosition):
        self.plyrRect = newPosition

 #updated capture code
    def capture(self,sheepSwarm, plyrSheep):


        kDict = pg.key.get_pressed()
        if (kDict[pg.K_RSHIFT] != 0):
             if (self.capture_tokens > 0):  # Right now I have the capture tokens under the class definition, might have to put under player class

                      # When rightshift key is pressed, activates capture function if token >0

                      # Get current position of the Shephard, using placeholder image var
                shepherd_x = self.plyrRect.x
                shepherd_y = self.plyrRect.y

                      # Gets position of all sheep (including evil sheep)
                      # and eliminates all sheep within the range of the shephard

                for sheep in sheepSwarm:
                    x = sheep.sheepRect.x
                    y = sheep.sheepRect.y
                    xP = plyrSheep.plyrRect.x
                    yP = plyrSheep.plyrRect.y

                    if ((shepherd_x - 40) <= x <= (shepherd_x + 40) and (shepherd_y - 40) <= y <= (shepherd_y + 40)):
                        sheepSwarm.remove(sheep)
                        #sheep.sheep =  pg.transform.scale(sheep.sheep, (0, 0))
                        self.capture_tokens -= 1
                    if ((shepherd_x - 40) <= xP <= (shepherd_x + 40) and (shepherd_y - 40) <= yP <= (shepherd_y + 40)):
                        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~SHEPHERD WINS!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                        self.win = True;
                        #plyrSheep.plyr =  pg.transform.scale(plyrSheep.plyr, (0, 0))
                        plyrSheep.plyrRect.x = random.randint(0,1000)
                        plyrSheep.plyrRect.y = random.randint(0,700)
                        self.capture_tokens -= 1

