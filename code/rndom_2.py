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
    vehicles = grid.vehicles
    moves = 0
    results = []

    # make a list of all states that have happened
    dictionary = {}
    # set up visualization
    # if exit.x == 5:
    #     width = 6
    # elif exit.x == 9:
    #     width = 9
    # else:
    #     width = 12
    string = makeString(vehicles)
    addDictionary(string, dictionary)
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
                        check = makeString(vehicles)
                        if check not in dictionary:
                            moves += 1
                            addDictionary(check, dictionary)
                            # anim.update(vehicles)
                # move horizontal car into a random direction
                else:
                    d = h_direction[direction]
                    if vehicles[i].checkMove(d, grid):
                        vehicles[i].moveCar(d, grid)
                        check = makeString(vehicles)
                        if check not in dictionary:
                            vehicles[i].moveCar(d, grid)
                            moves += 1
                            addDictionary(check, dictionary)
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
                        check = makeString(vehicles)
                        if check not in dictionary:
                            moves += 1
                            addDictionary(check, dictionary)
                            # anim.update(vehicles)
                # move horizontal truck into a random direction
                else:
                    d = h_direction[direction]
                    if vehicles[i].checkMove(d, grid):
                        vehicles[i].moveTruck(d, grid)
                        check = makeString(vehicles)
                        if check not in dictionary:
                            moves += 1
                            addDictionary(check, dictionary)
                            # anim.update(vehicles)

    # anim.done()


def makeString(vehicles):
    string = ""

    for i in range(0, len(vehicles)):
        if isinstance(vehicles[i], car.Car):
            x1 = str(vehicles[i].pos.x1)
            x2 = str(vehicles[i].pos.x2)
            y1 = str(vehicles[i].pos.y1)
            y2 = str(vehicles[i].pos.y2)

            string = string + x1 + x2 + y1 + y2

        elif isinstance(vehicles[i], truck.Truck):
            x1 = str(vehicles[i].pos.x1)
            x2 = str(vehicles[i].pos.x2)
            x3 = str(vehicles[i].pos.x3)
            y1 = str(vehicles[i].pos.y1)
            y2 = str(vehicles[i].pos.y2)
            y3 = str(vehicles[i].pos.y3)

            string = string + x1 + x2 + x3 + y1 + y2 + y3

    return string


def addDictionary(string, dictionary):
    dict2 = {string: True}
    dictionary.update(dict2)
