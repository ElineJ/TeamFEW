"""
rdom.py: Algorithm that loops through all vehicles and moves each vehicle
in a random direction (up/down or left/right) until it finds an exit.
"""

import random
import time


def runrandom(grid):
    """
    Sets up a timer and runs the rndom algorithm
    """
    start_time = time.time()
    vehicles = grid.vehicles
    moves = 0
    not_at_exit = True

    while not_at_exit:
        for vehicle in vehicles:
            number = random.randint(0, 1)
            # move vertical vehicle in a random direction
            if vehicle.orientation == 'V':
                v_direction = [vehicle.up, vehicle.down]
                if v_direction[number](grid):
                    moves += 1
            # move horizontal vehicle into a random direction
            elif vehicle.orientation == 'H':
                h_direction = [vehicle.left, vehicle.right]
                if h_direction[number](grid):
                    moves += 1
                    if grid.car_at_exit(vehicle.pos):
                        print "Moves:", moves
                        print "--- %s seconds ---" % (time.time() - start_time)
                        not_at_exit = False
