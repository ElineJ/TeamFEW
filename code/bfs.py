from grid import *
from car import *
from truck import *

def runbfs(grid, exit):
    # make a list of all states that have happened
    visited = []

    queue = []
    # make a queue of next steps
    queue = [grid.all_vehicles]

    while queue:
        # delete this grid set up from queue and save in node
        node = queue.pop(0)

        if node not in visited:
            # add this node to the visited set-ups
            visited.append(node)

            for Car in node:
                # try moving them in both directions
                # grid has to be updated

                if Car.orientation == "V":
                    Car_down = Car
                    print "Vertical car"

                    if Car.moveCar(Car.getCarPosition, "up", grid) == True:
                        Car.moveCar(Car.getCarPosition, "up", grid)

                        if CarPosition == exit:
                            return node
                        # grid = new set-up
                        # add new set-up to queue
                        else:
                            queue.append(node)

                    if Car.moveCar(Car_down.getCarPosition, "down", grid) == True:
                        Car.moveCar(Car_down.getCarPosition, "down", grid)

                        if CarPosition == exit:
                            return node
                        # grid = new set-up
                        # add new set-up to queue
                        else:
                            queue.append(node)

                if Car.orientation == "H":
                    Car_right = Car
                    print "Horizontal car"

                    if Car.moveCar(Car.getCarPosition, "left", grid) == True:
                        Car.moveCar(Car.getCarPosition, "left", grid)

                        if CarPosition == exit:
                            return node
                        # grid = new set-up
                        # add new set-up to queue
                        else:
                            queue.append(node)


                    if Car.moveCar(Car_right.getCarPosition, "right", grid) == True:
                        Car.moveCar(Car_right.getCarPosition, "right", grid)

                        if CarPosition == exit:
                            return node
                        # grid = new set-up
                        # add new set-up to queue
                        else:
                            queue.append(node)

            for Truck in node:
                if Truck.orientation == "V":
                    Truck_down = Truck
                    print "Vertical truck"

                    if moveTruck(Truck.getTruckPosition, "up", grid) == True:
                        moveTruck(Truck.getTruckPosition, "up", grid)

                        # grid = new set-up
                        # add new set-up to queue
                        queue.append(node)

                    if moveTruck(Truck_down.getTruckPosition, "down", grid) == True:
                        moveTruck(Truck_down.getTruckPosition, "down", grid)

                        # grid = new set-up
                        # add new set-up to queue
                        queue.append(node)

                if Truck.orientation == "H":
                    Truck_right = Truck
                    print "Horizontal Truck"

                    if moveTruck(Truck.getTruckPosition, "left", grid) == True:
                        moveTruck(Truck.getTruckPosition, "left", grid)

                        # grid = new set-up
                        # add new set-up to queue
                        queue.append(node)

                    if moveTruck(Truck_right.getTruckPosition, "right", grid) == True:
                        moveTruck(Truck_right.getTruckPosition, "right", grid)

                        # grid = new set-up
                        # add new set-up to queue
                        queue.append(node)
        print queue
        print visited
