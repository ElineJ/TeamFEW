# main code to run the simulation
# import visualize
import sys      # imports the sys module

from positions import *
from grid import *
from car import *
from truck import *
from csvtries import *
from bfs import *

# open csv file
f = open(sys.argv[1], 'rb')

#
exit = CarPosition(4, 2, 5, 2)
width = int(sys.argv[2])

grid = run(f, width, width, exit)
print grid.all_vehicles[0].orientation
f.close()

runbfs(grid.all_vehicles, exit)
