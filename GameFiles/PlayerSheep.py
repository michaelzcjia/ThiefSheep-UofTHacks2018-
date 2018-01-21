import pygame as pg
import math
import random
import numpy as np


class PlayerSheep():
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


    def __init__(self, imgURL = "../Sprites/sheep.png"):
        self.plyr = pg.image.load(imgURL)  # sheep.png, shepherd.png
        self.plyr = pg.transform.scale(self.plyr, (80, 80))
        self.plyrRect = self.plyr.get_rect()
        self.plyrRect.x = random.randint(1, 1000)  # 500
        self.plyrRect.y = random.randint(1, 700)  # 350


    def plyrMove(self):

        kDict = pg.key.get_pressed()
        # detect up,down,left,right keypresses.
        # Returns a rect object with coordinates after movement

        if (kDict[pg.K_w] != 0) and (kDict[pg.K_a] != 0):
            return self.plyrRect.move(self.speedUpLeft)
        if (kDict[pg.K_s] != 0) and (kDict[pg.K_a] != 0):
            return self.plyrRect.move(self.speedDownLeft)
        if (kDict[pg.K_w] != 0) and (kDict[pg.K_d] != 0):
            return self.plyrRect.move(self.speedUpRight)
        if (kDict[pg.K_s] != 0) and (kDict[pg.K_d] != 0):
            return self.plyrRect.move(self.speedDownRight)
        if (kDict[pg.K_w] != 0):
            return self.plyrRect.move(self.speedUp)
        if (kDict[pg.K_s] != 0):
            return self.plyrRect.move(self.speedDown)
        if (kDict[pg.K_d] != 0):
            return self.plyrRect.move(self.speedRight)
        if (kDict[pg.K_a] != 0):
            return self.plyrRect.move(self.speedLeft)

        return self.plyrRect

    def update(self, newPosition):
        self.plyrRect = newPosition