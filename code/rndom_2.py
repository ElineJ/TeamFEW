"""
Algorithm that loops through all vehicles and moves each vehicle
in a random direction (up/down or left/right) until it finds and exit.
Skips positions the grid has already been in, by saving strings of
positions in a dictionary.
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
    dictionary = {}

    # make string of inital grid
    string = make_string(vehicles)
    add_dictionary(string, dictionary)

    while not_at_exit:
        for vehicle in vehicles:
            number = random.randint(0, 1)
            # move vertical car in a random direction
            if vehicle.orientation == 'V':
                v_direction = [vehicle.up, vehicle.down]
                if v_direction[number](grid):
                    check = make_string(vehicles)
                    if check not in dictionary:
                        moves += 1
                        add_dictionary(check, dictionary)
            # move horizontal car into a random direction
            elif vehicle.orientation == 'H':
                h_direction = [vehicle.left, vehicle.right]
                if h_direction[number](grid):
                    check = make_string(vehicles)
                    if check not in dictionary:
                        moves += 1
                        add_dictionary(check, dictionary)
                        if grid.car_at_exit(vehicle.pos):
                            print "Steps:", moves
                            print "--- %s seconds ---" % (time.time() - start_time)
                            not_at_exit = False


def make_string(vehicles):
    """
    Creates a unique string of the position coordinates
    of all vehicles in the current grid.
    """
    return ''.join([str(vehicle) for vehicle in vehicles])


def add_dictionary(string, dictionary):
    """
    Adds unique string of vehicle positions to
    dictionary to track visited set-ups
    """
    dict2 = {string: True}
    dictionary.update(dict2)
