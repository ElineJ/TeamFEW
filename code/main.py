# main code to run the simulation
import visualize as vis
import sys

import positions as pos
import grid
import csvtries
import bfs
import rndom as rd

# open csv file
f = open(sys.argv[1], 'rb')

width = int(sys.argv[2])

# check which exit to use
if width == 6:
    exit = pos.GridPosition(5, 2)
elif width == 9:
    exit = pos.GridPosition(8, 4)
elif width == 12:
    exit = pos.GridPosition(11, 5)

# set up grid with vehicles
grid = csvtries.run(f, width, width, exit)
f.close()

# open visualization
# anim = vis.Visualization(width, width, grid.all_vehicles)
print "--- Random algoritme ---"
rd.runrandom(grid, exit)
print "--- bfs ---"
bfs.runbfs(grid, exit)
