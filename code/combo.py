import visualize as vis
import grid
import car
import truck
import random
import time
start_time = time.time()


def runcombo(grid, num_runs, max_moves):
    grid_bfs = grid.copy_grid()
    new_dictionary = {}
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
        while moves < max_moves and not_at_exit:
            for vehicle in vehicles:
                number = random.randint(0, 1)
                # move vertical car in a random direction
                if vehicle.orientation == 'V':
                    v_direction = [vehicle.up, vehicle.down]
                    if v_direction[number](new_grid):
                        check = make_string(vehicles)

                        if check not in random_dictionary:
                            moves += 1
                            add_random_dictionary(check, random_dictionary)

                # move horizontal car into a random direction
                elif vehicle.orientation == 'H':
                    h_direction = [vehicle.left, vehicle.right]
                    if h_direction[number](new_grid):
                        check = make_string(vehicles)

                        if check not in random_dictionary:
                            moves += 1
                            add_random_dictionary(check, random_dictionary)

                        # check if car is at exit
                        if new_grid.car_at_exit(vehicle.pos):
                            if moves < max_moves:
                                new_dictionary = dict(new_dictionary.items() + random_dictionary.items())
                            not_at_exit = False

    runbfs(grid_bfs, exit, new_dictionary)


def runbfs(grid, exit, new_dictionary):
    """
    Breadth First Search algorithm that finds the shortest path
    for the red car to get to the exit.
    """
    # make a list of all states that have happened
    print "dit is de lengte van de dict = " + str(len(new_dictionary))
    global dictionary
    global begin
    global parent
    global queue
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
                    return counter
                parent = value


def add_random_dictionary(string, random_dictionary):
    dict2 = {string: True}
    random_dictionary.update(dict2)
