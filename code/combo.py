import visualize as vis
import grid
import car
import truck
import random
import time


def runrandom(grid, exit, num_runs):

        start_time = time.time()
        v_direction = ["up", "down"]
        h_direction = ["left", "right"]
        vehicles = grid.all_vehicles
        grid_bfs = deepcopy(grid)
        moves = 0
        results = []

        # make a list of all states that have happened
        random_dictionary = {}
        # set up visualization
        # if exit.x == 5:
        #     width = 6
        # elif exit.x == 9:
        #     width = 9
        # else:
        #     width = 12
        string = makeString(vehicles)
        add_random_dictionary(string, random_dictionary)
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
                            if check not in random_dictionary:
                                moves += 1
                                add_random_dictionary(check, random_dictionary)
                                # anim.update(vehicles)
                    # move horizontal car into a random direction
                    else:
                        d = h_direction[direction]
                        if vehicles[i].checkMove(d, grid):
                            vehicles[i].moveCar(d, grid)
                            check = makeString(vehicles)
                            if check not in random_dictionary:
                                vehicles[i].moveCar(d, grid)
                                moves += 1
                                add_random_dictionary(check, random_dictionary)
                                # anim.update(vehicles)
                                # check if car is at exit
                                if vehicles[i].pos.x2 == exit.x and vehicles[i].pos.y2 == exit.y:
                                    # del results[:]
                                    print "Found exit!"
                                    print "Moves:", moves
                                    print("--- %s seconds ---" % (time.time() - start_time))
                                    runbfs(grid_bfs, exit, random_dictionary)
                                    results.append(moves)
                                    results.append("%.6s" % (time.time() - start_time))
                                    # print moves,("%s seconds" % (time.time() - start_time))
                                    runbfs(grid_bfs, exit, random_dictionary)
                                    return False

                elif isinstance(vehicles[i], truck.Truck):
                    direction = random.randint(0, 1)
                    # move vertical truck in a random direction
                    if vehicles[i].orientation == 'V':
                        d = v_direction[direction]
                        if vehicles[i].checkMove(d, grid):
                            vehicles[i].moveTruck(d, grid)
                            check = makeString(vehicles)
                            if check not in random_dictionary:
                                moves += 1
                                add_random_dictionary(check, random_dictionary)
                                # anim.update(vehicles)
                    # move horizontal truck into a random direction
                    else:
                        d = h_direction[direction]
                        if vehicles[i].checkMove(d, grid):
                            vehicles[i].moveTruck(d, grid)
                            check = makeString(vehicles)
                            if check not in random_dictionary:
                                moves += 1
                                add_random_dictionary(check, random_dictionary)
                                # anim.update(vehicles)


