import pygame as pg
import math
import random
import numpy as np


class PlayerHunt():
    plyr = None
    plyrRect = None
    speedRight = [2, 0]
    speedLeft = [-2, 0]
    speedUp = [0, -2]
    speedDown = [0, 2]
    speedUpLeft = [-math.sqrt(2), -math.sqrt(2)]
    speedUpRight = [math.sqrt(2), -math.sqrt(2)]
    speedDownLeft = [-math.sqrt(2), math.sqrt(2)]
    speedDownRight = [math.sqrt(2), math.sqrt(2)]


    def __init__(self, imgURL):
        self.plyr = pg.image.load("shephard.png")  # sheep.png, shepherd.png
        self.plyrRect = self.plyr.get_rect()


    def plyrMove(self):

        kDict = pg.key.get_pressed()
        # detect up,down,left,right keypresses.
        # Returns a rect object with coordinates after movement

        if (kDict[pg.K_UP] != 0) and (kDict[pg.K_LEFT] != 0):
            return self.sheepRect.move(self.speedUpLeft)
        if (kDict[pg.K_DOWN] != 0) and (kDict[pg.K_LEFT] != 0):
            return self.sheepRect.move(self.speedDownLeft)
        if (kDict[pg.K_UP] != 0) and (kDict[pg.K_RIGHT] != 0):
            return self.sheepRect.move(self.speedUpRight)
        if (kDict[pg.K_UP] != 0) and (kDict[pg.K_RIGHT] != 0):
            return self.sheepRect.move(self.speedDownRight)
        if (kDict[pg.K_UP] != 0):
            return self.sheepRect.move(self.speedUp)
        if (kDict[pg.K_DOWN] != 0):
            return self.sheepRect.move(self.speedDown)
        if (kDict[pg.K_RIGHT] != 0):
            return self.sheepRect.move(self.speedRight)
        if (kDict[pg.K_LEFT] != 0):
            return self.sheepRect.move(self.speedLeft)

        return None