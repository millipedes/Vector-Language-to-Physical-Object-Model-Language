def tertiary_parse(parent, current, child):
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
        elif current == 3 and child == 7:
            return "a"
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

def parse_path(P, h, w):
    M = [["0" for _ in range(w)] for _ in range(h)]
    if P[0][2] == 1:
        M[P[0][1]][P[0][0]] = "s"
    elif P[0][2] == 2:
        M[P[0][1]][P[0][0]] = "j"
    elif P[0][2] == 3:
        M[P[0][1]][P[0][0]] = "i"
    elif P[0][2] == 4:
        M[P[0][1]][P[0][0]] = "h"

    for i in range(1, len(P) - 1):
        M[P[i][1]][P[i][0]] = tertiary_parse(P[i - 1][2], P[i][2], P[i + 1][2])

    if P[len(P) - 1][2] == 5:
        M[P[len(P) - 1][1]][P[len(P) - 1][0]] = "i"
    elif P[len(P) - 1][2] == 6:
        M[P[len(P) - 1][1]][P[len(P) - 1][0]] = "h"
    elif P[len(P) - 1][2] == 7:
        M[P[len(P) - 1][1]][P[len(P) - 1][0]] = "s"
    elif P[len(P) - 1][2] == 8:
        M[P[len(P) - 1][1]][P[len(P) - 1][0]] = "j"

    return M


def get_mat_child(M, x, y):
    if M[y][x] == 1:
        return M[y - 1][x]
    if M[y][x] == 2:
        return M[y][x + 1]
    if M[y][x] == 3:
        return M[y + 1][x]
    if M[y][x] == 4:
        return M[y][x - 1]
