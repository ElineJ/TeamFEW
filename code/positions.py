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
        self.x = x
        self.y = y


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

    def getX(self):
        x = [self.x1, self.x2]
        return x

    def getY(self):
        y = [self.y1, self.y2]
        return y


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
        self.y1 = int(y1)
        self.y2 = int(y2)
        self.x3 = int(x3)
        self.y3 = int(y3)

    def getX(self):
        x = [self.x1, self.x2, self.x3]
        return x

    def getY(self):
        y = [self.y1, self.y2, self.y3]
        return y
