from positions import *
# import visualize

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
                new_grid = GridPosition(i, j)
                empty_grid.append(new_grid)


    def isRedOnExit(self, pos):
        """
        Checks if the red car is at the exit

        Returns True if it is, False if it isn't
        """
        if pos == self.exit:
            return True
        return False

    def isPositionEmpty(self, pos):
        print pos.x
        print pos.y
        for i in range(0, len(self.empty_grid)):

            if pos.x == self.empty_grid[i].x and pos.y == self.empty_grid[i].y:
                return True
        return False

    def updateEmptyPosition(self, pos, new_pos):
        for i in range(0, len(self.empty_grid)):
            if pos == self.empty_grid[i]:
                self.empty_grid[i] = new_pos
