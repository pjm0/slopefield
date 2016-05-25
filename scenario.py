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
from slopefield import f, magfield, SCALE

class Scenario:
    def __init__(self):
        self.resolution = screen_x, screen_y
        self.fields = {"f":magfield} # To map function names to forcefield functions.
        self.agents = {} # To map agent names to Agent objects.


    def draw_field(self):
        for x in range(0, screen_x, 2 * SCALE):
            for y in range(0, screen_y, 2 * SCALE):
                #print(x, y)
                angle = self.fields["f"](x, y)
                x_component, y_component = cos(angle), sin(angle)
                pygame.draw.aaline(screen, RED, (x, y),
                                   (x + int(x_component * SCALE * 1.5),
                                    y + int(y_component * SCALE * 1.5)))
                pygame.draw.aaline(screen, GREEN, (x, y),
                                   (x + int(x_component * SCALE),
                                    y + int(y_component * SCALE)))
        pygame.display.flip()



    def draw(self, x, y):
        pass

if __name__ == '__main__':
    test = Scenario()
    test.draw_field()
    
