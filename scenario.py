# scenario.py

#import pygame
from math import *
from random import choice
from time import sleep

import colors
from screen import *
screen_x, screen_y = screen.get_width(), screen.get_height()

from geometry import *
from agent import Agent
from avoid_border import avoid_border

class Scenario:
    def __init__(self):
        pass

    def draw(self):
        pass

if __name__ == '__main__':
    test = Scenario((1024, 768), frozenset())
    
