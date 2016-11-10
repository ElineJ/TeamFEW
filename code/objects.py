# Code for the game rush hour
#
# Sets up vehicles (trucks and cars) and a grid for the game


import numpy as np

import visualize
import pylab


class Position(object):


class Grid(object):
    """
    Sets up a grid for the game with a given width and height

    Exit: the position of the exit
    all_vehicles: an array of all the vehicle positions on the board
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

    def isPositioninGrid(self, pos):
        """
        Checks if a position is in the grid

        Returns True if it is, False if it isn't
        """
        if 0 > vehicle.x1 <= self.width and 0 > vehicle.x2 <= self.width and 0 > vehicle.y1 < self.height and 0 > vehicle.y1 < self.height:
            return True
        return False

class Vehicle(object):
    """
    Creates an object for a vehicle
    """
    def __init__(self, x1, x2, y1, y2):

        # kan eigenlijk niet hier omdat trucks 3 lang zijn
        self.pos = position
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def getVehiclePosition(self):
        """
        Returns the current position of vehicle
        """
        return self.pos

    def setVehiclePosition(self, x1, x2, y1, y2):

        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        # niet erg mooi

class Hcar(Vehicle):
    def __init__(self):

    def movement(self):
