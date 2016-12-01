# main code to run the simulation
# import visualize
from visualize import *
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

# set up grid with vehicles
grid = run(f, width, width, exit)
f.close()

# open visualization
anim = Visualization(width, width, grid.all_vehicles)

runbfs(grid, exit)
# anim.update()
