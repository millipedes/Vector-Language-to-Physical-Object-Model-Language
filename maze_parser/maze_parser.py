def dual_parser(parent, current):
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
