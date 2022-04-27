import random as rand

from .sorting_algorithm import sorting_algorithm
from room.room import room

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
        head_room = Room()
        rand.seed()
        x_end   = rand.randrange(0, self.w) # Set Notation-> [0, (w - 1)]
        y_end   = rand.randrange(0, self.h) # Set Notation-> [0, (h - 1)]
        x_start = rand.randrange(0, self.w) # Set Notation-> [0, (w - 1)]
        y_start = rand.randrange(0, self.h) # Set Notation-> [0, (h - 1)]
        x_curr  = random_x_start            # start x at the x start
        y_curr  = random_y_start            # start y at the y start
        while not ((x_end != x_curr) and (y_end != y_curr)):
            choice = rand.randrange(1, 5) # make a choice of direction
            if choice == 1 and (y_curr - 1 >= 0):
                y_curr -= 1
            # If we chose to go right and we can still go right
            elif choice == 2 and (x_curr + 1 < self.w):
                x_curr += 1
            # If we chose to go down and we can still go down
            elif choice == 3 and (y_curr + 1 < self.h):
                y_curr += 1
            # If we chose to go left and we can still go left
            elif choice == 4 and (x_curr - 1 >= 0):
                x_curr -= 1
            if(head_room.room_data == None)

    def wilsons_algorithm(self, x_curr, x_end, y_curr, y_end):
