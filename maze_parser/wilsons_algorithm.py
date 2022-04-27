import random as rand

from .sorting_algorithm import sorting_algorithm
from .maze_parser import dual_parse

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
        self.ix = 0
        self.iy = 0
        self.path = self.generate_dungeon()

    def generate_dungeon(self):
        return self.wilsons_algorithm()
    
    def wilsons_algorithm(self):
        M = [[0 for _ in range(self.w)] for _ in range(self.h)]
        rand.seed()
        x_end  = rand.randrange(0, self.w)  # Set Notation-> [0, (w - 1)]
        y_end  = rand.randrange(0, self.h)  # Set Notation-> [0, (h - 1)]
        self.ix = rand.randrange(0, self.w) # Set Notation-> [0, (w - 1)]
        self.iy = rand.randrange(0, self.h) # Set Notation-> [0, (h - 1)]
        x_curr = self.ix                    # start x at the x start
        y_curr = self.iy                    # start y at the y start
        rand.seed()                         # start random engine
        choice = 0
        while not (x_curr == x_end and y_curr == y_end):
            choice = rand.randrange(1, 5) # make a choice of direction
            M[y_curr][x_curr] = choice # Choice of direction
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
        if choice == 1:
            M[y_curr][x_curr] = 5
        if choice == 2:
            M[y_curr][x_curr] = 6
        if choice == 3:
            M[y_curr][x_curr] = 7
        if choice == 4:
            M[y_curr][x_curr] = 8
        P = [] # Path
        self.make_path(P, M, self.ix, self.iy, self.ix, self.iy, x_end, y_end)
        return P

    def make_path(self, A, M, x, y, x_start, y_start, x_end, y_end):
        if M[y][x] == 1:
            if (x_start == x and y_start == y) or (x_end == x and y_end == y):
                A.append((x, y, M[y][x], 's'))
            else:
                A.append((x, y, M[y][x], dual_parse(M[y][x], M[y - 1][x])))
            self.make_path(A, M, x, y - 1, x_start, y_start, x_end, y_end)
        elif M[y][x] == 2:
            if (x_start == x and y_start == y) or (x_end == x and y_end == y):
                A.append((x, y, M[y][x], 'j'))
            else:
                A.append((x, y, M[y][x], dual_parse(M[y][x], M[y][x + 1])))
            self.make_path(A, M, x + 1, y, x_start, y_start, x_end, y_end)
        elif M[y][x] == 3:
            if (x_start == x and y_start == y) or (x_end == x and y_end == y):
                A.append((x, y, M[y][x], 'i'))
            else:
                A.append((x, y, M[y][x], dual_parse(M[y][x], M[y + 1][x])))
            self.make_path(A, M, x, y + 1, x_start, y_start, x_end, y_end)
        elif M[y][x] == 4:
            if (x_start == x and y_start == y) or (x_end == x and y_end == y):
                A.append((x, y, M[y][x], 'h'))
            else:
                A.append((x, y, M[y][x], dual_parse(M[y][x], M[y][x - 1])))
            self.make_path(A, M, x - 1, y, x_start, y_start, x_end, y_end)

    def print_path(self):
        for i in range(len(self.path)):
            print(self.path[i])
