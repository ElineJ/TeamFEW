import random
import time
# import visualize as vis
import car
import truck


# @profile
def runrandom(grid, exit):
    """
    Algorithm that loops through all vehicles and moves each vehicle
    in a random direction (up/down or left/right) until it finds and exit.
    Skips positions the grid has already been in.
    """
    start_time = time.time()
    v_direction = ["up", "down"]
    h_direction = ["left", "right"]
    vehicles = grid.vehicles
    moves = 0
    results = []
    not_at_exit = True
    # make a list of all states that have happened
    dictionary = {}
    # set up visualization
    # if exit.x == 5:
    #     width = 6
    # elif exit.x == 8:
    #     width = 9
    # else:
    #     width = 12
    string = make_string(vehicles)
    add_dictionary(string, dictionary)
    # open window with visualization
    # anim = vis.Visualization(width, width, vehicles)

    while not_at_exit:
        for vehicle in vehicles:
            number = random.randint(0, 1)
            # move vertical car in a random direction
            if vehicle.orientation == 'V':
                direction = v_direction[number]
                if vehicle.move(direction, grid):
                    check = make_string(vehicles)
                    if check not in dictionary:
                        moves += 1
                        add_dictionary(check, dictionary)
                        # anim.update(vehicles)
            # move horizontal car into a random direction
            elif vehicle.orientation == 'H':
                direction = h_direction[number]
                if vehicle.move(direction, grid):
                    check = make_string(vehicles)
                    if check not in dictionary:
                        moves += 1
                        add_dictionary(check, dictionary)
                        # anim.update(vehicles)
                        # check if car is at exit
                        if grid.car_at_exit(vehicle.pos):
                            # print "Found exit!"
                            del results[:]
                            results.append(moves)
                            results.append("%.6s" % (time.time() - start_time))
                            print "Moves:", moves
                            print("--- %s seconds ---" % (time.time() - start_time))
                            # print moves,("%s seconds" % (time.time() - start_time))
                            return results
    # anim.done()


def make_string(vehicles):
    """
    Creates a unique string of the position coordinates
    of all vehicles in the current grid.
    """
    string = ""
    for vehicle in vehicles:
        string = string + str(vehicle)
    return string


def add_dictionary(string, dictionary):
    """
    Adds unique string of vehicle positions to
    dictionary to track visited set-ups
    """
    dict2 = {string: True}
    dictionary.update(dict2)
