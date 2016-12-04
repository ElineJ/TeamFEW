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

#
exit = pos.CarPosition(4, 2, 5, 2)
width = int(sys.argv[2])

# set up grid with vehicles
grid = csvtries.run(f, width, width, exit)
f.close()

# open visualization
# anim = vis.Visualization(width, width, grid.all_vehicles)
print "--- Random algoritme ---"
rd.runrandom(grid, exit)
print "--- bfs ---"
bfs.runbfs(grid, exit)
