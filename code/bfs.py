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

    while queue:
        print "Queue at start: " ,len(queue)

        # delete this grid set up from queue and save in node
        node = queue.pop(0)
        check = makeString(node)

        if check not in dictionary:
            # add this node to the visited set-ups
            # dict.append(node)
            addDictionary(check, dictionary)

        for i in range(0, len(node.all_vehicles)):
            if isinstance(node.all_vehicles[i], car.Car):
                # try moving them in both directions
                # grid has to be updated
                if node.all_vehicles[i].orientation == "V":
                    # use deepcopy to make a copy of nodes and the objects in node
                    new_node = deepcopy(node)

                    # moved = new_node.all_vehicles[i].moveCar(new_node.all_vehicles[i].getCarPosition, "up", new_node)
                    if new_node.all_vehicles[i].moveCar(new_node.all_vehicles[i].getCarPosition, "up", new_node) != False:
                        # print "Car moved up"
                        # grid = new set-up
                        # add new set-up to queue
                        string = makeString(new_node)
                        # only add new set up if not already in dictionary
                        if string not in dictionary:
                            #print "hier iets aan het doen"
                            addDictionary(string, dictionary)
                            queue.append(new_node)
                            print "Queue: ", len(queue)

                    new_node2 = deepcopy(node)
                    if new_node2.all_vehicles[i].moveCar(new_node2.all_vehicles[i].getCarPosition, "down", new_node2) != False:
                        # print "Car moved down"
                        # grid = new set-up
                        # add new set-up to queue

                        string = makeString(new_node2)
                        if string not in dictionary:
                            #print "hier iets aan het doen"
                            addDictionary(string, dictionary)
                            queue.append(new_node2)

                elif node.all_vehicles[i].orientation == "H":
                    new_node = deepcopy(node)
                    if new_node.all_vehicles[i].moveCar(new_node.all_vehicles[i].getCarPosition, "left", new_node) != False:
                        # print "Car moved left"
                        string = makeString(new_node)
                        if string not in dictionary:
                            #print "hier iets aan het doen"
                            addDictionary(string, dictionary)
                            queue.append(new_node)

                    new_node2 = deepcopy(node)
                    if new_node2.all_vehicles[i].moveCar(new_node2.all_vehicles[i].getCarPosition, "right", new_node2) != False:
                        # print "Car moved right"
                        # check if the car is at the exit
                        if new_node2.all_vehicles[i].pos.x2 == 5 and new_node2.all_vehicles[i].pos.y2 == 2:
                            print "found exit"
                            print("--- %s seconds ---" % (time.time() - start_time))
                            return new_node2

                        # grid = new set-up
                        # add new set-up to queue
                        else:
                            string = makeString(new_node2)
                            if string not in dictionary:
                                #print "hier iets aan het doen"
                                addDictionary(string, dictionary)
                                queue.append(new_node2)

            elif isinstance(node.all_vehicles[i], truck.Truck):
                if node.all_vehicles[i].orientation == "V":

                    new_node = deepcopy(node)
                    if new_node.all_vehicles[i].moveTruck(new_node.all_vehicles[i].getTruckPosition, "up", new_node) != False:
                        # print "truck moved up"
                        # grid = new set-up
                        # add new set-up to queue
                        string = makeString(new_node)
                        if string not in dictionary:
                            #print "hier iets aan het doen"
                            addDictionary(string, dictionary)
                            queue.append(new_node)

                    new_node2 = deepcopy(node)
                    if new_node2.all_vehicles[i].moveTruck(new_node2.all_vehicles[i].getTruckPosition, "down", new_node2) != False:
                        # print "truck moved down"
                        # add new set-up to queue
                        string = makeString(new_node2)
                        if string not in dictionary:
                            #print "hier iets aan het doen"
                            addDictionary(string, dictionary)
                            queue.append(new_node2)
                            print "Queue: ", len(queue)

                elif node.all_vehicles[i].orientation == "H":

                    new_node = deepcopy(node)
                    if new_node.all_vehicles[i].moveTruck(new_node.all_vehicles[i].getTruckPosition, "left", new_node) != False:
                        # print "truck moved left"

                        # grid = new set-up
                        # add new set-up to queue
                        string = makeString(new_node)
                        if string not in dictionary:
                            #print "hier iets aan het doen"
                            addDictionary(string, dictionary)
                            queue.append(new_node)

                    new_node2 = deepcopy(node)
                    if new_node2.all_vehicles[i].moveTruck(new_node2.all_vehicles[i].getTruckPosition, "right", new_node2) != False:
                        # print "truck moved right"

                        # grid = new set-up
                        # add new set-up to queue
                        string = makeString(new_node2)
                        if string not in dictionary:
                            #print "hier iets aan het doen"
                            addDictionary(string, dictionary)
                            queue.append(new_node2)
            #for i in range(0, len(queue)):
                # print str(queue[i]) + str(i)
                #print "wtf"
        #for k, v in dictionary.iteritems():
        #    print k, v
        print "Queue at end: " ,len(queue)
    return dictionary


    #for i in range(0, len(grid.all_vehicles)):
    #    print "Last position: ", grid.all_vehicles[i].pos.x1, grid.all_vehicles[i].pos.x2, grid.all_vehicles[i].pos.x1, grid.all_vehicles[i].pos.y2

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
    #print string
    return string

def addDictionary(string, dictionary):
    #dictionary = dictionary
    dict2 = {string: 'True'}
    dictionary.update(dict2)
