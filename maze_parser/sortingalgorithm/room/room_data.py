class room_data:
    def __init__(self, *args, **kwargs):
        if 'edges' in kwargs:
            self.__edges = kwargs.get('edges')
        else:
            self.__edges = [1 for _ in range(4)]
    def get_edges(self):
        return self.__edges
    def set_edges(self, edges):
        self.__edges = edges
