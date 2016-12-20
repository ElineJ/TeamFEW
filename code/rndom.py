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
    # if exit.x2 == 5:
    #     width = 6
    # elif exit.x2 == 8:
    #     width = 9
    # else:
    #     width = 12

    # open window with visualization
    # anim = vis.Visualization(width, width, vehicles)
    while not_at_exit:
        for vehicle in vehicles:
            number = random.randint(0, 1)
            # move vertical car in a random direction
            if vehicle.orientation == 'V':
                direction = v_direction[number]
                if vehicle.move(direction, grid) != False:
                    moves += 1
                    # anim.update(vehicles)
            # move horizontal car into a random direction
            elif vehicle.orientation == 'H':
                direction = h_direction[number]
                if vehicle.move(direction, grid) != False:
                    moves += 1
                    # anim.update(vehicles)
                    if grid.car_at_exit(vehicle.pos):
                        print "Found exit!"
                        print "Moves:", moves
                        print "--- %s seconds ---" % (time.time() - start_time)
                        # del results[:]
                        results.append(moves)
                        results.append("%.6s" % (time.time() - start_time))

                        return results

    # anim.done()
