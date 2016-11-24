# All position objects for rush hour

import numpy as np
import pylab

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

    def getX(self):
        return self.x

    def getY(self):
        return self.y

class CarPosition(object):
    """
    A Position represents a position on the grid
    """
    def __init__(self, x1, x2, y1, y2):
        """
        Initializes a position with coordinates (x, x, y, y).
        """
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
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
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
    def getX(self):
        x = [self.x1, self.x2, self.x3]
        return x
    def getY(self):
        y = [self.y1, self.y2, self.y3]
        return y

# === Grid

class Grid(object):
    """
    Sets up a grid for the game with a given width and height

    Exit: the position of the exit
    all_vehicles: an array of all the vehicle position objects on the board
    """


    def __init__(self, width, height, exit):
        all_vehicles = []
        self.width = width
        self.height = height
        self.exit = exit
        self.all_vehicles = all_vehicles
        empty_grid = []
        self.empty_grid = empty_grid
        for i in range(0, height):
            for j in range(0, width):
                new_grid = GridPosition(i, j)
                empty_grid.append(new_grid)

        for i in range(0, len(self.all_vehicles)):
            empty_pos1 = GridPosition(all_vehicles[i].x1, all_vehicles[i].y1)
            empty_pos2 = GridPosition(all_vehicles[i].x2, all_vehicles[i].y2)
            empty_pos3 = GridPosition(all_vehicles[i].x3, all_vehicles[i].y3)

            for j in range(0, len(self.empty_grid)):
                if self.empty_grid[j] == empty_pos1 or self.empty_grid[j] == empty_pos2 or self.empty_grid[j] == empty_pos3:
                    self.empty_grid[j].remove

    def isRedOnExit(self, pos):
        """
        Checks if the red car is at the exit

        Returns True if it is, False if it isn't
        """
        if pos == self.exit:
            return True
        return False

    def isPositionEmpty(self, pos):
        print pos.x
        print pos.y
        for i in range(0, len(self.empty_grid)):

            if pos.x == self.empty_grid[i].x and pos.y == self.empty_grid[i].y:
                return True
        return False

    def updateEmptyPosition(self, pos, new_pos):
        for i in range(0, len(self.empty_grid)):
            if pos == self.empty_grid[i]:
                self.empty_grid[i] = new_pos
