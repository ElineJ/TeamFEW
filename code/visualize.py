# Visualization code for the game Rush hour

from Tkinter import *
import matplotlib
matplotlib.use("TkAgg")
from car import *
from truck import *

def carColors(all_vehicles):
    for i in range(0, len(all_vehicles)):
        if all_vehicles[i].color == 'blue':
            all_vehicles[i].color = '#5981F3'
        elif all_vehicles[i].color == 'red':
            all_vehicles[i].color = '#B63339'
        elif all_vehicles[i].color == 'orange':
            all_vehicles[i].color = '#E99F62'
        elif all_vehicles[i].color == 'light-blue':
            all_vehicles[i].color = '#96D8EE'
        elif all_vehicles[i].color == 'yellow':
            all_vehicles[i].color = '#D4D35F'
        elif all_vehicles[i].color == 'dark-yellow':
            all_vehicles[i].color = '#AEAE00'
        elif all_vehicles[i].color == 'purple':
            all_vehicles[i].color = '#A38AFF'
        elif all_vehicles[i].color == 'grey':
            all_vehicles[i].color = '#999999'
        elif all_vehicles[i].color == 'green':
            all_vehicles[i].color = '#4091A2'


class Visualization:
    def __init__(self, width, height, all_vehicles, delay = 0.2):

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

        # change car colors
        carColors(all_vehicles)

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
            if isinstance(all_vehicles[i], Car):
                x1, y1 = int(all_vehicles[i].pos.x1) * self.cellwidth, int(all_vehicles[i].pos.y1) * self.cellheight
                if all_vehicles[i].orientation == 'V':
                    x2, y2 = x1 + self.cellwidth, y1 + 2 * self.cellheight
                else:
                    x2, y2 = x1 + 2 * self.cellwidth, y1 + self.cellheight
                self.rect[all_vehicles[1].pos.x1, all_vehicles[i].pos.y1] = self.w.create_rectangle(x1, y1, x2, y2, fill = all_vehicles[i].color)
            elif isinstance(all_vehicles[i], Truck):
                x1, y1 = int(all_vehicles[i].pos.x1) * self.cellwidth, int(all_vehicles[i].pos.y1) * self.cellheight
                if all_vehicles[i].orientation == 'V':
                    x2, y2 = x1 + self.cellwidth, y1 + 3 * self.cellheight
                else:
                    x2, y2 = x1 + 3 * self.cellwidth, y1 + self.cellheight
                self.rect[all_vehicles[1].pos.x1, all_vehicles[i].pos.y1] = self.w.create_rectangle(x1, y1, x2, y2, fill = all_vehicles[i].color)

        # self.time = 0
        self.master.update()
        #self.w.mainloop()

    def update(self, all_vehicles):
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

        # change car colors
        carColors(all_vehicles)

        # Draw new vehicles
        for i in range(0, len(all_vehicles)):
            if isinstance(all_vehicles[i], Car):
                x1, y1 = int(all_vehicles[i].pos.x1) * self.cellwidth, int(all_vehicles[i].pos.y1) * self.cellheight
                if all_vehicles[i].orientation == 'V':
                    x2, y2 = x1 + self.cellwidth, y1 + 2 * self.cellheight
                else:
                    x2, y2 = x1 + 2 * self.cellwidth, y1 + self.cellheight
                self.rect[all_vehicles[1].pos.x1, all_vehicles[i].pos.y1] = self.w.create_rectangle(x1, y1, x2, y2, fill = all_vehicles[i].color)
            elif isinstance(all_vehicles[i], Truck):
                x1, y1 = int(all_vehicles[i].pos.x1) * self.cellwidth, int(all_vehicles[i].pos.y1) * self.cellheight
                if all_vehicles[i].orientation == 'V':
                    x2, y2 = x1 + self.cellwidth, y1 + 3 * self.cellheight
                else:
                    x2, y2 = x1 + 3 * self.cellwidth, y1 + self.cellheight
                self.rect[all_vehicles[1].pos.x1, all_vehicles[i].pos.y1] = self.w.create_rectangle(x1, y1, x2, y2, fill = all_vehicles[i].color)

        self.master.update()
        # time.sleep(self.delay)

    def done(self):
        "Indicate that the animation is done so that we allow the user to close the window."
        mainloop()
