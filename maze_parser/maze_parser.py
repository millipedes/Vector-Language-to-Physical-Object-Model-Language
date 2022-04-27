def dual_parse(parent, current, child):
    print("parent ", parent, " current ", current, " child ", child, sep='')
    if   parent == 1:
        if   current == 1 and child == 1:
            return "b"
        elif current == 1 and child == 2:
            return "b"
        elif current == 1 and child == 4:
            return "b"
        elif current == 2:
            return "f"
        elif current == 4:
            return "d"
        elif current == 5:
            return "b"
    elif parent == 2:
        if current == 1:
            return "c"
        elif current == 2 and child == 2:
            return "a"
        elif current == 2 and child == 1:
            return "a"
        elif current == 2 and child == 3:
            return "a"
        elif current == 3:
            return "d"
    elif parent == 3:
        if current == 1:
            return "g"
        if current == 2:
            return "g"
        elif current == 3 and child == 3:
            return "b"
        elif current == 3 and child == 2:
            return "b"
        elif current == 3 and child == 4:
            return "c"
        elif current == 4:
            return "c"
        elif current == 7:
            return "a"
    elif parent == 4:
        if current == 2:
            return "g"
        elif current == 3:
            return "f"
        elif current == 4 and child == 4:
            return "a"
        elif current == 4 and child == 1:
            return "g"
        elif current == 4 and child == 3:
            return "a"
        elif current == 8:
            return "a"

# def get_mat_parent(M, x, y, x_start,  y_start):
#     x_prev = 0
#     y_prev = 0
#     x_curr = x_start
#     y_curr = y_start
#     while not (x_curr == x and y_curr == y):
#         if M[y_curr][x_curr] == 1:
#             y_prev = y_curr
#             y_curr -= 1
#         if M[y_curr][x_curr] == 2:
#             x_prev = x_curr
#             x_curr += 1
#         if M[y_curr][x_curr] == 3:
#             y_prev = y_curr
#             y_curr += 1
#         if M[y_curr][x_curr] == 4:
#             x_prev = x_curr
#             x_curr -= 1
#     return M[y_prev][x_prev]
# 
def get_mat_child(M, x, y):
    if M[y][x] == 1:
        return M[y - 1][x]
    if M[y][x] == 2:
        return M[y][x + 1]
    if M[y][x] == 3:
        return M[y + 1][x]
    if M[y][x] == 4:
        return M[y][x - 1]

# def get_mat_g_child(M, x, y):
#     if M[y][x] == 1:
#         if get_mat_child(M, x, y) == 1:
#             return get_mat_child(M, x, y - 2)
#         elif get_mat_child(M, x, y) == 2:
#             return get_mat_child(M, x + 1, y - 1)
#         elif get_mat_child(M, x, y) == 3:
#             return get_mat_child(M, x, y)
#         elif get_mat_child(M, x, y) == 4:
#             return get_mat_child(M, x - 1, y - 1)
#     if M[y][x] == 2:
#         if get_mat_child(M, x, y) == 1:
#             return get_mat_child(M, x + 1, y - 1)
#         elif get_mat_child(M, x, y) == 2:
#             return get_mat_child(M, x + 2, y)
#         elif get_mat_child(M, x, y) == 3:
#             return get_mat_child(M, x + 1, y + 1)
#         elif get_mat_child(M, x, y) == 4:
#             return get_mat_child(M, x, y)
#     if M[y][x] == 3:
#         if get_mat_child(M, x, y) == 1:
#             return get_mat_child(M, x, y)
#         elif get_mat_child(M, x, y) == 2:
#             return get_mat_child(M, x + 1, y + 1)
#         elif get_mat_child(M, x, y) == 3:
#             return get_mat_child(M, x, y + 2)
#         elif get_mat_child(M, x, y) == 4:
#             return get_mat_child(M, x - 1, y + 1)
#     if M[y][x] == 4:
#         if get_mat_child(M, x, y) == 1:
#             return get_mat_child(M, x - 1, y - 1)
#         elif get_mat_child(M, x, y) == 2:
#             return get_mat_child(M, x, y)
#         elif get_mat_child(M, x, y) == 3:
#             return get_mat_child(M, x - 1, y + 1)
#         elif get_mat_child(M, x, y) == 4:
#             return get_mat_child(M, x - 2, y)

def tri_path_parse(parent, current, child):
    pass
