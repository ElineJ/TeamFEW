import visualize as vis
import grid
import car
import truck
import random
import time
start_time = time.time()


def runcombo(grid, exit, num_runs, max_moves):
    grid_bfs = grid.copy_grid()
    check_dictionary = {}
    start_time = time.time()

    for i in range(0, num_runs):
        new_grid = grid.copy_grid()
        random_dictionary = {}
        vehicles = new_grid.vehicles
        not_at_exit = True
        moves = 0

        string = make_string(vehicles)
        if string not in random_dictionary:
            add_random_dictionary(string, random_dictionary)
        # open window with visualization
        # anim = vis.Visualization(width, width, vehicles)
        while moves < max_moves and not_at_exit:
            for vehicle in vehicles:
                number = random.randint(0, 1)
                # move vertical car in a random direction
                if vehicle.orientation == 'V':
                    v_direction = [vehicle.up, vehicle.down]
                    if v_direction[number](grid):
                        check = make_string(vehicles)

                        if check not in random_dictionary:
                            moves += 1
                            add_random_dictionary(check, random_dictionary)

                # move horizontal car into a random direction
                elif vehicle.orientation == 'H':
                    h_direction = [vehicle.left, vehicle.right]
                    if h_direction[number](grid):
                        check = make_string(vehicles)

                        if check not in random_dictionary:
                            moves += 1
                            add_random_dictionary(check, random_dictionary)

                            # check if car is at exit
                        if grid.car_at_exit(vehicle.pos):
                            # print "Found exit!"
                            print moves
                            if moves < max_moves:
                                check_dictionary = dict(check_dictionary.items() + random_dictionary.items())
                            not_at_exit = False

    runbfs(grid_bfs, exit, check_dictionary)


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
    # vehicles = grid.vehicles
    begin = make_string(grid.vehicles)
    while queue:
        # check initial board
        node = queue.pop(0)
        parent = make_string(node.vehicles)
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
    string = make_string(node.vehicles)
    if string not in dictionary:
        add_dictionary(string, parent)
        queue.append(node)


def make_string(vehicles):
    """
    Creates a unique string of the position coordinates
    of all vehicles in the current grid.
    """
    return ''.join([str(vehicle) for vehicle in vehicles])


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
