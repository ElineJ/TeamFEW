import visualize as vis
import grid
import car
import truck
import random
import time
start_time = time.time()

def runcombo(grid, exit, num_runs):
    grid_bfs = grid.copy_grid()
    check_dictionary = {}
    start_time = time.time()

    for i in range(0, num_runs):
        v_direction = ["up", "down"]
        h_direction = ["left", "right"]
        new_grid = grid.copy_grid()
        random_dictionary = {}
        vehicles = new_grid.vehicles
        not_at_exit = True
        moves = 0
        # make a list of all states that have happened
        # set up visualization
        # if exit.x == 5:
        #     width = 6
        # elif exit.x == 9:
        #     width = 9
        # else:
        #     width = 12
        string = make_string(vehicles)
        print string
        if string not in random_dictionary:
            add_random_dictionary(string, random_dictionary)
        # open window with visualization
        # anim = vis.Visualization(width, width, vehicles)
        while moves < 5000 and not_at_exit:
            for vehicle in vehicles:
                number = random.randint(0, 1)
                # move vertical car in a random direction
                if vehicle.orientation == 'V':
                    direction = v_direction[number]
                    if vehicle.move(direction, new_grid) != False:
                        check = make_string(vehicles)
                        moves += 1
                        if check not in random_dictionary:

                            add_random_dictionary(check, random_dictionary)
                            # anim.update(vehicles)
                # move horizontal car into a random direction
                elif vehicle.orientation == 'H':
                    direction = h_direction[number]
                    if vehicle.move(direction, new_grid) != False:
                        check = make_string(vehicles)
                        moves += 1
                        if check not in random_dictionary:

                            add_random_dictionary(check, random_dictionary)
                            # anim.update(vehicles)
                            # check if car is at exit
                        if grid.car_at_exit(vehicle.pos):
                            # print "Found exit!"
                            print moves
                            if moves < 5000:
                                check_dictionary = dict(check_dictionary.items() + random_dictionary.items())
                                print "ik kom hier in"
                            not_at_exit = False

    runbfs(grid_bfs, exit, check_dictionary)
        # anim.done()


# @profile
def runbfs(grid, exit, check_dictionary):
    """
    Breadth First Search algorithm that finds the shortest path
    for the red car to get to the exit.
    """
    # make a list of all states that have happened
    print "dit is de lengte van de dict = " + str(len(check_dictionary))
    dictionary = {}
    string = make_string(grid.vehicles)
    print string
    # make a queue of next steps
    queue = []
    queue = [grid]
    vehicles = grid.vehicles
    begin = make_string(vehicles)
    while queue:
        # delete this grid set up from queue and save in node
        node = queue.pop(0)
        check = make_string(node.vehicles)
        if check not in dictionary:
            # add this node to the visited set-ups
            add_dictionary(check, dictionary, begin)
        if check in check_dictionary:
            for i in range(0, len(node.vehicles)):
                # move vertical vehicles
                if node.vehicles[i].orientation == "V":
                    # use deepcopy to make a copy of nodes and the objects in node
                    new_node = node.copy_grid()
                    if new_node.vehicles[i].move("up", new_node) != False:
                        # add new set-up to queue
                        string = make_string(new_node.vehicles)
                        if string not in dictionary:
                            add_dictionary(string, dictionary, check)
                            queue.append(new_node)
                    new_node2 = node.copy_grid()
                    if new_node2.vehicles[i].move("down", new_node2) != False:

                        # add new set-up to queue
                        string = make_string(new_node2.vehicles)
                        if string not in dictionary:
                            add_dictionary(string, dictionary, check)
                            queue.append(new_node2)


                # move horizontal vehicles
                elif node.vehicles[i].orientation == "H":
                    new_node = node.copy_grid()
                    if new_node.vehicles[i].move("left", new_node) != False:

                        # add set-up to dictionary
                        string = make_string(new_node.vehicles)
                        if string not in dictionary:
                            add_dictionary(string, dictionary, check)
                            queue.append(new_node)
                    new_node2 = node.copy_grid()
                    if new_node2.vehicles[i].move("right", new_node2) != False:

                        # check if the car is at the exit
                        if new_node2.car_at_exit(new_node2.vehicles[i].pos):
                            print "klaar ermee"
                            print "--- %s seconds ---" % (time.time() - start_time)
                            return amount_steps(dictionary, check, begin)

                        # add new set-up to queue
                        else:
                            string = make_string(new_node2.vehicles)
                            if string not in dictionary:
                                add_dictionary(string, dictionary, check)
                                queue.append(new_node2)

def make_string(vehicles):
    """
    Creates a unique string of the position coordinates
    of all vehicles in the current grid.
    """
    string = ""
    for vehicle in vehicles:
        string = string + str(vehicle)
    return string

def add_dictionary(string, dictionary, check):
    dict1 = {string: check}
    dictionary.update(dict1)

def amount_steps(dictionary, parent, begin):
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
