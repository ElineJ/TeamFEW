from grid import *
from car import *
from truck import *
import random

def runrandom(grid, exit):

    v_direction = ["up", "down"]
    h_direction = ["left", "right"]

    while True:
        for i in range(0, len(grid.all_vehicles)):
            if isinstance(all_vehicles[i], Car):
                direction = random.randint(0, 1)


            elif isinstance(all_vehicles[i], Truck):
                direction = random.randint(0, 360)
