import visualize as vis
import grid
import car
import truck
import random
import time

start_time = time.time()
def runrandom(grid, exit):

    v_direction = ["up", "down"]
    h_direction = ["left", "right"]
    vehicles = grid.all_vehicles
    moves = 0;
    # anim = vis.Visualization(6, 6, grid.all_vehicles)

    while True:
        for i in range(0, len(vehicles)):
            if isinstance(vehicles[i], car.Car):
                direction = random.randint(0, 1)
                # move vertical car in a random direction
                if vehicles[i].orientation == 'V':
                    d = v_direction[direction]
                    # print "Current position car:", vehicles[i].pos.x1, vehicles[i].pos.x2, vehicles[i].pos.y1, vehicles[i].pos.y2
                    if vehicles[i].moveCar(vehicles[i].getCarPosition, d, grid) != False:
                        # print "Car moved up/down"
                        moves += 1
                        # anim.update(vehicles)
                # move horizontal car into a random direction
                else:
                    d = h_direction[direction]
                    # print "Current position car:", vehicles[i].pos.x1, vehicles[i].pos.x2, vehicles[i].pos.y1, vehicles[i].pos.y2
                    if vehicles[i].moveCar(vehicles[i].getCarPosition, d, grid) != False:
                        # print "Car moved left/right"
                        moves += 1
                        # anim.update(vehicles)
                        # check if car is at exit
                        if vehicles[i].pos.x2 == exit.x and vehicles[i].pos.y2 == exit.y:
                            print "Found exit!"
                            print "Moves:", moves
                            print("--- %s seconds ---" % (time.time() - start_time))
                            # print moves,("%s seconds" % (time.time() - start_time))
                            return False

            elif isinstance(vehicles[i], truck.Truck):
                direction = random.randint(0, 1)
                # print "Current position truck:", vehicles[i].pos.x1, vehicles[i].pos.x2, vehicles[i].pos.x3, vehicles[i].pos.y1, vehicles[i].pos.y2, vehicles[i].pos.y3
                # move vertical truck in a random direction
                if vehicles[i].orientation == 'V':
                    # print "Truck"
                    d = v_direction[direction]
                    # print d
                    if vehicles[i].moveTruck(vehicles[i].getTruckPosition, d, grid) != False:
                        moves += 1
                        # anim.update(vehicles)
                # move horizontal truck into a random direction
                else:
                    d = h_direction[direction]
                    print "Current position truck:", vehicles[i].pos.x1, vehicles[i].pos.x2, vehicles[i].pos.x3, vehicles[i].pos.y1, vehicles[i].pos.y2,  vehicles[i].pos.y3
                    print d
                    if vehicles[i].moveTruck(vehicles[i].getTruckPosition, d, grid) != False:
                        moves += 1
                        # anim.update(vehicles)
