import random as rand

from .sorting_algorithm import sorting_algorithm
from room.room import room
from room.room import room_data

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

    def generate_dungeon(self):
        head_room = Room()
        M = self.preleminary_matrix_gen()
        wilsons_algorithm(head_room, M, 0, 0)

    def wilsons_algorithm(self, current, parent, M, x, y):
        if current.room_data == None:
            if   M[y][x] == 1:
                current.get_room_data().turn_up_current()
                current.set_up(Room())
                current.get_up().get_room_data() = room_data()
                wilsons_algorithm(current.get_up(), M, x, y - 1)
            elif M[y][x] == 2:
                current.get_room_data().turn_right_current()
                current.set_right(Room())
                current.get_right().get_room_data() = room_data()
                wilsons_algorithm(current.get_right(), M, x + 1, y)
            elif M[y][x] == 3:
                current.get_room_data().turn_down_current()
                current.set_down(Room())
                current.get_down().get_room_data() = room_data()
                wilsons_algorithm(current.get_down(), M, x, y + 1)
            elif M[y][x] == 4:
                current.get_room_data().turn_left_current()
                current.set_left(Room())
                current.get_left().get_room_data() = room_data()
                wilsons_algorithm(current.get_left(), M, x - 1, y)

    def preleminary_matrix_gen(self):
        M = [[0 for _ in range(self.w)] for _ in range(self.h)]
        rand.seed()
        x_end  = rand.randrange(0, self.w)  # Set Notation-> [0, (w - 1)]
        y_end  = rand.randrange(0, self.h)  # Set Notation-> [0, (h - 1)]
        self.ix = rand.randrange(0, self.w) # Set Notation-> [0, (w - 1)]
        self.iy = rand.randrange(0, self.h) # Set Notation-> [0, (h - 1)]
        x_curr = self.ix                    # start x at the x start
        y_curr = self.iy                    # start y at the y start
        rand.seed()                         # start random engine
        while not (x_curr == x_end and y_curr == y_end):
            choice = rand.randrange(1, 5) # make a choice of direction
            M[y_curr][x_curr] = choice # Choice of direction
            if choice == 1 and (y_curr - 1 >= 0):
                y_curr -= 1
            # If we chose to go right and we can still go right
            elif choice == 2 and (x_curr + 1 < w):
                x_curr += 1
            # If we chose to go down and we can still go down
            elif choice == 3 and (y_curr + 1 < h):
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
        get_path(P, M, self.ix, self.iy, x_end, y_end)
        path_to_mat(P, path_Mat, w, h)
        return M
    def path_to_mat(P, M, w, h):
        for i in range(len(P)):
            M[P[i][1]][P[i][0]] = P[i][2]
    def get_path(A, M, x, y, x_end, y_end):
        A.append((x, y, M[y][x]))
        if M[y][x] == 1:
            get_path(A, M, x, y - 1, x_end, y_end)
        if M[y][x] == 2:
            get_path(A, M, x + 1, y, x_end, y_end)
        if M[y][x] == 3:
            get_path(A, M, x, y + 1, x_end, y_end)
        if M[y][x] == 4:
            get_path(A, M, x - 1, y, x_end, y_end)
