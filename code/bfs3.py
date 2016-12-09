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
    # anim = vis.Visualization(width, width, grid.all_vehicles)
    # make a list of all states that have happened
    dictionary = {}
    # make a queue of next steps
    queue = []
    queue = [grid]

    while queue:
        # print "Queue at start: ", len(queue)

        # delete this grid set up from queue and save in node
        node = queue.pop(0)
        check = makeString(node)

        if check not in dictionary:
            # add this node to the visited set-ups

            addDictionary(check, dictionary)

        GenerateMove(node, dictionary, queue, exit)

    # anim.done()

def makeString(node):
    string = ""

    for i in range(0, len(node.all_vehicles)):
        if isinstance(node.all_vehicles[i], car.Car):
            x1 = str(node.all_vehicles[i].pos.x1)
            x2 = str(node.all_vehicles[i].pos.x2)
            y1 = str(node.all_vehicles[i].pos.y1)
            y2 = str(node.all_vehicles[i].pos.y2)

            string = string + x1 + x2 + y1 + y2

        elif isinstance(node.all_vehicles[i], truck.Truck):
            x1 = str(node.all_vehicles[i].pos.x1)
            x2 = str(node.all_vehicles[i].pos.x2)
            x3 = str(node.all_vehicles[i].pos.x3)
            y1 = str(node.all_vehicles[i].pos.y1)
            y2 = str(node.all_vehicles[i].pos.y2)
            y3 = str(node.all_vehicles[i].pos.y3)

            string = string + x1 + x2 + x3 + y1 + y2 + y3

    return string

def addDictionary(string, dictionary):
    dict2 = {string: 'True'}
    dictionary.update(dict2)

def GenerateMove(node, dictionary, queue, exit):
                for i in range(0, len(node.all_vehicles)):
                    if isinstance(node.all_vehicles[i], car.Car):
                        # try moving them in both directions
                        # grid has to be updated
                        if node.all_vehicles[i].orientation == "V":
                            # use deepcopy to make a copy of nodes and the objects in node
                            new_node = deepcopy(node)

                            if new_node.all_vehicles[i].moveCar(new_node.all_vehicles[i].getCarPosition, "up", new_node) != False:
                                # print "Car moved up"

                                # grid = new set-up
                                # add new set-up to queue
                                string = makeString(new_node)
                                # only add new set up if not already in dictionary
                                if string not in dictionary:
                                    addDictionary(string, dictionary)
                                    queue.append(new_node)
                                    # anim.update(new_node.all_vehicles)

                            new_node2 = deepcopy(node)
                            if new_node2.all_vehicles[i].moveCar(new_node2.all_vehicles[i].getCarPosition, "down", new_node2) != False:
                                # print "Car moved down"
                                # grid = new set-up
                                # add new set-up to queue

                                string = makeString(new_node2)
                                if string not in dictionary:
                                    addDictionary(string, dictionary)
                                    queue.append(new_node2)
                                    # anim.update(new_node2.all_vehicles)

                        elif node.all_vehicles[i].orientation == "H":
                            new_node = deepcopy(node)
                            if new_node.all_vehicles[i].moveCar(new_node.all_vehicles[i].getCarPosition, "left", new_node) != False:
                                # print "Car moved left"
                                # anim.update(new_node.all_vehicles)

                                string = makeString(new_node)
                                if string not in dictionary:
                                    addDictionary(string, dictionary)
                                    queue.append(new_node)
                                    # anim.update(new_node.all_vehicles)

                            new_node2 = deepcopy(node)
                            if new_node2.all_vehicles[i].moveCar(new_node2.all_vehicles[i].getCarPosition, "right", new_node2) != False:
                                # print "Car moved right"

                                # check if the car is at the exit
                                if new_node2.all_vehicles[i].pos.x2 == exit.x and new_node2.all_vehicles[i].pos.y2 == exit.y:
                                    print "found exit"
                                    print("--- %s seconds ---" % (time.time() - start_time))
                                    queue = []
                                    return queue

                                    # anim.update(new_node2.all_vehicles)



                                # grid = new set-up
                                # add new set-up to queue
                                else:
                                    string = makeString(new_node2)
                                    if string not in dictionary:
                                        addDictionary(string, dictionary)
                                        queue.append(new_node2)
                                        # anim.update(new_node2.all_vehicles)

                    elif isinstance(node.all_vehicles[i], truck.Truck):
                        if node.all_vehicles[i].orientation == "V":

                            new_node = deepcopy(node)
                            if new_node.all_vehicles[i].moveTruck(new_node.all_vehicles[i].getTruckPosition, "up", new_node) != False:
                                # print "truck moved up"
                                # anim.update(new_node.all_vehicles)
                                # grid = new set-up
                                # add new set-up to queue
                                string = makeString(new_node)
                                if string not in dictionary:
                                    addDictionary(string, dictionary)
                                    queue.append(new_node)
                                    # anim.update(new_node.all_vehicles)

                            new_node2 = deepcopy(node)
                            if new_node2.all_vehicles[i].moveTruck(new_node2.all_vehicles[i].getTruckPosition, "down", new_node2) != False:
                                # print "truck moved down"
                                # anim.update(new_node2.all_vehicles)
                                # add new set-up to queue
                                string = makeString(new_node2)
                                if string not in dictionary:
                                    addDictionary(string, dictionary)
                                    queue.append(new_node2)
                                    # anim.update(new_node2.all_vehicles)

                        elif node.all_vehicles[i].orientation == "H":

                            new_node = deepcopy(node)
                            if new_node.all_vehicles[i].moveTruck(new_node.all_vehicles[i].getTruckPosition, "left", new_node) != False:
                                # print "truck moved left"
                                # anim.update(new_node.all_vehicles)
                                # grid = new set-up
                                # add new set-up to queue
                                string = makeString(new_node)
                                if string not in dictionary:
                                    addDictionary(string, dictionary)
                                    queue.append(new_node)
                                    # anim.update(new_node.all_vehicles)

                            new_node2 = deepcopy(node)
                            if new_node2.all_vehicles[i].moveTruck(new_node2.all_vehicles[i].getTruckPosition, "right", new_node2) != False:
                                # print "truck moved right"
                                # anim.update(new_node2.all_vehicles)
                                # grid = new set-up
                                # add new set-up to queue
                                string = makeString(new_node2)
                                if string not in dictionary:
                                    addDictionary(string, dictionary)
                                    queue.append(new_node2)
                                    # anim.update(new_node2.all_vehicles)
