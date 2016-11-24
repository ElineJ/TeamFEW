# Visualization code for the game Rush hour

from Tkinter import *
import matplotlib
matplotlib.use("TkAgg")

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
    car4 = Car(1, 2, 5, 5, 'H', 'light-blue')
    if car4.color == 'light-blue':
        car4.color = '#96D8EE'
    all_vehicles.append(car4)
    car5 = Car(4, 4, 2, 3, 'V', 'yellow')
    if car5.color == 'yellow':
        car5.color = '#D4D35F'
    all_vehicles.append(car5)

def makeCars2():
    del all_vehicles[:]
    car = Car(0, 0, 1, 2, 'V', 'blue')
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
    car4 = Car(1, 2, 5, 5, 'H', 'light-blue')
    if car4.color == 'light-blue':
        car4.color = '#96D8EE'
    all_vehicles.append(car4)
    car5 = Car(4, 4, 2, 3, 'V', 'yellow')
    if car5.color == 'yellow':
        car5.color = '#D4D35F'
    all_vehicles.append(car5)

def carColors(all_vehicles):
    for i in range(0, len(all_vehicles)):
        if all_vehicles[i].color == '':
            all_vehicles[i].color =
        elif all_vehicles[i].color == '':
            all_vehicles[i].color =
        elif all_vehicles[i].color == '':
            all_vehicles[i].color =
        elif all_vehicles[i].color == '':
            all_vehicles[i].color =        

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
        self.w = Canvas(self.master, width=505, height=500)
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

        # draw exit depending on size of field
        if width == 6:
            x1 = 6 * self.cellwidth
            y1 = 2 * self.cellheight
            x2 = 6 * self.cellwidth + 5
            y2 = y1 + self.cellheight
            self.rect[x1, y1] = self.w.create_rectangle(x1,y1,x2,y2, fill="black", tags="rect")
        # exit for 9x9 field
        if width == 9:
            x1 = 9 * self.cellwidth
            y1 = 4 * self.cellheight
            x2 = 9 * self.cellwidth + 5
            y2 = y1 + self.cellheight
            self.rect[x1, y1] = self.w.create_rectangle(x1,y1,x2,y2, fill="black", tags="rect")
        # exit for 12x12 field
        if width == 12:
            x1 = 12 * self.cellwidth
            y1 = 5 * self.cellheight
            x2 = 12 * self.cellwidth + 5
            y2 = y1 + self.cellheight
            self.rect[x1, y1] = self.w.create_rectangle(x1,y1,x2,y2, fill="black", tags="rect")

        # draw vehicles
        for i in range(0, len(all_vehicles)):
            x1, y1 = all_vehicles[i].x1 * self.cellwidth, all_vehicles[i].y1 * self.cellheight
            if all_vehicles[i].orientation == 'V':
                x2, y2 = x1 + self.cellwidth, y1 + 2 * self.cellheight
            else:
                x2, y2 = x1 + 2 * self.cellwidth, y1 + self.cellheight
            self.rect[all_vehicles[1].x1, all_vehicles[i].y1] = self.w.create_rectangle(x1, y1, x2, y2, fill = all_vehicles[i].color)

    def update(self):
        # Delete all existing vehicles
        for vehicle in all_vehicles:
            self.w.delete(vehicle)
            self.master.update_idletasks()

        # draw new empty grid
        self.rect = {}
        for column in range(0, self.columns):
            for row in range(0, self.rows):
                x1 = column * self.cellwidth
                y1 = row * self.cellheight
                x2 = x1 + self.cellwidth
                y2 = y1 + self.cellheight
                self.rect[row, column] = self.w.create_rectangle(x1,y1,x2,y2, fill="#363958", tags="rect")

        # Draw new vehicles
        for i in range(0, len(all_vehicles)):
            x1, y1 = all_vehicles[i].x1 * self.cellwidth, all_vehicles[i].y1 * self.cellheight
            if all_vehicles[i].orientation == 'V':
                x2, y2 = x1 + self.cellwidth, y1 + 2 * self.cellheight
            else:
                x2, y2 = x1 + 2 * self.cellwidth , y1 + self.cellheight
            self.rect[all_vehicles[1].x1, all_vehicles[i].y1] = self.w.create_rectangle(x1, y1, x2, y2, fill = all_vehicles[i].color)
