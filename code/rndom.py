import random
import time
# import visualize as vis


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

    # open window with visualization
    # anim = vis.Visualization(width, width, vehicles)
    while not_at_exit:
        for i in range(0, len(vehicles)):
            number = random.randint(0, 1)
            # move vertical car in a random direction
            if vehicles[i].orientation == 'V':
                direction = v_direction[number]
                if vehicles[i].checkMove(direction, grid):
                    vehicles[i].move(direction, grid)
                    moves += 1
                    # anim.update(vehicles)
            # move horizontal car into a random direction
            else:
                direction = h_direction[number]
                if vehicles[i].checkMove(direction, grid):
                    vehicles[i].move(direction, grid)
                    moves += 1
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
