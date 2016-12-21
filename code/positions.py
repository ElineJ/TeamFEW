# All position objects for rush hour
# === Position classes


class GridPosition(object):
    """
    A Position representing the empty position on the grid
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = int(x)
        self.y = int(y)
        self.id = str(x) + str(y)

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.id)


class CarPosition(object):
    """
    A Position represents a position on the grid
    """
    def __init__(self, x1, x2, y1, y2):
        """
        Initializes a position with coordinates (x, x, y, y).
        """
        self.x1 = int(x1)
        self.x2 = int(x2)
        self.y1 = int(y1)
        self.y2 = int(y2)
        self.id = str(x1) + str(x2) + str(y1) + str(y2)

    def __eq__(self, other):
        return (self.x1 == other.x1 and
                self.x2 == other.x2 and
                self.y1 == other.y1 and
                self.y2 == other.y2)

    def __ne__(self, other):
        return not self.__eq__(other)

    # def getX(self):
    #     x = [self.x1, self.x2]
    #     return x
    #
    # def getY(self):
    #     y = [self.y1, self.y2]
    #     return y


class TruckPosition(object):
    """
    A Position represents a position on the grid
    """
    def __init__(self, x1, x2, x3, y1, y2, y3):
        """
        Initializes a position with coordinates (x, x, x, y, y, y).
        """
        self.x1 = int(x1)
        self.x2 = int(x2)
        self.x3 = int(x3)
        self.y1 = int(y1)
        self.y2 = int(y2)
        self.y3 = int(y3)
        self.id = (str(x1) + str(x2) + str(x3) +
                  str(y1) + str(y2) + str(y3))

    def __eq__(self, other):
        return (self.x1 == other.x1 and
                self.x2 == other.x2 and
                self.x3 == other.x3 and
                self.y1 == other.y1 and
                self.y2 == other.y2 and
                self.y3 == other.y3)

    def __ne__(self, other):
        return not self.__eq__(other)

    # def getX(self):
    #     x = [self.x1, self.x2, self.x3]
    #     return x
    #
    # def getY(self):
    #     y = [self.y1, self.y2, self.y3]
    #     return y
