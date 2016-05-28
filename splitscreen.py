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
    test.clear(BLUE)
    for i in range(len(test)):
        test.clear(BLACK, i)
        test.draw_lines(GREEN, [(0, 0), (100, 100 * i)], i)
        
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

    @property
    def scale(self):
        return self.SUBSCREEN / self.divisions

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

    def clear(self, color, i=None):
        """ Clear the subscreen at index i.
        """
        if i != None:
            pygame.draw.rect(self.screen, color, self.rect(i))
        else:
            Screen.clear(self, color)

    def draw_lines(self, color, points, i=None):
        if i == None:
            Screen.draw_lines(self, color, points)
        else:
            origin = self.rect(i)[:2]
            adjusted_points = []
            for x, y in points:
                new_x = origin[0] + x * self.scale
                new_y = origin[1] + y * self.scale
                adjusted_points.append((new_x, new_y))
            Screen.draw_lines(self, color, adjusted_points)
        
 
    




if __name__ == '__main__':
    main()









