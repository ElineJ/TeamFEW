# main code to run the simulation

import positions
import grid
import truck
import car
import visualize
from csvtries import *
import sys      # imports the sys module

# open csv file
f = open(sys.argv[1], 'rb')

# get grid size
s = sys.argv[2]

w = int(s)

exit = positions.CarPosition(4, 2, 5, 2)

print s

run(f, w, w, exit)

print newGrid.all_vehicles[0].color

position = newGrid.all_vehicles[0].getCarPosition
newGrid.all_vehicles[0].moveCar(position, )

f.close()
