import pygame as pg
import math
import random
import numpy as np

#Purpose of this class is to add items to ThiefSheep. Still need to determine whether we should add all the different
#items or just a repeat of this one

class Item():

    ItemRect = None

    Item1 = pg.image.load("../Sprites/sheep.png")


    def __init__(self):

