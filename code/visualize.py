# Visualization code for the game Rush hour
#
#

import math
import time

from Tkinter import *
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt

class Visualization:
    def __init__(self, width, height, delay = 0.2):
        "Initializes a visualization with the specified parameters."
        # Number of seconds to pause after each frame
        self.delay = delay

        self.max_dim = max(width, height)
        self.width = width
        self.height = height

        # Initialize a drawing surface
        self.master = Tk()
        self.w = Canvas(self.master, width=500, height=500)
        self.w.pack()
        self.master.update()

        # Draw a backing and lines
        x1, y1 = self._map_coords(0, 0)
        x2, y2 = self._map_coords(width, height)
        self.w.create_rectangle(x1, y1, x2, y2, fill = "white")

        # Draw gray squares for dirty tiles
        self.tiles = {}
        for i in range(width):
            for j in range(height):
                x1, y1 = self._map_coords(i, j)
                x2, y2 = self._map_coords(i + 1, j + 1)
                self.tiles[(i, j)] = self.w.create_rectangle(x1, y1, x2, y2,
                                                             fill = "#dbe8ff")

        # Draw

        # Draw gridlines
        for i in range(width + 1):
            x1, y1 = self._map_coords(i, 0)
            x2, y2 = self._map_coords(i, height)
            self.w.create_line(x1, y1, x2, y2)
        for i in range(height + 1):
            x1, y1 = self._map_coords(0, i)
            x2, y2 = self._map_coords(width, i)
            self.w.create_line(x1, y1, x2, y2)

        # draw shapes for cars
        x1, y1 = self._map_coords(0, 0)
        x2, y2 = self._map_coords(0, 1)
        self.w.create_rectangle(x1, y1, x2, y2, fill="red")

        # Draw some status text
        #self.robots = None
        #self.text = self.w.create_text(25, 0, anchor=NW,
        #                               text=self._status_string(0, 0))
        #self.time = 0
        #self.master.update()

    def _map_coords(self, x, y):
        "Maps grid positions to window positions (in pixels)."
        return (250 + 450 * ((x - self.width / 2.0) / self.max_dim),
                250 + 450 * ((self.height / 2.0 - y) / self.max_dim))

    def done(self):
        "Indicate that the animation is done so that we allow the user to close the window."
        mainloop()
