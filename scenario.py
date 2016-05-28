# scenario.py

#import pygame
from math import *
from random import choice
from time import sleep

import colors
from splitscreen import Splitscreen
#screen_x, screen_y = screen.get_width(), screen.get_height()

from colors import *
from geometry import *
from agent import Agent
from avoid_border import avoid_border
from slopefield import f, magfield, SCALE

class Scenario:
    def __init__(self, num_screens):
        
        self.fields = {"f":magfield, "g":f} # To map function names to forcefield functions.
        self.agents = {} # To map agent names to Agent objects.
        self.display = Splitscreen(num_screens)
        self.resolution = self.display.width, self.display.height


    def draw_field(self, i=None):
        display = self.display
        for x in range(0, self.display.width, 2 * SCALE):
            for y in range(0, self.display.height, 2 * SCALE):
                #print(x, y)
                angle = self.fields["f"](x, y)
                x_component, y_component = cos(angle), sin(angle)
                display.draw_lines(RED,
                                   [(x, y),
                                    ((x + int(x_component * SCALE * 1.5),
                                    y + int(y_component * SCALE * 1.5)))], i)
                display.draw_lines(GREEN,
                                   [(x, y),
                                    ((x + int(x_component * SCALE),
                                    y + int(y_component * SCALE)))], i)
##                pygame.draw.aaline(screen, RED, (x, y),
##                                   (x + int(x_component * SCALE * 1.5),
##                                    y + int(y_component * SCALE * 1.5)))
##                pygame.draw.aaline(screen, GREEN, (x, y),
##                                   (x + int(x_component * SCALE),
##                                    y + int(y_component * SCALE)))
        display.refresh()



    def draw(self, x, y):
        pass

if __name__ == '__main__':
    test = Scenario(10)
    test.draw_field(0)
    test.draw_field(1)
    test.draw_field(2)
    test.draw_field(3)
    
