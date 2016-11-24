import grid
import car
import truck

def runbfs(vehicles):
    # make a list of all states that have happened
    visited = []

    # make a queue of next steps
    queue = [vehicles]

    while queue:
        # delete this grid set up from queue and save in instance
        instance = queue.pop(0)

        if instance not in visited:
            for Car in instance:
                # try moving them in both directions
                # vehicles has to be updated

                if Car.orientation = "V":
                    print "Vertical car"

                    # add this instance to the visited set-ups
                    visited.add(instance)

                    # vehicles = new set-up
                    # add new set-up to queueu
                    queue.extend(vehicles)

                if Car.orientation = "H":
                    print "Horizontal car"

                    # add this instance to the visited set-ups
                    visited.add(instance)

                    # add new set-up to queueu
                    queue.extend(vehicles)


            for Truck in vehicles:


                visited.add(instance)
                queue.extend(vehicles)
