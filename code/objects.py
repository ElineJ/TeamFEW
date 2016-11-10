# Code for the game rush hour
#
# Sets up vehicles (trucks and cars) and a grid for the game


import numpy as np
#from matplotlib import mpl, pyplot

import visualize
import pylab

# === Position classes

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
        self.width = width
        self.height = height
        self.exit = exit
        all_vehicles = []
        self.all_vehicles = all_vehicles

    def isRedOnExit(self, pos):
        """
        Checks if the red car is at the exit

        Returns True if it is, False if it isn't
        """
        if pos == self.exit:
            return True
        return False

    def isPositionInGrid(self, pos):
        """
        Checks if a position is in the grid

        Returns True if it is, False if it isn't
        """
        if (0 > pos.x1 <= self.width) and (0 > pos.x2 <= self.width) and (0 > pos.y1 <= self.height) and (0 > pos.y2 <= self.height):
            return True
        else:
            return False

# === Vehicles

class Car(object):
    """
    Creates an object for a vehicle type of car
    """
    def __init__(self, x1, x2, y1, y2, orientation, color):
        position = CarPosition(x1, x2, y1, y2)
        self.pos = position
        self.orientation = orientation
        self.color = color

    def getCarPosition(self):
        """
        Returns the current position of vehicle
        """
        return self.pos

    def setCarPosition(self, position):
        """
        Set the position of the car to position

        position: a Position object.
        """
        self.pos = position

    def moveCar(self, position):
        """
        Moves car to new position
        """

        # check if position is on the grid


        # move vertical car right
        if self.orientation == 'V':
            y1 = self.pos.y1 + 1
            y2 = self.pos.y2 + 1
            new_pos = CarPosition(self.pos.x1, self.pos.x2, y1, y2)
            self.setCarPosition(new_pos)
        # move horizontal car up
        else:
            x1 = self.pos.x1 + 1
            x2 = self.pos.x2 + 1
            new_pos = CarPosition(x1, x2, self.pos.y1, self.pos.y2)
            self.setCarPosition(new_pos)

        # move vertical car left
        if self.orientation == 'H':
            y1 = self.pos.y1 - 1
            y2 = self.pos.y2 - 1
            new_pos = CarPosition(self.pos.x1, self.pos.x2, y1, y2)
            self.setCarPosition(new_pos)
        # move horizontal car down
        else:
            x1 = self.pos.x1 - 1
            x2 = self.pos.x2 - 1
            new_pos = CarPosition(x1, x2, self.pos.y1, self.pos.y2)
            self.setCarPosition(new_pos)

        # if position is on the grid, move car
        # update position in all_vehicles


class Truck(object):
    """
    Creates an object for a vehicle type of truck
    """
    def __init__(self, position, orientation, color):
        self.pos = position
        self.orientation = orientation
        self.color = color

    def getTruckPosition(self):
        """
        Returns the current position of vehicle
        """
        return self.pos

    def setTruckPosition(self, position):
        """
        Set the position of the car to position

        position: a Position object.
        """
        self.pos = position

# == run simulation

def runSimulation(width, height):
    anim = visualize.Visualization(width, height)

    anim.done()
