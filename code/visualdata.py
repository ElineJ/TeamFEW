import csv
import sys
import visualize as vis
import car
import truck
import grid

def run():
    game = sys.argv[1]

    steps = []

    with open(game, 'rb') as f:
        reader = csv.reader(f)
        steps = list(reader)
        print "opened game"

    print steps

    # open window with visualization
    anim = vis.Visualization(grid.width, grid.width, grid.vehicles)

    #go through all set ups in list
    for i in range(0, len(steps)):
        counter = 0

        # change coordinates for cars and trucks in grid
        for j in range(0, len(grid.vehicles)):
            string = steps[i]
            if isinstance(grid.vehicles[j], truck.Truck):
                grid.vehicles[j].pos.x1 = string[counter]
                grid.vehicles[j].pos.x2 = string[counter + 1]
                grid.vehicles[j].pos.x3 = string[counter + 2]
                grid.vehicles[j].pos.y1 = string[counter + 3]
                grid.vehicles[j].pos.y2 = string[counter + 4]
                grid.vehicles[j].pos.y3 = string[counter + 5]
                counter += 6
            elif isinstance(grid.vehicles[j], car.Car):
                grid.vehicles[j].pos.x1 = string[counter]
                grid.vehicles[j].pos.x2 = string[counter + 1]
                grid.vehicles[j].pos.y1 = string[counter + 2]
                grid.vehicles[j].pos.y2 = string[counter + 3]
                counter += 4
        anim.update(grid.vehicles)

run()
