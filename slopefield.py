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


SCALE = 10
opponent = choice(range(150, 774)), choice(range(150, 518))
ball = 512, 384#choice(range(512)), choice(range(screen_y))
goal = 1, 384






def f(x, y, scale=1):
    BORDER_WIDTH = 100;
#*//*
#*/ double attack_heading
    if distance_to_line((x, y), ball, goal) < 20 and distance_to((x, y), ball) < 100:
        theta = angle_to(goal, ball)
##    elif (distance_to_line((x, y), ball, goal) < 200
##          and distance_to((x, y), ball) < 200
##          and distance_to((x, y), goal) < 20 + distance_to(ball, goal)):
##        if add_angles(angle_to(ball, goal), -angle_to((x, y), goal)) > 0:
##            theta = angle_to(goal, ball) + pi/2
##        else:
##            theta = angle_to(goal, ball) - pi/2;
##    elif abs(add_angles(angle_to((x, y), ball), -angle_to(goal, ball))) < pi/2:#########wrong
##        theta = angle_to(ball, goal);
    else:
        theta = -angle_to(goal, ball)+ 2*angle_to((x, y), ball);
    #print(theta)
    vector_x = cos(theta);
    vector_y = sin(theta);
    
    
    if x < BORDER_WIDTH:
        vector_x = max(vector_x, (BORDER_WIDTH - x) / BORDER_WIDTH)
    if x > screen_x - BORDER_WIDTH:
        vector_x = min(vector_x, -(x - (screen_x - BORDER_WIDTH)) / BORDER_WIDTH)
    if y < BORDER_WIDTH:
        vector_y = max(vector_y, (BORDER_WIDTH - y) / BORDER_WIDTH)
    if y > screen_y - BORDER_WIDTH:
        vector_y = min(vector_y, -(y - (screen_y - BORDER_WIDTH)) / BORDER_WIDTH)
        
##    if distance_to((x, y), opponent) < 200:
##        theta = angle_to((x, y), opponent) + 0.25 * pi + \
##                0.25 * pi * distance_to((x, y), opponent) / 200
##    else:
    theta = atan2(vector_y, vector_x)

    return theta #x + scale * vector_x, y + scale * vector_y;


#/*
def main():
    from pygame.locals import QUIT
    while True:
        agents = [Agent((choice(range(screen_x)),
                         choice(range(screen_y))),
                        0,
                        10,
                        None, screen) for _ in range(100000)]
        screen.fill(BLACK)
        ball = choice(range(150, 774)), choice(range(150, 518))
        opponent = choice(range(150, 774)), choice(range(150, 518))
        #pygame.draw.circle(screen, BLUE, ball, 10)
        pygame.draw.circle(screen, WHITE, goal, 10)
        pygame.draw.circle(screen, RED, opponent, 10)
        for x in range(0, screen_x, 2 * SCALE):
            for y in range(0, screen_y, 2 * SCALE):
                #print(x, y)
                angle = f(x, y)
                x_component, y_component = cos(angle), sin(angle)
                pygame.draw.aaline(screen, RED, (x, y),
                                   (x + int(x_component * SCALE * 1.5),
                                    y + int(y_component * SCALE * 1.5)))
                pygame.draw.aaline(screen, GREEN, (x, y),
                                   (x + int(x_component * SCALE),
                                    y + int(y_component * SCALE)))

        for n in range(40):
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                else:
                    print(event.type)
            pygame.draw.circle(screen, WHITE, goal, 10)
            #pygame.draw.circle(screen, RED, opponent, 10)
            for agent in agents:
                agent.rotate_to(f(*agent.loc))
                agent.advance()
                agent.draw()
            pygame.display.flip()
    

if __name__ == '__main__':
    main()
