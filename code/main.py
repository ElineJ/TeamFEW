#!/usr/bin/env python
# usage of file:
# python main.py <game number (1-7)>

# main code to run the simulation
import sys
sys.dont_write_bytecode = True
import rndom as rd
from copy import deepcopy
import positions as pos
import csvtries
import bfs
# import visualize as vis

# array of all files for the games
games = ['none', '../datasets/Game #1.csv', '../datasets/Game #2.csv',
   '../datasets/Game #3.csv', '../datasets/Game #4.csv', '../datasets/Game #5.csv',
   '../datasets/Game #6.csv', '../datasets/Game #7.csv']

# check if game exists, open file for game
game = int(sys.argv[1])
if game == 0 or game > 7:
    sys.exit("Game does not exist, choose 1 - 7")
else:
    f = open(games[game], 'rb')

# set up exits for each of the games
if game == 1 or game == 2 or game == 3:
    exit = pos.GridPosition(5, 2)
    width, height = 6, 6
elif game == 4 or game == 5 or game == 6:
    exit = pos.GridPosition(8, 4)
    width, height = 9, 9
elif game == 7:
    exit = pos.GridPosition(11, 5)
    width, height = 12, 12

# set up grid with vehicles
grid_rnd = csvtries.run(f, width, height, exit)
grid_bfs = deepcopy(grid_rnd)
f.close()

# open visualization
# anim = vis.Visualization(width, width, grid.vehicles)
print "--- Random algoritme ---"
rd.runrandom(grid_rnd, exit)
print "--- bfs ---"
bfs.runbfs(grid_bfs, exit)
