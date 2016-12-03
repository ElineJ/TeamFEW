import grid
import car
import truck
from copy import deepcopy

def runbfs(grid, exit):
    # make a list of all states that have happened
    dictionary = {}

    for i in range(0, len(grid.all_vehicles)):
        if isinstance(grid.all_vehicles[i], car.Car):
            print "First position car: ", grid.all_vehicles[i].pos.x1, grid.all_vehicles[i].pos.x2, grid.all_vehicles[i].pos.y1, grid.all_vehicles[i].pos.y2
        if isinstance(grid.all_vehicles[i], truck.Truck):
            print "First position truck: ", grid.all_vehicles[i].pos.x1, grid.all_vehicles[i].pos.x2, grid.all_vehicles[i].pos.x3, grid.all_vehicles[i].pos.y1, grid.all_vehicles[i].pos.y2, grid.all_vehicles[i].pos.y3
    queue = []
    # make a queue of next steps
    queue = [grid]

    while queue:
        # delete this grid set up from queue and save in node
        node = queue.pop(0)
        #print "we zijn hier"

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

                    if new_node.all_vehicles[i].moveCar(new_node.all_vehicles[i].getCarPosition, "up", new_node) != False:
                        # node.all_vehicles[i].moveCar(node.all_vehicles[i].getCarPosition, "up", new_node)

                        #if CarPosition == exit:
                        #    #print "found exit"
                        #    return new_node
                        # grid = new set-up
                        # add new set-up to queue

                        string = makeString(new_node)
                        # only add new set up if not already in dictionary
                        if string not in dictionary:
                            #print "hier iets aan het doen"
                            addDictionary(string, dictionary)
                            queue.append(new_node)

                    new_node2 = deepcopy(node)
                    if new_node2.all_vehicles[i].moveCar(new_node2.all_vehicles[i].getCarPosition, "down", new_node2) != False:
                        # node.all_vehicles[i].moveCar(node.all_vehicles[i].getCarPosition, "down", new_node)

                        # grid = new set-up
                        # add new set-up to queue

                        string = makeString(new_node2)
                        if string not in dictionary:
                            #print "hier iets aan het doen"
                            addDictionary(string, dictionary)
                            queue.append(new_node2)

                if node.all_vehicles[i].orientation == "H":
                    new_node = deepcopy(node)
                    if new_node.all_vehicles[i].moveCar(new_node.all_vehicles[i].getCarPosition, "left", new_node) != False:
                        #node.all_vehicles[i].moveCar(node.all_vehicles[i].getCarPosition, "left", new_node)

                        # if horizontal car on exit this means the exit is found
                        if new_node.all_vehicles[i].x1 == 5:
                            if new_node.all_vehicles[i].y2 == 2:
                                print "found exit"
                                return new_node
                        # grid = new set-up
                        # add new set-up to queue
                        else:
                            string = makeString(new_node)
                            if string not in dictionary:
                                #print "hier iets aan het doen"
                                addDictionary(string, dictionary)
                                queue.append(new_node)

                    new_node2 = deepcopy(node)
                    if new_node2.all_vehicles[i].moveCar(new_node2.all_vehicles[i].getCarPosition, "right", new_node2) != False:
                        #node.all_vehicles[i].moveCar(node.all_vehicles[i].getCarPosition, "right", new_node)

                        if new_node2.all_vehicles[i].x2 == 5:
                            if new_node2.all_vehicles[i].y2 == 2:
                                print "found exit"
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
                    # print "Vertical truck"
                    new_node = deepcopy(node)
                    if new_node.all_vehicles[i].moveTruck(new_node.all_vehicles[i].getTruckPosition, "up", new_node) != False:
                        #node.all_vehicles[i].moveTruck(node.all_vehicles[i].getTruckPosition, "up", new_node)
                        # grid = new set-up
                        # add new set-up to queue
                        string = makeString(new_node)
                        if string not in dictionary:
                            #print "hier iets aan het doen"
                            addDictionary(string, dictionary)
                            queue.append(new_node)

                    new_node2 = deepcopy(node)
                    if new_node2.all_vehicles[i].moveTruck(new_node2.all_vehicles[i].getTruckPosition, "down", new_node2) != False:
                        #node.all_vehicles[i].moveTruck(node.all_vehicles[i].getTruckPosition, "down", new_node)
                        # grid = new set-up
                        # add new set-up to queue
                        string = makeString(new_node2)
                        if string not in dictionary:
                            #print "hier iets aan het doen"
                            addDictionary(string, dictionary)
                            queue.append(new_node2)

                if node.all_vehicles[i].orientation == "H":
                    # print "Horizontal Truck"
                    new_node = deepcopy(node)
                    if new_node.all_vehicles[i].moveTruck(new_node.all_vehicles[i].getTruckPosition, "left", new_node) != False:
                        #node.all_vehicles[i].moveTruck(node.all_vehicles[i].getTruckPosition, "left", new_node)

                        # grid = new set-up
                        # add new set-up to queue
                        string = makeString(new_node)
                        if string not in dictionary:
                            #print "hier iets aan het doen"
                            addDictionary(string, dictionary)
                            queue.append(new_node)

                    new_node2 = deepcopy(node)
                    if new_node2.all_vehicles[i].moveTruck(new_node2.all_vehicles[i].getTruckPosition, "right", new_node2) != False:
                        #node.all_vehicles[i].moveTruck(node.all_vehicles[i].getTruckPosition, "right", new_node)

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
        ##print queue
        return dictionary

    for i in range(0, len(grid.all_vehicles)):
        print "Last position: ", grid.all_vehicles[i].pos.x1, grid.all_vehicles[i].pos.x2, grid.all_vehicles[i].pos.x1, grid.all_vehicles[i].pos.y2


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
    #string = string

    #dictionary = dictionary
    dict2 = {string: 'True'}
    dictionary.update(dict2)
