import random as rand

from .sorting_algorithm import sorting_algorithm

class wilsons_algorithm(sorting_algorithm):
    def __init__(self, *args, **kwargs):
        if 'w' in kwargs:
            self.w = kwargs.get('w')
        else:
            self.w = 10
        if 'h' in kwargs:
            self.h = kwargs.get('h')
        else:
            self.h = 10

    def generate_dungeon(self):
        rand.seed()
        x_end   = rand.randrange(0, self.w) # Set Notation-> [0, (w - 1)]
        y_end   = rand.randrange(0, self.h) # Set Notation-> [0, (h - 1)]
        x_start = rand.randrange(0, self.w) # Set Notation-> [0, (w - 1)]
        y_start = rand.randrange(0, self.h) # Set Notation-> [0, (h - 1)]
        x_curr  = random_x_start            # start x at the x start
        y_curr  = random_y_start            # start y at the y start
        while not ((x_end != x_curr) and (y_end != y_curr)):
