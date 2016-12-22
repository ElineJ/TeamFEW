import csv
import sys
import visualize as vis
import car
import truck
import grid
import csvtries
import positions as pos

games = ['none', '../datasets/Game #1.csv', '../datasets/Game #2.csv',
         '../datasets/Game #3.csv', '../datasets/Game #4.csv',
         '../datasets/Game #5.csv', '../datasets/Game #6.csv',
         '../datasets/Game #7.csv']

# TODO: add datasets
datasets = ['none', '../results/gameresult1.csv', '..results/gameresult2.csv',
        '../results/gameresult3.csv']

def run():
    """
    Visualizes one of the games using a dataset containing the path
    found using the breadth-first search algorithm.
    """

    # create list of steps
    steps = []

    # get the dataset of the path
    data = int(sys.argv[1])
    if data == 0 or data > 7:
        sys.exit("Game does not exist, choose 1 - 7")
    else:
        f = open(datasets[data], 'rb')
        reader = csv.reader(f)
        steps = list(reader)

    # get the grid of the game
    game = int(sys.argv[2])
    if game == 0 or game > 7:
        sys.exit("Game does not exist, choose 1 - 7")
    else:
        f = open(games[game], 'rb')

    # set up exits for each of the games
    if game == 1 or game == 2 or game == 3:
        exit = pos.CarPosition(4, 5, 2, 2)
        width, height = 6, 6
    elif game == 4 or game == 5 or game == 6:
        exit = pos.CarPosition(7, 8, 4, 4)
        width, height = 9, 9
    elif game == 7:
        exit = pos.CarPosition(10, 11, 5, 5)
        width, height = 12, 12

    # set up grid with vehicles
    grid = csvtries.run(f, width, height, exit)

    # open window with visualization
    anim = vis.Visualization(grid.width, grid.width, grid.vehicles)

    #go through all set ups in list
    for i in range(0, len(steps)):

        for j in range(0, len(steps[i])):

            counter = 0

            location_steps = steps[i]

            # change coordinates for cars and trucks in grid
            for k in range(0, len(grid.vehicles)):

                string = location_steps[j]

                if isinstance(grid.vehicles[k], truck.Truck):
                    grid.vehicles[k].pos.x1 = string[counter]
                    grid.vehicles[k].pos.x2 = string[counter + 1]
                    grid.vehicles[k].pos.x3 = string[counter + 2]
                    grid.vehicles[k].pos.y1 = string[counter + 3]
                    grid.vehicles[k].pos.y2 = string[counter + 4]
                    grid.vehicles[k].pos.y3 = string[counter + 5]
                    counter += 6
                elif isinstance(grid.vehicles[k], car.Car):
                    grid.vehicles[k].pos.x1 = string[counter]
                    grid.vehicles[k].pos.x2 = string[counter + 1]
                    grid.vehicles[k].pos.y1 = string[counter + 2]
                    grid.vehicles[k].pos.y2 = string[counter + 3]
                    counter += 4

            # update animation
            anim.update(grid.vehicles)

run()
