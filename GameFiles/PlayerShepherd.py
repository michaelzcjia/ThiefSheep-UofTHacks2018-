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