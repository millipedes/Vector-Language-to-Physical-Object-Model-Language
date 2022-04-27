def dual_parse(parent, current):
    if   parent == 1:
        if current == 1:
            return "b"
        if current == 2:
            return "f"
        if current == 4:
            return "d"
    elif parent == 2:
        if current == 1:
            return "c"
        if current == 2:
            return "a"
        if current == 4:
            return "d"
    elif parent == 3:
        if current == 1:
            return "g"
        if current == 3:
            return "b"
        if current == 4:
            return "c"
    elif parent == 4:
        if current == 2:
            return "g"
        if current == 3:
            return "a"
        if current == 4:
            return "b"

def tri_path_parse(parent, current, child):
    pass
