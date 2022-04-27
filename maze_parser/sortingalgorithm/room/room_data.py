class room_data:
    def __init__(self):
        self.__edges = [1 for _ in range(4)]
    def get_edges(self):
        return self.__edges
    def set_edges(self, edges):
        self.__edges = edges
    def turn_off_up(self):
        self.__edges[0] = 0;
    def turn_off_right(self):
        self.__edges[1] = 0;
    def turn_off_down(self):
        self.__edges[2] = 0;
    def turn_off_left(self):
        self.__edges[3] = 0;
    def turn_on_up(self):
        self.__edges[0] = 1;
    def turn_on_right(self):
        self.__edges[1] = 1;
    def turn_on_down(self):
        self.__edges[2] = 1;
    def turn_on_left(self):
        self.__edges[3] = 1;
