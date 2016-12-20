import positions as pos
import truck
import car


class Grid(object):
    """
    Sets up a grid for the game with a given width and height

    Exit: the position of the exit
    vehicles: an array of all the vehicle position objects on the board
    """

    def __init__(self, width, height, exit):
        self.width = width
        self.height = height
        self.exit = exit
        vehicles = []
        self.vehicles = vehicles
        empty_grid = []
        self.empty_grid = empty_grid
        for i in range(0, height):
            for j in range(0, width):
                new_grid = pos.GridPosition(i, j)
                empty_grid.append(new_grid)

        # for vehicle in self.vehicles:
        #     if isinstance(vehicle, car.Car):
        #         print "Car:", vehicle.pos.x1, vehicle.pos.x2, vehicle.pos.y1, vehicle.pos.y2
        #     elif isinstance(vehicle, truck.Truck):
        #         print "Truck:", vehicle.pos.x1, vehicle.pos.x2, vehicle.pos.x3,
        #         vehicle.pos.y1, vehicle.pos.y2, vehicle.pos.y3
    # def isRedOnExit(self, pos):
    #     """
    #     Checks if the red car is at the exit
    #
    #     Returns True if it is, False if it isn't
    #     """
    #     if pos == self.exit:
    #         return True
    #     return False

    # @profile
    def isPositionEmpty(self, pos):
        # print "Position:", pos.x, pos.y
        for i in range(0, len(self.empty_grid)):
            # print bool(pos == self.empty_grid[i])
            if pos == self.empty_grid[i]:
                # print "Position Empty"
                return True
        return False

    # @profile
    def updateEmptyPosition(self, pos, new_pos):
        for i in range(0, len(self.empty_grid)):
            if pos == self.empty_grid[i]:
                self.empty_grid[i] = new_pos
                # print "Removed empty pos"

    def removeEmptyGrid(self):

        # create GridPosition objects for all vehicle positions
        for i in range(0, len(self.vehicles)):
            empty_pos1 = pos.GridPosition(self.vehicles[i].pos.x1, self.vehicles[i].pos.y1)
            empty_pos2 = pos.GridPosition(self.vehicles[i].pos.x2, self.vehicles[i].pos.y2)
            if isinstance(self.vehicles[i], truck.Truck):
                empty_pos3 = pos.GridPosition(self.vehicles[i].pos.x3, self.vehicles[i].pos.y3)
            # check for the positions in empty_grid
            for j in reversed(range(0, len(self.empty_grid))):
                if self.empty_grid[j] == empty_pos1:
                    del self.empty_grid[j]
                elif self.empty_grid[j] == empty_pos2:
                    del self.empty_grid[j]
                elif isinstance(self.vehicles[i], truck.Truck):
                    if self.empty_grid[j] == empty_pos3:
                        del self.empty_grid[j]
