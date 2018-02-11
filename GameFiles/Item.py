import pygame as pg
import math
import random
import numpy as np

#Purpose of this class is to add items to ThiefSheep. Still need to determine whether we should add all the different
#items or just a repeat of this one


class item():


    itemRect = None
    itemImage = pg.image.load("../Sprites/appo.png") #only create the apple item for now


    def __int__(self): #initializes coordinates of the item
        self.itemRect = self.itemImage.get_rect()

        #random positioning, adjust the following ranges if SCREENRES changes
        self.itemRect.x = random.randint(1, 1000)
        self.itemRect.y = random.randint(1, 700)


