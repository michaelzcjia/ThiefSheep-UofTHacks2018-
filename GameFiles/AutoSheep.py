import pygame as pg
import math
import random
import numpy as np


class autoSheep():
    x_speed = None
    y_speed = None

    speed = None

    sheep = pg.image.load("../Sprites/sheep.png")

    sheepRect = None

    def __init__(self):
        self.x_speed = random.uniform(-2, 2)
        self.y_speed = random.uniform(-2, 2)

        self.speed = [self.x_speed, self.y_speed]

        self.sheepRect = self.sheep.get_rect()
        self.sheepRect.x = random.randint(1, 1000)  # 500
        self.sheepRect.y = random.randint(1, 700)  # 350

    # function for sheep movement
    def update(self):
        # random num generator to see when the sheep changes directions
        sameDir = random.uniform(0, 2)

        # if statement to change sheep direction
        if sameDir > 1.98:
            xRandNum = random.uniform(1, 10)
            xMult = 1 if xRandNum > 5 else -1

            yRandNum = random.uniform(1, 10)
            yMult = 1 if yRandNum > 5 else -1

            self.x_speed = xMult * random.uniform(-2, 2)
            self.y_speed = yMult * random.uniform(-2, 2)

        self.sheepRect = self.sheepRect.move([self.x_speed, self.y_speed])





#    events = pg.event.get()

#     for event in events:
#         if event.type == pg.KEYDOWN:
#             if event.key == pg.K_LEFT:

#             if event.key == pg.K_RIGHT:
#                 x_pos += 1
#             if event.key == pg.K_UP:
#                 y_pos += 1
#             if event.key == pg.K_DOWN:
#                 y_pos -= 1
# Going to put capture method in here
#             if event.key == pg.




# Detects sheep or plyrSheep within a radius and 'kills' them
# token -=1
# if token = 0 :
# end game


