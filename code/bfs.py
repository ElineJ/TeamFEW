import time
#import visualize as vis
import car
import csv
import truck
start_time = time.time()

def runbfs(grid, exit):
    """
    Breadth First Search algorithm that finds the shortest path
    for the red car to get to the exit.
    """
    # make a list of all states that have happened
    dictionary = {}
    # make a queue of next steps
    queue = []
    queue = [grid]
    begin = make_string(grid)

    while queue:
        # delete this grid set up from queue and save in node
        node = queue.pop(0)
        check = make_string(node)
        if check not in dictionary:
            # add this node to the visited set-ups
            add_dictionary(check, dictionary, begin)

        for i in range(0, len(node.vehicles)):
            # move vertical vehicles
            if node.vehicles[i].orientation == "V":
                # use copy function to make a copy of nodes and the objects in node
                new_node = node.copy_grid()
                if new_node.vehicles[i].move("up", new_node):
                    # add new set-up to queue
                    string = make_string(new_node)
                    if string not in dictionary:
                        add_dictionary(string, dictionary, check)
                        queue.append(new_node)
                new_node2 = node.copy_grid()
                if new_node2.vehicles[i].move("down", new_node2):
                    # add new set-up to queue
                    string = make_string(new_node2)
                    if string not in dictionary:
                        add_dictionary(string, dictionary, check)
                        queue.append(new_node2)

            # move horizontal vehicles
            elif node.vehicles[i].orientation == "H":
                new_node = node.copy_grid()
                if new_node.vehicles[i].move("left", new_node):
                    # add set-up to dictionary
                    string = make_string(new_node)
                    if string not in dictionary:
                        add_dictionary(string, dictionary, check)
                        queue.append(new_node)
                new_node2 = node.copy_grid()
                if new_node2.vehicles[i].move("right", new_node2):
                    # check if the car is at the exit
                    if new_node2.car_at_exit(new_node2.vehicles[i].pos):
                        print "--- %s seconds ---" % (time.time() - start_time)
                        return amount_steps(dictionary, check, begin, new_node2)
                    # add new set-up to queue
                    else:
                        string = make_string(new_node2)
                        if string not in dictionary:
                            add_dictionary(string, dictionary, check)
                            queue.append(new_node2)

# @profile
def make_string(node):
    """
    Creates a unique string of the position coordinates
    of all vehicles in the current grid.
    """
    string = ""
    for vehicle in node.vehicles:
        string = string + str(vehicle)
    return string

# @profile
def add_dictionary(string, dictionary, check):
    """
    Adds a unique string of vehicle positions to
    dictionary to track visited set-ups
    """
    dict2 = {string: check}
    dictionary.update(dict2)


def amount_steps(dictionary, parent, begin, grid):
    """
    Counts the steps it has taken for the red car
    to get to the exit.
    """
    counter = 0
    steps = []
    while parent:
        for key, value in dictionary.iteritems():
            node = key
            if parent == node:
                counter += 1
                steps.insert(0, node)
                if parent == begin:
                    print "Counter = " + str(counter)
                    # print steps
                    # visualobject(steps, grid)
                    return counter
                parent = value

def visualobject(steps, grid):
    """
    Translates the array of coordinates into grid objects
    for the visualization and writes array to a file.
    """
    # open window with visualization
    #anim = vis.Visualization(grid.width, grid.width, grid.vehicles)

    with open('../results/gameresult3.csv', 'a') as testFile:
        testFileWriter = csv.writer(testFile)
        testFileWriter.writerow(steps)

    # go through all set ups in list
    # for i in range(0, len(steps)):
    #     counter = 0
    #
    #     # change coordinates for cars and trucks in grid
    #     for j in range(0, len(grid.vehicles)):
    #         string = steps[i]
    #         if isinstance(grid.vehicles[j], truck.Truck):
    #             grid.vehicles[j].pos.x1 = string[counter]
    #             grid.vehicles[j].pos.x2 = string[counter + 1]
    #             grid.vehicles[j].pos.x3 = string[counter + 2]
    #             grid.vehicles[j].pos.y1 = string[counter + 3]
    #             grid.vehicles[j].pos.y2 = string[counter + 4]
    #             grid.vehicles[j].pos.y3 = string[counter + 5]
    #             counter += 6
    #         elif isinstance(grid.vehicles[j], car.Car):
    #             grid.vehicles[j].pos.x1 = string[counter]
    #             grid.vehicles[j].pos.x2 = string[counter + 1]
    #             grid.vehicles[j].pos.y1 = string[counter + 2]
    #             grid.vehicles[j].pos.y2 = string[counter + 3]
    #             counter += 4
    #     #anim.update(grid.vehicles)
