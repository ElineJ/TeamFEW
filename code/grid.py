from positions import *
from car import *
from truck import *
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

        # remove the positions for vehicles from empty grid
        #TODO: dit deel werkt niet!
        # print "Vehicles:", len(self.all_vehicles)
        # for i in range(0, len(self.all_vehicles)):
        #     print "Test"
        #     empty_pos1 = GridPosition(self.all_vehicles[i].pos.x1, self.all_vehicles[i].pos.y1)
        #     empty_pos2 = GridPosition(self.all_vehicles[i].pos.x2, self.all_vehicles[i].pos.y2)
        #     if isinstance(self.all_vehicles[i], Truck):
        #         print "Truck"
        #         empty_pos3 = GridPosition(self.all_vehicles[i].pos.x3, self.all_vehicles[i].pos.y3)
        #     for j in range(0, len(self.empty_grid)):
        #         if isinstance(self.all_vehicles[i], Car):
        #             if self.empty_grid[j] == empty_pos1 or self.empty_grid[j] == empty_pos2:
        #                 #self.empty_grid[j].remove
        #                 del self.empty_grid[j]
        #                 print "Removed empty tile!"
        #         elif isinstance(self.all_vehicles[i], Truck):
        #             if self.empty_grid[j] == empty_pos1 or self.empty_grid[j] == empty_pos2 or self.empty_grid[j] == empty_pos3:
        #                 del self.empty_grid[j]
        #                 print "Removed empty tile!"

    def isRedOnExit(self, pos):
        """
        Checks if the red car is at the exit

        Returns True if it is, False if it isn't
        """
        if pos == self.exit:
            return True
        return False

    def isPositionEmpty(self, pos):
        for i in range(0, len(self.empty_grid)):
            if pos.x == self.empty_grid[i].x and pos.y == self.empty_grid[i].y:
                return True
        return False

    def updateEmptyPosition(self, pos, new_pos):
        for i in range(0, len(self.empty_grid)):
            if pos == self.empty_grid[i]:
                self.empty_grid[i] = new_pos

    def removeEmptyGrid(self):
        #TODO: dit deel werkt niet!
        print "Vehicles:", len(self.all_vehicles)
        for i in range(0, len(self.all_vehicles)):
            print "Test"
            empty_pos1 = GridPosition(self.all_vehicles[i].pos.x1, self.all_vehicles[i].pos.y1)
            empty_pos2 = GridPosition(self.all_vehicles[i].pos.x2, self.all_vehicles[i].pos.y2)
            if isinstance(self.all_vehicles[i], Truck):
                print "Truck"
                empty_pos3 = GridPosition(self.all_vehicles[i].pos.x3, self.all_vehicles[i].pos.y3)
            for j in range(0, len(self.empty_grid)):
                if isinstance(self.all_vehicles[i], Car):
                    if self.empty_grid[j] == empty_pos1 or self.empty_grid[j] == empty_pos2:
                        #self.empty_grid[j].remove
                        del self.empty_grid[j]
                        print "Removed empty tile!"
                elif isinstance(self.all_vehicles[i], Truck):
                    if self.empty_grid[j] == empty_pos1 or self.empty_grid[j] == empty_pos2 or self.empty_grid[j] == empty_pos3:
                        del self.empty_grid[j]
                        print "Removed empty tile!"
