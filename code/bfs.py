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
    global dictionary
    global queue
    global begin
    global parent
    dictionary = {}
    queue = []
    queue = [grid]
    begin = make_string(grid)

    while queue:
        # check initial board
        node = queue.pop(0)
        parent = make_string(node)
        if parent not in dictionary:
            add_dictionary(parent, begin)
            queue.append(node)

        # move all vehicles from current position
        for i in range(0, len(node.vehicles)):
            if node.vehicles[i].orientation == "V":
                # move vertical vehicles
                nodecopy = node.vehicles[i].move_up(node)
                if nodecopy is not False:
                    check_dictionary(nodecopy)
                nodecopy = node.vehicles[i].move_down(node)
                if nodecopy is not False:
                    check_dictionary(nodecopy)

            elif node.vehicles[i].orientation == "H":
                # move horizontal vehicles
                nodecopy = node.vehicles[i].move_left(node)
                if nodecopy is not False:
                    check_dictionary(nodecopy)
                nodecopy = node.vehicles[i].move_right(node)
                if nodecopy is not False:
                    if nodecopy.car_at_exit(nodecopy.vehicles[i].pos):
                        print "--- %s seconds ---" % (time.time() - start_time)
                        return amount_steps(parent, nodecopy)
                    check_dictionary(nodecopy)


def check_dictionary(node):
    """

    """
    string = make_string(node)
    if string not in dictionary:
        add_dictionary(string, parent)
        queue.append(node)


def make_string(node):
    """
    Creates a unique string of the position coordinates
    of all vehicles in the current grid.
    """
    return ''.join([str(vehicle) for vehicle in node.vehicles])


def add_dictionary(string, parent):
    """
    Adds a unique string of vehicle positions to
    dictionary to track visited set-ups
    """
    dict2 = {string: parent}
    dictionary.update(dict2)


def amount_steps(parent, grid):
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
                    print "Steps = " + str(counter)
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

    with open('../results/gameresult5.csv', 'a') as testFile:
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