def runbfs(grid, exit, random_dictionary):

    # set up visualization
    # if exit.x == 5:
    #     width = 6
    # elif exit.x == 9:
    #     width = 9
    # else:
    #     width = 12

    # open window with visualization
    # anim = vis.Visualization(width, width, grid.all_vehicles)

    # make a list of all states that have happened
    dictionary = {}
    # parents = {}
    # start = makeString(grid)

    # counter = 0
    # make a queue of next steps
    queue = []
    queue = [grid]

    begin = makeString(grid.all_vehicles)

    while queue:
        # print "Queue at start: ", len(queue)

        # delete this grid set up from queue and save in node
        node = queue.pop(0)
        check = makeString(node.all_vehicles)
        # parents[node] = start
        if check not in dictionary:
            # add this node to the visited set-ups
            # parents[node] = check
            addDictionary(check, dictionary, begin)
        if check in random_dictionary:
            for i in range(0, len(node.all_vehicles)):
                if isinstance(node.all_vehicles[i], car.Car):
                    # try moving them in both directions
                    # grid has to be updated
                    if node.all_vehicles[i].orientation == "V":
                        # use deepcopy to make a copy of nodes and the objects in node
                        new_node = deepcopy(node)

                        if new_node.all_vehicles[i].moveCar("up", new_node) != False:
                            # print "Car moved up"

                            # grid = new set-up
                            # add new set-up to queue
                            string = makeString(new_node.all_vehicles)
                            # only add new set up if not already in dictionary
                            if string not in dictionary:
                                addDictionary(string, dictionary, check)
                                queue.append(new_node)
                                # anim.update(new_node.all_vehicles)

                        new_node2 = deepcopy(node)
                        if new_node2.all_vehicles[i].moveCar("down", new_node2) != False:
                            # print "Car moved down"
                            # grid = new set-up
                            # add new set-up to queue

                            string = makeString(new_node2.all_vehicles)
                            if string not in dictionary:
                                addDictionary(string, dictionary, check)
                                queue.append(new_node2)
                                # anim.update(new_node2.all_vehicles)

                    elif node.all_vehicles[i].orientation == "H":
                        new_node = deepcopy(node)
                        if new_node.all_vehicles[i].moveCar("left", new_node) != False:
                            # print "Car moved left"
                            # anim.update(new_node.all_vehicles)

                            string = makeString(new_node.all_vehicles)
                            if string not in dictionary:
                                addDictionary(string, dictionary, check)
                                queue.append(new_node)
                                # anim.update(new_node.all_vehicles)

                        new_node2 = deepcopy(node)
                        if new_node2.all_vehicles[i].moveCar("right", new_node2) != False:
                            # print "Car moved right"

                            # check if the car is at the exit
                            if new_node2.all_vehicles[i].pos.x2 == exit.x and new_node2.all_vehicles[i].pos.y2 == exit.y:
                                print "found exit"
                                print("--- %s seconds ---" % (time.time() - start_time))
                                amountSteps(dictionary, check, begin)
                                # print counter
                                return new_node2
                                # anim.update(new_node2.all_vehicles)
                                # solution = [exit]
                                # n = exit
                                # while n in parents and parents[n]:
                                #     solution.append(parents[n])
                                #     n = parents[n]
                                #
                                # return solution[::-1]

                            # grid = new set-up
                            # add new set-up to queue
                            else:
                                string = makeString(new_node2.all_vehicles)
                                if string not in dictionary:
                                    addDictionary(string, dictionary, check)
                                    queue.append(new_node2)
                                    # anim.update(new_node2.all_vehicles)

                elif isinstance(node.all_vehicles[i], truck.Truck):
                    if node.all_vehicles[i].orientation == "V":

                        new_node = deepcopy(node)
                        if new_node.all_vehicles[i].moveTruck("up", new_node) != False:
                            # print "truck moved up"
                            # anim.update(new_node.all_vehicles)
                            # grid = new set-up
                            # add new set-up to queue
                            string = makeString(new_node.all_vehicles)
                            if string not in dictionary:
                                addDictionary(string, dictionary, check)
                                queue.append(new_node)
                                # anim.update(new_node.all_vehicles)

                        new_node2 = deepcopy(node)
                        if new_node2.all_vehicles[i].moveTruck("down", new_node2) != False:
                            # print "truck moved down"
                            # anim.update(new_node2.all_vehicles)
                            # add new set-up to queue
                            string = makeString(new_node2.all_vehicles)
                            if string not in dictionary:
                                addDictionary(string, dictionary, check)
                                queue.append(new_node2)
                                # anim.update(new_node2.all_vehicles)

                    elif node.all_vehicles[i].orientation == "H":

                        new_node = deepcopy(node)
                        if new_node.all_vehicles[i].moveTruck("left", new_node) != False:
                            # print "truck moved left"
                            # anim.update(new_node.all_vehicles)
                            # grid = new set-up
                            # add new set-up to queue
                            string = makeString(new_node.all_vehicles)
                            if string not in dictionary:
                                addDictionary(string, dictionary, check)
                                queue.append(new_node)
                                # anim.update(new_node.all_vehicles)

                        new_node2 = deepcopy(node)
                        if new_node2.all_vehicles[i].moveTruck("right", new_node2) != False:
                            # print "truck moved right"
                            # anim.update(new_node2.all_vehicles)
                            # grid = new set-up
                            # add new set-up to queue
                            string = makeString(new_node2.all_vehicles)
                            if string not in dictionary:
                                addDictionary(string, dictionary, check)
                                queue.append(new_node2)
                                # anim.update(new_node2.all_vehicles)

    return dictionary
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

def addDictionary(string, dictionary, check):
    dict2 = {string: check}
    dictionary.update(dict2)

def amountSteps(dictionary, parent, begin):
    counter = 0
    while parent:
        for key, value in dictionary.iteritems():
            #print str(key) + "key"
            node = key
            if parent == node:
                #print str(begin) + "begin"
                #print parent
                #print node
                counter += 1
                if parent == begin:
                    print "Counter = " + str(counter)
                    return counter
                parent = value

def add_random_dictionary(string, random_dictionary):
    dict2 = {string: True}
    random_dictionary.update(dict2)
