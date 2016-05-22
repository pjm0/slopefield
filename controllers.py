# controllers.py

import pygame.joystick

def get_controllers():
    pygame.joystick.init()
    count = pygame.joystick.get_count()
    return [pygame.joystick.Joystick(n) for n in range(count)]

if __name__ == '__main__':
    controllers = get_controllers()
