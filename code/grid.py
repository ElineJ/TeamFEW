import positions as pos
import car
import truck

# === Grid

class Grid(object):
    """
    Sets up a grid for the game with a given width and height

    Exit: the position of the exit
    all_vehicles: an array of all the vehicle position objects on the board
    """

    def __init__(self, width, height, exit):
        self.width = width
        self.height = height
        self.exit = exit
        all_vehicles = []
        self.all_vehicles = all_vehicles
        empty_grid = []
        self.empty_grid = empty_grid
        for i in range(0, height):
            for j in range(0, width):
                new_grid = pos.GridPosition(i, j)
                empty_grid.append(new_grid)

    # def isRedOnExit(self, pos):
    #     """
    #     Checks if the red car is at the exit
    #
    #     Returns True if it is, False if it isn't
    #     """
    #     if pos == self.exit:
    #         return True
    #     return False

    def isPositionEmpty(self, pos):
        for i in range(0, len(self.empty_grid)):
            if pos.x == self.empty_grid[i].x and pos.y == self.empty_grid[i].y:
                return True
        return False

    def updateEmptyPosition(self, pos, new_pos):
        for i in range(0, len(self.empty_grid)):
            if pos.x == self.empty_grid[i].x and pos.y == self.empty_grid[i].y:
                self.empty_grid[i] = new_pos

    def removeEmptyGrid(self):

        # create GridPosition objects for all vehicle positions
        for i in range(0, len(self.all_vehicles)):
            empty_pos1 = pos.GridPosition(self.all_vehicles[i].pos.x1, self.all_vehicles[i].pos.y1)
            empty_pos2 = pos.GridPosition(self.all_vehicles[i].pos.x2, self.all_vehicles[i].pos.y2)
            if isinstance(self.all_vehicles[i], truck.Truck):
                empty_pos3 = pos.GridPosition(self.all_vehicles[i].pos.x3, self.all_vehicles[i].pos.y3)
            # check for the positions in empty_grid
            for j in reversed(range(0, len(self.empty_grid))):
                if self.empty_grid[j].x == empty_pos1.x and self.empty_grid[j].y == empty_pos1.y:
                    del self.empty_grid[j]

                elif self.empty_grid[j].x == empty_pos2.x and self.empty_grid[j].y == empty_pos2.y:
                    del self.empty_grid[j]

                elif isinstance(self.all_vehicles[i], truck.Truck):
                    if self.empty_grid[j].x == empty_pos3.x and self.empty_grid[j].y == empty_pos3.y:
                        del self.empty_grid[j]
