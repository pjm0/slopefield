# splitscreen.py
"""

Display multiple force field functions in a grid pattern.

"""
from colors import *
from screen import *
from math import ceil, sqrt
import pygame.display, pygame.draw

def main():
    from time import sleep
    test = Splitscreen(screen, 20)
    for i in range(len(test)):
        test.clear(BLUE, i)
        
    test.refresh()
    sleep(6)
    pygame.quit()

class Splitscreen:
    BORDER = 1
    SUBSCREEN = 3
    
    def __init__(self, screen, size):
        self.screen = screen
        self.size = size
        
    @property
    def width(self):
        return self.screen.get_width()

    @property
    def height(self):
        return self.screen.get_height()

    @property
    def columns(self):
        return ceil(sqrt(len(self)))

    @property
    def divisions(self):
        SUBSCREEN, BORDER = self.SUBSCREEN, self.BORDER
        return (BORDER) + (SUBSCREEN + BORDER) * self.columns

    @property
    def x_scale(self):
        return self.width / self.divisions

    @property
    def y_scale(self):
        return self.height / self.divisions

    def rect(self, i):
        SUBSCREEN, BORDER = self.SUBSCREEN, self.BORDER
        columns = self.columns
        x, y = (i % columns, i // columns)
        top_left_x, top_left_y = ((BORDER + (SUBSCREEN + BORDER)*x),
                                  (BORDER + (SUBSCREEN + BORDER)*y))
        return (self.x_scale * (top_left_x),
                self.y_scale * (top_left_y),
                self.x_scale * SUBSCREEN,
                self.y_scale * SUBSCREEN)
                                  

    def __len__(self):
        return self.size

    def clear(self, color, i):
        """ Clear the subscreen at index i.
        """
        pygame.draw.rect(self.screen, color, self.rect(i))

    def clear_all(self, color):
        """ Clear the entire screen.
        """
        self.screen.fill(color)
    
    def refresh(self):
        """ Update the screen.
        """
        pygame.display.flip()



    def get_top_left(self, index):
        divisions = self.get_n_divisions()

def h(n):
    columns = f(n)
    return (n // columns, n % columns) if n > 0 else None


if __name__ == '__main__':
    main()
