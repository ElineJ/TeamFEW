from grid import *
from car import *
from truck import *

def runbfs(grid, exit):
    # make a list of all states that have happened
    dict = {}

    dictionary = []

    queue = []
    # make a queue of next steps
    queue = [grid]

    while queue:
        # delete this grid set up from queue and save in node
        node = queue.pop(0)

        check = makestring(node, dictionary)

        #if check not in dict:
        if check not in dictionary:
            # add this node to the visited set-ups
            # dict.append(node)

            print str(dict) + "dict"
            print str(check) + "check"


            for i in range(0, len(node.all_vehicles)):
                if isinstance(node.all_vehicles[i], Car):
                # try moving them in both directions
                # grid has to be updated

                    if node.all_vehicles[i].orientation == "V":
                        print "Vertical car"
                        new_node = node
                        # TODO: dit werkt helemaal niet!!!!
                        if node.all_vehicles[i].moveCar(node.all_vehicles[i].getCarPosition, "up", new_node) != "dit kan dus niet he":
                            print "bewogen"
                            # node.all_vehicles[i].moveCar(node.all_vehicles[i].getCarPosition, "up", new_node)

                            if CarPosition == exit:
                                print "found exit"
                                return new_node
                            # grid = new set-up
                            # add new set-up to queue
                            else:
                                queue.append(new_node)
                                string = makestring(node, dictionary)
                                dictionary.append(string)
                                print dictionary

                        new_node = node
                        if node.all_vehicles[i].moveCar(node.all_vehicles[i].getCarPosition, "down", new_node) != "dit kan dus niet he":
                            # node.all_vehicles[i].moveCar(node.all_vehicles[i].getCarPosition, "down", new_node)

                            if CarPosition == exit:
                                print "found exit"
                                return new_node
                            # grid = new set-up
                            # add new set-up to queue
                            else:
                                queue.append(new_node)
                                string = makestring(node, dictionary)
                                dictionary.append(string)

                    if node.all_vehicles[i].orientation == "H":
                        print "Horizontal car"
                        new_node = node
                        if node.all_vehicles[i].moveCar(node.all_vehicles[i].getCarPosition, "left", new_node) != "dit kan dus niet he":
                            #node.all_vehicles[i].moveCar(node.all_vehicles[i].getCarPosition, "left", new_node)

                            if CarPosition == exit:
                                print "found exit"
                                return new_node
                            # grid = new set-up
                            # add new set-up to queue
                            else:
                                queue.append(new_node)
                                string = makestring(node, dictionary)
                                dictionary.append(string)

                        new_node = node
                        if node.all_vehicles[i].moveCar(node.all_vehicles[i].getCarPosition, "right", new_node) != "dit kan dus niet he":
                            #node.all_vehicles[i].moveCar(node.all_vehicles[i].getCarPosition, "right", new_node)

                            if CarPosition == exit:
                                print "found exit"
                                return new_node

                            # grid = new set-up
                            # add new set-up to queue
                            else:
                                queue.append(new_node)
                                string = makestring(node, dictionary)
                                dictionary.append(string)

                elif isinstance(node.all_vehicles[i], Truck):
                    if node.all_vehicles[i].orientation == "V":
                        print "Vertical truck"
                        new_node = node
                        if node.all_vehicles[i].moveTruck(node.all_vehicles[i].getTruckPosition, "up", new_node) != "dit kan dus niet he":
                            #node.all_vehicles[i].moveTruck(node.all_vehicles[i].getTruckPosition, "up", new_node)
                            print "wat"
                            # grid = new set-up
                            # add new set-up to queue
                            queue.append(new_node)
                            string = makestring(node, dictionary)
                            dictionary.append(string)


                        new_node = node
                        if node.all_vehicles[i].moveTruck(node.all_vehicles[i].getTruckPosition, "down", new_node) != "dit kan dus niet he":
                            #node.all_vehicles[i].moveTruck(node.all_vehicles[i].getTruckPosition, "down", new_node)

                            # grid = new set-up
                            # add new set-up to queue
                            queue.append(new_node)
                            string = makestring(node, dictionary)
                            dictionary.append(string)


                    if node.all_vehicles[i].orientation == "H":
                        print "Horizontal Truck"
                        new_node = node
                        if node.all_vehicles[i].moveTruck(node.all_vehicles[i].getTruckPosition, "left", new_node) != "dit kan dus niet he":
                            #node.all_vehicles[i].moveTruck(node.all_vehicles[i].getTruckPosition, "left", new_node)

                            # grid = new set-up
                            # add new set-up to queue
                            queue.append(new_node)
                            string = makestring(node, dictionary)
                            dictionary.append(string)

                        new_node = node
                        if node.all_vehicles[i].moveTruck(node.all_vehicles[i].getTruckPosition, "right", new_node) != "dit kan dus niet he":
                            #node.all_vehicles[i].moveTruck(node.all_vehicles[i].getTruckPosition, "right", new_node)

                            # grid = new set-up
                            # add new set-up to queue
                            queue.append(new_node)
                            string = makestring(node, dictionary)
                            dictionary.append(string)
        #print queue
        #print dict

def makestring(node, dictionary):
    string = ""

    for i in range(0, len(node.all_vehicles)):
        if isinstance(node.all_vehicles[i], Car):
            x1 = str(node.all_vehicles[i].pos.x1)
            x2 = str(node.all_vehicles[i].pos.x2)
            y1 = str(node.all_vehicles[i].pos.y1)
            y2 = str(node.all_vehicles[i].pos.y2)

            string = string + x1 + x2 + y1 + y2

        elif isinstance(node.all_vehicles[i], Truck):
            x1 = str(node.all_vehicles[i].pos.x1)
            x2 = str(node.all_vehicles[i].pos.x2)
            x3 = str(node.all_vehicles[i].pos.x3)
            y1 = str(node.all_vehicles[i].pos.y1)
            y2 = str(node.all_vehicles[i].pos.y2)
            y3 = str(node.all_vehicles[i].pos.y3)

            string = string + x1 + x2 + x3 + y1 + y2 + y3

    print string
    dict.update({string: True})
    return string
