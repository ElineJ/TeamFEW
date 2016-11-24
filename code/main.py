# main code to run the simulation

import positions
import grid
import truck
import car
import visualize
import csvtries
import sys      # imports the sys module

# open csv file
f = open(sys.argv[1], 'rb')

# get grid size
s = sys.argv[2]

exit = positions.CarPosition(4, 2, 5, 2)
#Grid = positions.Grid(s, s, exit)

print s


csvtries.run(f)
position = Grid.all_vehicles.Car[0].getCarPosition
newGrid.all_vehicles.Car[0].moveCar(position, )

f.close()
