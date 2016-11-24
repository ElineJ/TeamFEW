import grid
from car import *
from truck import *

def runbfs(vehicles, exit):
    # make a list of all states that have happened
    visited = []

    queue = []
    # make a queue of next steps
    queue = [vehicles]

    while queue:
        # delete this grid set up from queue and save in instance
        instance = queue.pop(0)

        if instance not in visited:
            # add this instance to the visited set-ups
            visited.append(instance)

            for Car in instance:
                # try moving them in both directions
                # vehicles has to be updated

                if Car.orientation == "v":
                    Car_down = Car
                    print "Vertical car"

                    if Car.moveCar(Car.getCarPosition, "up") == True:
                        Car.moveCar(Car.getCarPosition, "up")

                        if CarPosition == exit:
                            return instance
                            break
                        # vehicles = new set-up
                        # add new set-up to queue
                        else:
                            queue.append(instance)

                    if Car.moveCar(Car_down.getCarPosition, "down") == True:
                        Car.moveCar(Car_down.getCarPosition, "down")

                        if CarPosition == exit:
                            return instance
                            break
                        # vehicles = new set-up
                        # add new set-up to queue
                        else:
                            queue.append(instance)

                if Car.orientation == "H":
                    Car_right = Car
                    print "Horizontal car"

                    if Car.moveCar(Car.getCarPosition, "left") == True:
                        Car.moveCar(Car.getCarPosition, "left")

                        if CarPosition == exit:
                            return instance
                            break
                        # vehicles = new set-up
                        # add new set-up to queue
                        else:
                            queue.append(instance)


                    if Car.moveCar(Car_right.getCarPosition, "right") == True:
                        Car.moveCar(Car_right.getCarPosition, "right")

                        if CarPosition == exit:
                            return instance
                            break
                        # vehicles = new set-up
                        # add new set-up to queue
                        else:
                            queue.append(instance)

            for Truck in instance:
                if Truck.orientation == "V":
                    Truck_down = Truck
                    print "Vertical truck"

                    if moveTruck(Truck.getTruckPosition, "up") == True:
                        moveTruck(Truck.getTruckPosition, "up")

                        # vehicles = new set-up
                        # add new set-up to queue
                        queue.append(instance)

                    if moveTruck(Truck_down.getTruckPosition, "down") == True:
                        moveTruck(Truck_down.getTruckPosition, "down")

                        # vehicles = new set-up
                        # add new set-up to queue
                        queue.append(instance)

                if Truck.orientation == "H":
                    Truck_right = Truck
                    print "Horizontal Truck"

                    if moveTruck(Truck.getTruckPosition, "left") == True:
                        moveTruck(Truck.getTruckPosition, "left")

                        # vehicles = new set-up
                        # add new set-up to queue
                        queue.append(instance)

                    if moveTruck(Truck_right.getTruckPosition, "right") == True:
                        moveTruck(Truck_right.getTruckPosition, "right")

                        # vehicles = new set-up
                        # add new set-up to queue
                        queue.append(instance)
        print queue
        print visited
