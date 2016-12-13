import visualize as vis
import grid
import car
import truck
import random
import time


def runrandom(grid, exit):
    start_time = time.time()
    v_direction = ["up", "down"]
    h_direction = ["left", "right"]
    vehicles = grid.all_vehicles
    moves = 0
    results = []

    # set up visualization
    # if exit.x == 5:
    #     width = 6
    # elif exit.x == 9:
    #     width = 9
    # else:
    #     width = 12

    # open window with visualization
    # anim = vis.Visualization(width, width, vehicles)
    while True:
        for i in range(0, len(vehicles)):
            if isinstance(vehicles[i], car.Car):
                direction = random.randint(0, 1)
                # move vertical car in a random direction
                if vehicles[i].orientation == 'V':
                    d = v_direction[direction]
                    if vehicles[i].checkMove(d, grid):
                        vehicles[i].moveCar(d, grid)
                        moves += 1
                        # anim.update(vehicles)
                # move horizontal car into a random direction
                else:
                    d = h_direction[direction]
                    if vehicles[i].checkMove(d, grid):
                        vehicles[i].moveCar(d, grid)
                        moves += 1
                        # anim.update(vehicles)
                        # check if car is at exit
                        if vehicles[i].pos.x2 == exit.x and vehicles[i].pos.y2 == exit.y:
                            # print "Found exit!"
                            # print "Moves:", moves
                            # print("--- %s seconds ---" % (time.time() - start_time))
                            # del results[:]
                            results.append(moves)
                            results.append("%.6s" % (time.time() - start_time))
                            # print moves,("%s seconds" % (time.time() - start_time))
                            return results

            elif isinstance(vehicles[i], truck.Truck):
                direction = random.randint(0, 1)
                # move vertical truck in a random direction
                if vehicles[i].orientation == 'V':
                    d = v_direction[direction]
                    if vehicles[i].checkMove(d, grid):
                        vehicles[i].moveTruck(d, grid)
                        moves += 1
                        # anim.update(vehicles)
                # move horizontal truck into a random direction
                else:
                    d = h_direction[direction]
                    if vehicles[i].checkMove(d, grid):
                        vehicles[i].moveTruck(d, grid)
                        moves += 1
                        # anim.update(vehicles)

    # anim.done()
