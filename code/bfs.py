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
            for Car in vehicles:
                # try moving them in both directions
                # vehicles has to be updated

                print 'Car visited'                

                # add this instance to the visited set-ups
                visited.add(instance)

                # add new set-up to queueu
                queue.extend(vehicles)

            for Truck in vehicles:


                visited.add(instance)
                queue.extend(vehicles)
