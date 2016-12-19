import sys
import positions as pos
import csvtries
import bfs
import rndom as rd
from copy import deepcopy

import csv

# open csv file
f = open(sys.argv[1], 'rb')
width = int(sys.argv[2])
height = width
num_runs = int(sys.argv[3])

# check which exit to use
if width == 6:
    exit = pos.GridPosition(5, 2)
elif width == 9:
    exit = pos.GridPosition(8, 4)
elif width == 12:
    exit = pos.GridPosition(11, 5)

# set up grid with vehicles
grid_rnd = csvtries.run(f, width, height, exit)
# grid_bfs = deepcopy(grid_rnd)
f.close()

for i in range(0, num_runs):
    new_grid = deepcopy(grid_rnd)
    # print "--- Random algoritme ---"
    result = rd.runrandom(new_grid, exit)
    # print result
    # add result to csv file
    with open('../results/test.csv', 'a') as testFile:
        testFileWriter = csv.writer(testFile)
        testFileWriter.writerow(result)

print "done"
