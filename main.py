from maze_parser.maze_parser import Parser
import random as rand

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

def get_neighbors(M, x_center, y_center, w, h):
    A = []
    for i in range(-1, 1):
        for j in range(-1, 1):
            if (current_y_coor - 1 >= 0) and (current_x_coor + 1 < w) and (current_x_coor - 1 >= 0) and (current_y_coor - 1 >= 0):
                if M[y_center + i][x_center + j] != "0":
                    A.append(M[y_center + i][x_center + j])
    return A

def path_to_mat(P, M, w, h):
    for i in range(len(P)):
        M[P[i][1]][P[i][0]] = P[i][2]

def my_mat_trans(M, x_start, y_start, x_end, y_end, w, h):
    for i in range(len(M)):
        print(M[i])
    x_curr = x_start
    y_curr = y_start
    M_final = [["0" for _ in range(w)] for _ in range(h)]
    if M[y_start][x_start] == 1:
        M_final[y_start][x_start] = "s"
        y_curr -= 1
    if M[y_start][x_start] == 2:
        M_final[y_start][x_start] = "j"
        x_curr += 1
    if M[y_start][x_start] == 3:
        M_final[y_start][x_start] = "i"
        y_curr += 1
    if M[y_start][x_start] == 4:
        M_final[y_start][x_start] = "h"
        x_curr -= 1

    while not (x_curr == x_end and y_curr == y_end):
        print(x_curr, y_curr)
        if M[y_curr][x_curr] == 1:
            # /\ & /\
            if M[y_curr - 1][x_curr] == 1: 
                M_final[y_curr][x_curr]     = "b" 
            # /\ & ->
            elif M[y_curr - 1][x_curr] == 2:
                M_final[y_curr][x_curr]     = "b"
                M_final[y_curr - 1][x_curr] = "f"
                x_curr += 1
            # /\ & \/ Cannot Occur!!
            # /\ & <-
            elif M[y_curr - 1][x_curr] == 4:
                M_final[y_curr][x_curr]     = "b"
                M_final[y_curr - 1][x_curr] = "d"
                x_curr -= 1
            elif M[y_curr - 1][x_curr] == 5:
                M_final[y_curr][x_curr] = "b"
            y_curr -= 1
        elif M[y_curr][x_curr] == 2:
            # -> & /\
            if M[y_curr][x_curr + 1] == 1: 
                M_final[y_curr][x_curr] = "a"
                M_final[y_curr][x_curr + 1] = "c"
                y_curr -= 1
            # -> & ->
            elif M[y_curr][x_curr + 1] == 2: 
                M_final[y_curr][x_curr] = "a"
            # -> & \/
            elif M[y_curr][x_curr + 1] == 3: 
                M_final[y_curr][x_curr] = "a"
                M_final[y_curr][x_curr + 1] = "d"
                y_curr += 1
            elif M[y_curr][x_curr + 1] == 6:
                M_final[y_curr][x_curr] = "a"
            x_curr += 1
            # -> & <- Connot Occur!!
        elif M[y_curr][x_curr] == 3:
            # \/ & /\ Cannot Occur!!
            # \/ & ->
            if M[y_curr + 1][x_curr] == 2: 
                M_final[y_curr][x_curr] = "b"
                M_final[y_curr + 1][x_curr] = "g"
                x_curr += 1
            # \/ & \/
            elif M[y_curr + 1][x_curr] == 3: 
                M_final[y_curr][x_curr] = "b" 
            # \/ & <-
            elif M[y_curr + 1][x_curr] == 4: 
                M_final[y_curr][x_curr]     = "b"
                M_final[y_curr + 1][x_curr] = "f"
                x_curr -= 1
            elif M[y_curr][x_curr] == 7:
                M_final[y_curr][x_curr] = "b"
            y_curr += 1
        elif M[y_curr][x_curr] == 4:
            # <- & /\
            if M[y_curr][x_curr - 1] == 1: 
                M_final[y_curr][x_curr] = "a"
                M_final[y_curr][x_curr - 1] = "g"
                y_curr += 1
            # <- & -> Cannot Occur!!
            # <- & \/
            elif M[y_curr][x_curr - 1] == 3: 
                M_final[y_curr][x_curr] = "a"
                M_final[y_curr][x_curr - 1] = "f"
                y_curr -= 1
            # <- & <-
            elif M[y_curr][x_curr - 1] == 4: 
                M_final[y_curr][x_curr] = "a"
            elif M[y_curr][x_curr - 1] == 8:
                M_final[y_curr][x_curr] = "a"
            x_curr -= 1
    if M[y_end][x_end] == 5:
        M_final[y_end][x_end] = "i"
    if M[y_end][x_end] == 6:
        M_final[y_end][x_end] = "j"
    if M[y_end][x_end] == 7:
        M_final[y_end][x_end] = "s"
    if M[y_end][x_end] == 8:
        M_final[y_end][x_end] = "h"
    return M_final


q = 5
M = wilsons_algorithm(q, q)
for i in range(q):
    print(M[i])
p = Parser()
