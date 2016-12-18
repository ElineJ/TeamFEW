import visualize as vis
import car
import truck
from copy import deepcopy
import time
start_time = time.time()


def runbfs(grid, exit):

    # set up visualization
    # if exit.x == 5:
    #     width = 6
    # elif exit.x == 9:
    #     width = 9
    # else:
    #     width = 12

    # open window with visualization
    # anim = vis.Visualization(width, width, grid.vehicles)

    # make a list of all states that have happened
    dictionary = {}
    # parents = {}
    # start = makeString(grid)
    # counter = 0
    # make a queue of next steps
    queue = []
    queue = [grid]

    begin = makeString(grid)

    while queue:
        # delete this grid set up from queue and save in node
        node = queue.pop(0)
        check = makeString(node)
        # parents[node] = start
        if check not in dictionary:
            # add this node to the visited set-ups
            # parents[node] = check
            addDictionary(check, dictionary, begin)

        for i in range(0, len(node.vehicles)):
            # if isinstance(node.vehicles[i], car.Car):
            # try moving them in both directions
            # grid has to be updated
            if node.vehicles[i].orientation == "V":
                # use deepcopy to make a copy of nodes and the objects in node
                new_node = deepcopy(node)

                if new_node.vehicles[i].move("up", new_node) != False:
                    # add new set-up to queue
                    string = makeString(new_node)
                    # only add new set up if not already in dictionary
                    if string not in dictionary:
                        addDictionary(string, dictionary, check)
                        queue.append(new_node)
                        # anim.update(new_node.vehicles)

                new_node2 = deepcopy(node)
                if new_node2.vehicles[i].move("down", new_node2) != False:
                    # add new set-up to queue
                    string = makeString(new_node2)
                    if string not in dictionary:
                        addDictionary(string, dictionary, check)
                        queue.append(new_node2)
                        # anim.update(new_node2.vehicles)

            elif node.vehicles[i].orientation == "H":
                new_node = deepcopy(node)
                if new_node.vehicles[i].move("left", new_node) != False:
                    # anim.update(new_node.vehicles)

                    string = makeString(new_node)
                    if string not in dictionary:
                        addDictionary(string, dictionary, check)
                        queue.append(new_node)
                        # anim.update(new_node.vehicles)

                new_node2 = deepcopy(node)
                if new_node2.vehicles[i].move("right", new_node2) != False:
                    # check if the car is at the exit
                    if new_node2.vehicles[i].pos.x2 == exit.x and new_node2.vehicles[i].pos.y2 == exit.y:
                        print "found exit"
                        print("--- %s seconds ---" % (time.time() - start_time))
                        amountSteps(dictionary, check, begin)
                        return new_node2
                        # anim.update(new_node2.vehicles)

                    # add new set-up to queue
                    else:
                        string = makeString(new_node2)
                        if string not in dictionary:
                            addDictionary(string, dictionary, check)
                            queue.append(new_node2)
                            # anim.update(new_node2.vehicles)

    return dictionary
    # anim.done()


def makeString(node):
    string = ""

    for i in range(0, len(node.vehicles)):
        if isinstance(node.vehicles[i], car.Car):
            x1 = str(node.vehicles[i].pos.x1)
            x2 = str(node.vehicles[i].pos.x2)
            y1 = str(node.vehicles[i].pos.y1)
            y2 = str(node.vehicles[i].pos.y2)

            string = string + x1 + x2 + y1 + y2

        elif isinstance(node.vehicles[i], truck.Truck):
            x1 = str(node.vehicles[i].pos.x1)
            x2 = str(node.vehicles[i].pos.x2)
            x3 = str(node.vehicles[i].pos.x3)
            y1 = str(node.vehicles[i].pos.y1)
            y2 = str(node.vehicles[i].pos.y2)
            y3 = str(node.vehicles[i].pos.y3)

            string = string + x1 + x2 + x3 + y1 + y2 + y3

    return string


def addDictionary(string, dictionary, check):
    dict2 = {string: check}
    dictionary.update(dict2)


def amountSteps(dictionary, parent, begin):
    counter = 0
    while parent:
        for key, value in dictionary.iteritems():
            node = key
            if parent == node:
                counter += 1
                if parent == begin:
                    print "Counter = " + str(counter)
                    return counter
                parent = value
