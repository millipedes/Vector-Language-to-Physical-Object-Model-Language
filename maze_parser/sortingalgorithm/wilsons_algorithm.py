from abc import ABC, abstractmethod
import random as rand
class sorting_algorithm(ABC):
    @abstractmethod
    def generate_dungeon(self):
        pass
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
        random_x_dest  = rand.randrange(0, w) # Set Notation-> [0, (w - 1)]
        random_y_dest  = rand.randrange(0, h) # Set Notation-> [0, (h - 1)]
        random_x_start = rand.randrange(0, w) # Set Notation-> [0, (w - 1)]
        random_y_start = rand.randrange(0, h) # Set Notation-> [0, (h - 1)]
        current_x_coor = random_x_start            # start x at the x start
        current_y_coor = random_y_start            # start y at the y start
# def get_path(A, M, x, y, x_end, y_end):
#     A.append((x, y, M[y][x]))
#     if M[y][x] == 1:
#         get_path(A, M, x, y - 1, x_end, y_end)
#     if M[y][x] == 2:
#         get_path(A, M, x + 1, y, x_end, y_end)
#     if M[y][x] == 3:
#         get_path(A, M, x, y + 1, x_end, y_end)
#     if M[y][x] == 4:
#         get_path(A, M, x - 1, y, x_end, y_end)
# 
# def get_neighbors(M, x_center, y_center, w, h):
#     A = []
#     for i in range(-1, 1):
#         for j in range(-1, 1):
#             if (current_y_coor - 1 >= 0) and (current_x_coor + 1 < w) and (current_x_coor - 1 >= 0) and (current_y_coor - 1 >= 0):
#                 if M[y_center + i][x_center + j] != "0":
#                     A.append(M[y_center + i][x_center + j])
#     return A
# 
# def path_to_mat(P, M, w, h):
#     for i in range(len(P)):
#         M[P[i][1]][P[i][0]] = P[i][2]
# 
# def wilsons_algorithm(h, w):
#     M = [[0 for _ in range(w)] for _ in range(h)]
#     rand.seed()
#     random_x_dest  = rand.randrange(0, w) # Set Notation-> [0, (w - 1)]
#     random_y_dest  = rand.randrange(0, h) # Set Notation-> [0, (h - 1)]
#     random_x_start = rand.randrange(0, w) # Set Notation-> [0, (w - 1)]
#     random_y_start = rand.randrange(0, h) # Set Notation-> [0, (h - 1)]
#     current_x_coor = random_x_start            # start x at the x start
#     current_y_coor = random_y_start            # start y at the y start
#     rand.seed()                                # start random engine
#     while not (current_x_coor == random_x_dest and current_y_coor ==
#             random_y_dest):
#         choice = rand.randrange(1, 5) # make a choice of direction
#         M[current_y_coor][current_x_coor] = choice # Choice of direction
#         if choice == 1 and (current_y_coor - 1 >= 0):
#             current_y_coor -= 1
#         # If we chose to go right and we can still go right
#         elif choice == 2 and (current_x_coor + 1 < w):
#             current_x_coor += 1
#         # If we chose to go down and we can still go down
#         elif choice == 3 and (current_y_coor + 1 < h):
#             current_y_coor += 1
#         # If we chose to go left and we can still go left
#         elif choice == 4 and (current_x_coor - 1 >= 0):
#             current_x_coor -= 1
#     if choice == 1:
#         M[current_y_coor][current_x_coor] = 5
#     if choice == 2:
#         M[current_y_coor][current_x_coor] = 6
#     if choice == 3:
#         M[current_y_coor][current_x_coor] = 7
#     if choice == 4:
#         M[current_y_coor][current_x_coor] = 8
#     P = [] # Path
#     path_Mat = [[0 for _ in range(w)] for _ in range(h)]
#     get_path(P, M, random_x_start, random_y_start, random_x_dest,
#             random_y_dest)
#     print(P)
#     path_to_mat(P, path_Mat, w, h)
#     M_final = my_mat_trans(path_Mat, random_x_start, random_y_start,
#             random_x_dest, random_y_dest, w, h)
#     return M_final
