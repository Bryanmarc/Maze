class Coords(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get(self):
        return str(self.x) + ", " + str(self.y)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y
