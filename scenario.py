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
from slopefield import f, g, h, magfield, t, ball, z, c
import pygame
from pygame import QUIT

def main():
    test = Scenario(1, 20)
    
##    test.draw_field("f", 0)
##    test.draw_field("g", 1)
    scale = 10
    f_1, f_2  = magfield, g
    while True:
        for n in range(scale):
            test.display.clear(BLACK)
            test.fields["h"] = z(f_1, f_2, n/scale)
            test.draw_field("h", 0)
            test.run_agents(1)
            test.display.refresh()
        for n in range(scale, 0, -1):
            test.display.clear(BLACK)
            test.fields["h"] = z(f_1, f_2, n/scale)
            test.draw_field("h", 0)
            test.run_agents(1)
            test.display.refresh()
##    test.run_agents(100)
##        test.fields["f"] = g
##        test.fields["g"] = f
##        test.run_agents(50)
##        test.fields["f"] = f
##        test.fields["g"] = g

    pygame.quit()


class Scenario:
    BOTS = 10000
    def __init__(self, num_screens, scale = 10):
        
        self.fields = {"h": magfield} # To map function names to forcefield functions.
        self.order = ["h"]
        self.display = Splitscreen(num_screens)
        self.agents = {key:[Agent((choice(range(self.display.width)),
                                   choice(range(self.display.height))),
                                  0,
                                  10,
                        None, self.display) for _ in range(self.BOTS)]
                       for key in self.fields} # To map agent names to Agent objects.
        self.resolution = self.display.width, self.display.height
        self.scale = scale


    def draw_field(self, key, i=None):
        display = self.display
        display.clear(BLACK, i)
        for agent in self.agents[key]:
            agent.draw(i)
        for x in range(0, self.display.width, 2 * self.scale):
            for y in range(0, self.display.height, 2 * self.scale):
                #print(x, y)
                angle = self.fields[key](x, y)
                if angle is None:
                    pass
                else:
                    x_component, y_component = cos(angle), sin(angle)
                    display.draw_lines(RED,
                                       [(x, y),
                                        ((x + int(x_component * self.scale * 1.5),
                                        y + int(y_component * self.scale * 1.5)))], i)
                    display.draw_lines(GREEN,
                                       [(x, y),
                                        ((x + int(x_component * self.scale),
                                        y + int(y_component * self.scale)))], i)
        #display.refresh()


    def run_agents(self, n):
        
        for n in range(n):
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
##                else:
##                    print(event.type)
            #pygame.draw.circle(screen, RED, opponent, 10)
            for n in range(len(self.order)):
                key = self.order[n]
                for agent in self.agents[key]:
                    agent.rotate_to(self.fields[key](*agent.loc))
                    agent.advance()
                    agent.draw(n)
##            self.display.refresh()

    
    def draw(self, x, y):
        pass

if __name__ == '__main__':
    main()
    
