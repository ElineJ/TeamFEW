# main code to run the simulation

import positions
import grid
import truck
import car
import visualize
import csvtries

# open csv file
f = open(sys.argv[1], 'rb')

# get grid size
s = open(sys.argv[2])

exit = CarPosition(4, 2, 5, 2)
Grid = Grid(s, s, exit)
csvtries.run(f)
position = all_vehicles.Car[0].getCarPosition
newGrid.all_vehicles.Car[0].moveCar(position, )
