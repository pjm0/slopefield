# splitscreen.py
"""

Display multiple force field functions in a grid pattern.

"""

## TODO
##
## - interface for writing lines to subscreens (have to "shrink" coords)
##
##

from colors import *
from screen import Screen
from math import ceil, sqrt
import pygame.display, pygame.draw

def main():
    from time import sleep
    test = Splitscreen(5)
    test.clear_all(BLUE)
    for i in range(len(test)):
        test.clear(BLACK, i)
        
    test.refresh()
    sleep(2)
    pygame.quit()

class Splitscreen(Screen):
    BORDER = 1
    SUBSCREEN = 6
    
    def __init__(self, size):
        Screen.__init__(self)
        self.size = size

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
        Screen.clear(self, color)
    




if __name__ == '__main__':
    main()









