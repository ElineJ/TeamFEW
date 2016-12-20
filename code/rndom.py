import random
import time
import visualize as vis


# @profile
def runrandom(grid, exit):
    """
    Algorithm that loops through all vehicles and moves each vehicle
    in a random direction (up/down or left/right) until it finds and exit.
    """
    start_time = time.time()
    v_direction = ["up", "down"]
    h_direction = ["left", "right"]
    vehicles = grid.vehicles
    moves = 0
    results = []
    not_at_exit = True
    # print "Exit:", exit.x, exit.y
    # set up visualization
    # if exit.x == 5:
    #     width = 6
    # elif exit.x == 8:
    #     width = 9
    # else:
    #     width = 12

    # open window with visualization
    # anim = vis.Visualization(width, width, vehicles)
    while not_at_exit:
        for i in range(0, len(vehicles)):
            number = random.randint(0, 1)
            # move vertical car in a random direction
            if vehicles[i].orientation == 'V':
                direction = v_direction[number]
                if vehicles[i].move(direction, grid) != False:
                    # print "Test"
                    moves += 1
                    # anim.update(vehicles)
            # move horizontal car into a random direction
            elif vehicles[i].orientation == 'H':
                direction = h_direction[number]
                if vehicles[i].move(direction, grid) != False:
                    moves += 1
                    # print moves
                    # anim.update(vehicles)
                    # check if car is at exit
                    if vehicles[i].pos.x2 == exit.x and vehicles[i].pos.y2 == exit.y:
                        print "Found exit!"
                        print "Moves:", moves
                        # del results[:]
                        results.append(moves)
                        results.append("%.6s" % (time.time() - start_time))
                        # print moves,("%s seconds" % (time.time() -
                        # start_time))
                        return results

    # anim.done()
