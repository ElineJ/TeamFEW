import visualize as vis
import car
import truck
from copy import deepcopy
import time
start_time = time.time()


def runbfs(grid, exit):

    # make a list of all states that have happened
    dictionary = {}

    # make a queue of next steps
    queue = []
    queue = [grid]
    begin = makeString(grid)

    while queue:
        # delete this grid set up from queue and save in node
        node = queue.pop(0)
        check = makeString(node)
        if check not in dictionary:
            # add this node to the visited set-ups
            addDictionary(check, dictionary, begin)

        for i in range(0, len(node.vehicles)):

            # move vertical vehicles
            if node.vehicles[i].orientation == "V":
                # use deepcopy to make a copy of nodes and the objects in node
                new_node = deepcopy(node)

                if new_node.vehicles[i].move("up", new_node) != False:
                    # add new set-up to queue
                    string = makeString(new_node)
                    if string not in dictionary:
                        addDictionary(string, dictionary, check)
                        queue.append(new_node)

                new_node2 = deepcopy(node)
                if new_node2.vehicles[i].move("down", new_node2) != False:
                    # add new set-up to queue
                    string = makeString(new_node2)
                    if string not in dictionary:
                        addDictionary(string, dictionary, check)
                        queue.append(new_node2)

            # move horizontal vehicles
            elif node.vehicles[i].orientation == "H":
                new_node = deepcopy(node)
                if new_node.vehicles[i].move("left", new_node) != False:
                    # add set-up to dictionary
                    string = makeString(new_node)
                    if string not in dictionary:
                        addDictionary(string, dictionary, check)
                        queue.append(new_node)

                new_node2 = deepcopy(node)
                if new_node2.vehicles[i].move("right", new_node2) != False:
                    # check if the car is at the exit
                    if new_node2.vehicles[i].pos.x2 == exit.x and new_node2.vehicles[i].pos.y2 == exit.y:
                        print("--- %s seconds ---" % (time.time() - start_time))
                        return amountSteps(dictionary, check, begin)

                    # add new set-up to queue
                    else:
                        string = makeString(new_node2)
                        if string not in dictionary:
                            addDictionary(string, dictionary, check)
                            queue.append(new_node2)


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
