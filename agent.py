from colors import *
from geometry import angle_to, add_angles
from math import pi, sin, cos
import pygame
from random import choice, random

class Agent():
    def __init__(self, loc, theta, speed, rotation, screen):
        self.color = (choice(range(256)),
                      choice(range(256)),
                      choice(range(256)))
        self.loc = loc
        self.initial_theta = self.theta = theta
        self.speed = speed
        self.rotation = rotation
        self.path = [tuple(self.loc)]
        self.screen = screen
        self.active = True

    def __str__(self):
        return "rotation:{}\ninitial theta:{}\nfinal theta:{}\nfinal location:{}\n".format(self.rotation, self.initial_theta, self.theta, self.loc)

    def rotate_to(self, angle):
        self.theta = angle #+ (pi / 4 / 256) * choice(range(1, 256))

    def rotate_by(self, angle):
        self.theta += angle

    def advance(self):
        #self.theta = (-angle_to(goal, ball) + 2*angle_to(self.loc, ball))
        if self.active and (self.theta is not None):
            self.loc = (self.loc[0] + self.speed * cos(self.theta),
                        self.loc[1] + self.speed * sin(self.theta))
            if (0 <= self.loc[0] <= self.screen.width and
                0 <= self.loc[1] <= self.screen.height):
                self.path.append(tuple(self.loc))
            else:
                self.active =  False

    def draw(self, subscreen=None):
        if len(self.path) >= 2:
            #pygame.draw.lines
            if subscreen == None:
                self.screen.draw_lines(self.color, self.path)
            else:
                self.screen.draw_lines(self.color, self.path, subscreen)
        #pygame.draw.line(screen, BLUE, self.path[0], ball)
