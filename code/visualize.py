# Visualization code for the game Rush hour

from Tkinter import *
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt

all_vehicles = []

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

class Car(object):
    """
    Creates an object for a vehicle type of car
    """
    def __init__(self, x1, x2, y1, y2, orientation, color):
        self.orientation = orientation
        self.color = color
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

def makeCars():
    car = Car(0, 0, 0, 1, 'V', 'blue')
    if car.color == 'blue':
        car.color = '#5981F3'
    all_vehicles.append(car)
    car2 = Car(4, 5, 4, 4, 'H', 'orange')
    if car2.color == 'orange':
        car2.color = '#E99F62'
    all_vehicles.append(car2)
    car3 = Car(2, 3, 2, 2, 'H', 'red')
    if car3.color == 'red':
        car3.color = '#B63339'
    all_vehicles.append(car3)
    car4 = Car(1, 2, 5, 5, 'H', 'blue')
    if car4.color == 'blue':
        car4.color = '#5981F3'
    all_vehicles.append(car4)


def makeCars2():
    all_vehicles = []
    car = Car(0, 0, 1, 2, 'V', 'blue')
    if car.color == 'blue':
        car.color = '#5981F3'
    all_vehicles.append(car)
    car2 = Car(4, 5, 4, 4, 'H', 'orange')
    if car2.color == 'orange':
        car2.color = '#E99F62'
    all_vehicles.append(car2)
    car3 = Car(1, 1, 1, 2, 'V', 'red')
    if car3.color == 'red':
        car3.color = '#B63339'
    all_vehicles.append(car3)


class Visualization:
    def __init__(self, width, height, delay = 0.2):

        # Number of seconds to pause after each frame
        self.delay = delay
        self.max_dim = max(width, height)
        self.width = width
        self.height = height
        self.rows = height
        self.columns = width
        self.cellwidth = 500/self.columns
        self.cellheight = 500/self.rows

        # Initialize a drawing surface
        self.master = Tk()
        self.w = Canvas(self.master, width=500, height=500)
        self.w.pack()
        self.master.update()
        self.master.title("Rush hour")

        # draw a grid
        self.rect = {}
        for column in range(0, self.columns):
            for row in range(0, self.rows):
                x1 = column * self.cellwidth
                y1 = row * self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight
                self.rect[row, column] = self.w.create_rectangle(x1,y1,x2,y2, fill="#363958", tags="rect")

        # draw vehicles
        for i in range(0, len(all_vehicles)):
            x1, y1 = all_vehicles[i].x1 * self.cellwidth, all_vehicles[i].y1 * self.cellheight
            if all_vehicles[i].orientation == 'V':
                x2, y2 = x1 + self.cellwidth, y1 + 2 * self.cellheight
            else:
                x2, y2 = x1 + 2 * self.cellwidth, y1 + self.cellheight
            self.rect[all_vehicles[1].x1, all_vehicles[i].y1] = self.w.create_rectangle(x1, y1, x2, y2, fill = all_vehicles[i].color)
            print "x1, y1: ", x1, y1
            print "x2, y2: ", x2, y2


    def update():

        # Delete all existing vehicles
        for vehicle in all_vehicles:
            self.w.delete(vehicle)
            self.master.update_idletasks()

            # Draw new vehicles
            for i in range(0, len(all_vehicles)):
                x1, y1 = all_vehicles[i].x1 * self.cellwidth, all_vehicles[i].y1 * self.cellheight
                if all_vehicles[i].orientation == 'V':
                    x2, y2 = x1 + self.cellwidth, y1 + 2 * self.cellheight
                else:
                    x2, y2 = x1 + 2 * self.cellwidth , y1 + self.cellheight
                self.rect[all_vehicles[1].x1, all_vehicles[i].y1] = self.w.create_rectangle(x1, y1, x2, y2, fill = all_vehicles[i].color)
                print "x1, y1: ", x1, y1
                print "x2, y2: ", x2, y2
