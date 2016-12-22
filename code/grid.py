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
        empty_grid = set()
        self.empty_grid = empty_grid

    def car_at_exit(self, pos):
        """
        Checks if the red car is at the exit
        """
        return bool(pos == self.exit)

    def isPositionEmpty(self, pos):

        return bool(pos in self.empty_grid)

    def updateEmptyPosition(self, pos, new_pos):
        """
        Deletes old empty position from grid and adds new empty_position
        """
        self.empty_grid.remove(pos)
        self.empty_grid.add(new_pos)

    def removeEmptyGrid(self):
        # create empty grid for all tiles
        for i in range(0, self.height):
            for j in range(0, self.width):
                new_grid = pos.GridPosition(i, j)
                self.empty_grid.add(new_grid)

        # create GridPosition objects for all vehicle positions
        for i in range(0, len(self.vehicles)):
            empty_pos1 = pos.GridPosition(self.vehicles[i].pos.x1, self.vehicles[i].pos.y1)
            empty_pos2 = pos.GridPosition(self.vehicles[i].pos.x2, self.vehicles[i].pos.y2)
            if empty_pos1 in self.empty_grid:
                self.empty_grid.remove(empty_pos1)
            if empty_pos2 in self.empty_grid:
                self.empty_grid.remove(empty_pos2)
            if isinstance(self.vehicles[i], truck.Truck):
                empty_pos3 = pos.GridPosition(self.vehicles[i].pos.x3, self.vehicles[i].pos.y3)
                if empty_pos3 in self.empty_grid:
                    self.empty_grid.remove(empty_pos3)

    # @profile
    def copy_grid(self):
        """
        Creates a unique copy of current grid
        """
        # create new instance of grid and delete previous attributes
        gridcopy = Grid(self.width, self.height, self.exit)
        gridcopy.empty_grid.clear()
        del gridcopy.vehicles[:]
        # add empty_grid positions
        for empty in self.empty_grid:
            gridcopy.empty_grid.add(pos.GridPosition(empty.x, empty.y))
        # add vehicles to grid
        for vehicle in self.vehicles:
            gridcopy.vehicles.append(vehicle.copy_self())

        return gridcopy
