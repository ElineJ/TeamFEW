# Code for the game rush hour
#
# Sets up vehicles (trucks and cars) and a grid for the game


import numpy as np
#from matplotlib import mpl, pyplot

import visualize
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
    all_vehicles = []

    def __init__(self, width, height, exit):
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
        # Grid.all_vehicles.append(self.pos)

    def getCarPosition(self):
        """
        Returns the current position of vehicle
        """
        return self.pos

    def setCarPosition(self, old_pos, new_pos):
        """
        Set the position of the car to position

        position: a Position object.
        """
        for i in range(0, len(Grid.all_vehicles)):
            if Grid.all_vehicles[i] == old_pos:
                Grid.all_vehicles[i] = new_pos
        self.pos = new_pos
    def moveCar(self, position, direction):
        """
        Moves car to new position
        """
        old_pos = self.getCarPosition()

        if direction == 'right' or direction == 'up':
            # move vertical car up

            if self.orientation == 'V':

                y1 = self.pos.y1 - 1
                y2 = self.pos.y2 - 1
                new_pos = CarPosition(self.pos.x1, self.pos.x2, y1, y2)
                check_pos = GridPosition(self.pos.x1, y1)
                empty_pos = GridPosition(self.pos.x1, self.pos.y2)
                if Grid.isPositionEmpty(check_pos):
                    Grid.updateEmptyPosition(check_pos, empty_pos)
                    self.setCarPosition(old_pos, new_pos)
                else:
                    print("dit kan dus niet he")

            # move horizontal car right
            else:
                x1 = self.pos.x1 + 1
                x2 = self.pos.x2 + 1
                new_pos = CarPosition(x1, x2, self.pos.y1, self.pos.y2)
                check_pos = GridPosition(x2, self.pos.y2)
                empty_pos = GridPosition(self.pos.x1, self.pos.y1)
                if Grid.isPositionEmpty(check_pos):
                    Grid.updateEmptyPosition(check_pos, empty_pos)
                    self.setCarPosition(old_pos, new_pos)
                else:
                    print("dit kan dus niet he")

        elif direction == 'left' or direction == 'down':

            # move vertical car down
            if self.orientation == 'V':
                y1 = self.pos.y1 + 1
                y2 = self.pos.y2 + 1
                new_pos = CarPosition(self.pos.x1, self.pos.x2, y1, y2)
                check_pos = GridPosition(self.pos.x2, y2)
                empty_pos = GridPosition(self.pos.x1, self.pos.y1)
                if Grid.isPositionEmpty(check_pos):
                    Grid.updateEmptyPosition(check_pos, empty_pos)
                    self.setCarPosition(old_pos, new_pos)
                else:
                    print("dit kan dus niet he")

            # move horizontal car left
            else:
                x1 = self.pos.x1 - 1
                x2 = self.pos.x2 - 1
                new_pos = CarPosition(x1, x2, self.pos.y1, self.pos.y2)
                check_pos = GridPosition(x1, self.pos.y1)
                empty_pos = GridPosition(self.pos.x2, self.pos.y2)
                if Grid.isPositionEmpty(check_pos):
                    Grid.updateEmptyPosition(check_pos, empty_pos)
                    self.setCarPosition(old_pos, new_pos)
                else:
                    print("dit kan dus niet he")

        # TODO: update position in all_vehicles?


class Truck(object):
    """
    Creates an object for a vehicle type of truck
    """
    def __init__(self, x1, x2, x3, y1, y2, y3, orientation, color):
        position = TruckPosition(x1, x2, x3, y1, y2, y3)
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

    def moveTruck(self, position, direction):
        """
        Moves truck to new position
        """
        if direction == 'right' or direction == 'down':
            # move vertical car down
            if self.orientation == 'V':
                y1 = self.pos.y1 + 1
                y2 = self.pos.y2 + 1
                y3 = self.pos.y3 + 1
                new_pos = CarPosition(self.pos.x1, self.pos.x2, self.pos.x3, y1, y2, y3)
                self.setCarPosition(new_pos)
                check_pos = GridPosition(x1, self.pos.y1)
                empty_pos = GridPosition(self.pos.x2, self.pos.y2)
                if Grid.isPositionEmpty(check_pos):
                    Grid.updateEmptyPosition(check_pos, empty_pos)
                    self.setCarPosition(old_pos, new_pos)
                else:
                    print("dit kan dus niet he")
            # move horizontal car right
            else:
                x1 = self.pos.x1 + 1
                x2 = self.pos.x2 + 1
                x3 = self.pos.x3 + 1
                new_pos = CarPosition(x1, x2, x3, self.pos.y1, self.pos.y2, self.pos.y3)
                self.setCarPosition(new_pos)

        elif direction == 'left' or direction == 'up':
            # move vertical car up
            if self.orientation == 'V':
                y1 = self.pos.y1 - 1
                y2 = self.pos.y2 - 1
                y3 = self.pos.y3 - 1
                new_pos = CarPosition(self.pos.x1, self.pos.x2, self.pos.x3, y1, y2, y3)
                self.setCarPosition(new_pos)
            # move horizontal car left
            else:
                x2 = self.pos.x2 - 1
                x1 = self.pos.x1 - 1
                x3 = self.pos.x3 - 1
                new_pos = CarPosition(x1, x2, x3, self.pos.y1, self.pos.y2, self.pos.y3)
                self.setCarPosition(new_pos)

        # TODO: update position in all_vehicles?

# == run simulation

def runSimulation(width, height):
    anim = visualize.Visualization(width, height)
    anim.done()
