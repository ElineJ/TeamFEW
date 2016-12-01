from grid import *
from car import *
from truck import *

def runbfs(grid, exit):
    # make a list of all states that have happened
    dict = {}

    queue = []
    # make a queue of next steps
    queue = [grid]

    while queue:
        # delete this grid set up from queue and save in node
        node = queue.pop(0)

        if node not in dict:
            # add this node to the visited set-ups
            # dict.append(node)

            for i in range(0, len(node.all_vehicles)):
                if isinstance(node.all_vehicles[i], Car):
                # try moving them in both directions
                # grid has to be updated

                    if node.all_vehicles[i].orientation == "V":
                        print "Vertical car"
                        new_node = node
                        if node.all_vehicles[i].moveCar(node.all_vehicles[i].getCarPosition, "up", new_node) == True:
                            node.all_vehicles[i].moveCar(node.all_vehicles[i].getCarPosition, "up", new_node)

                            if CarPosition == exit:
                                return new_node
                            # grid = new set-up
                            # add new set-up to queue
                            else:
                                queue.append(new_node)
                        new_node = node
                        if node.all_vehicles[i].moveCar(node.all_vehicles[i].getCarPosition, "down", new_node) == True:
                            node.all_vehicles[i].moveCar(node.all_vehicles[i].getCarPosition, "down", new_node)

                            if CarPosition == exit:
                                return new_node
                            # grid = new set-up
                            # add new set-up to queue
                            else:
                                queue.append(node)

                    if node.all_vehicles[i].orientation == "H":
                        print "Horizontal car"
                        new_node = node
                        if node.all_vehicles[i].moveCar(node.all_vehicles[i].getCarPosition, "left", new_node) == True:
                            node.all_vehicles[i].moveCar(node.all_vehicles[i].getCarPosition, "left", new_node)

                            if CarPosition == exit:
                                return new_node
                            # grid = new set-up
                            # add new set-up to queue
                            else:
                                queue.append(new_node)

                        new_node = node
                        if node.all_vehicles[i].moveCar(node.all_vehicles[i].getCarPosition, "right", new_node) == True:
                            node.all_vehicles[i].moveCar(node.all_vehicles[i].getCarPosition, "right", new_node)

                            if CarPosition == exit:
                                return new_node
                            # grid = new set-up
                            # add new set-up to queue
                            else:
                                queue.append(new_node)

                elif isinstance(node.all_vehicles[i], Truck):
                    if node.all_vehicles[i].orientation == "V":
                        print "Vertical truck"
                        new_node = node
                        if node.all_vehicles[i].moveTruck(node.all_vehicles[i].getTruckPosition, "up", new_node) == True:
                            node.all_vehicles[i].moveTruck(node.all_vehicles[i].getTruckPosition, "up", new_node)

                            # grid = new set-up
                            # add new set-up to queue
                            queue.append(new_node)

                        new_node = node
                        if node.all_vehicles[i].moveTruck(node.all_vehicles[i].getTruckPosition, "down", new_node) == True:
                            node.all_vehicles[i].moveTruck(node.all_vehicles[i].getTruckPosition, "down", new_node)

                            # grid = new set-up
                            # add new set-up to queue
                            queue.append(new_node)

                    if node.all_vehicles[i].orientation == "H":
                        print "Horizontal Truck"
                        new_node = node
                        if node.all_vehicles[i].moveTruck(node.all_vehicles[i].getTruckPosition, "left", new_node) == True:
                            node.all_vehicles[i].moveTruck(node.all_vehicles[i].getTruckPosition, "left", new_node)

                            # grid = new set-up
                            # add new set-up to queue
                            queue.append(new_node)

                        new_node = node
                        if node.all_vehicles[i].moveTruck(node.all_vehicles[i].getTruckPosition, "right", new_node) == True:
                            node.all_vehicles[i].moveTruck(node.all_vehicles[i].getTruckPosition, "right", new_node)

                            # grid = new set-up
                            # add new set-up to queue
                            queue.append(new_node)
        print queue
        print dict
