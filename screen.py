import pygame
from colors import *

def main():
    from time import sleep
    test = Screen()
    test.draw_lines(WHITE, [(0, 0), (100, 100)])
    test.refresh()
    sleep(2)
    pygame.quit()

class Screen:
    SIZE = (1600, 900)
    
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.SIZE)
        self.screen.fill(BLACK)
        
    @property
    def width(self):
        return self.screen.get_width()

    @property
    def height(self):
        return self.screen.get_height()

    @property
    def rect(self):
        return None

    def clear(self, color):
        """ Clear the entire screen.
        """
        self.screen.fill(color)
    
    def refresh(self):
        """ Update the screen.
        """
        pygame.display.flip()

    def draw_lines(self, color, points):
        pygame.draw.aalines(self.screen, color, False, points)


if __name__ == '__main__':
    main()
