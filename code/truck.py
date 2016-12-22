import positions as pos


class Truck(object):
    """
    Creates an object for a vehicle type of truck
    """
    def __init__(self, x1, x2, x3, y1, y2, y3, orientation, color):
        position = pos.TruckPosition(x1, x2, x3, y1, y2, y3)
        self.pos = position
        self.orientation = orientation
        self.color = color
        self.type = "truck"

    def __str__(self):
        return (str(self.pos.x1) + str(self.pos.x2) + str(self.pos.x3) +
                str(self.pos.y1) + str(self.pos.y2) + str(self.pos.y3))

    def __eq__(self, other):
        return (self.type == other.type and self.pos.id == other.pos.id)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.type + self.pos.id)

    def copy_self(self):
        """
        Creates a new instance of Truck with attributes of
        truck to be copies
        """
        return Truck(self.pos.x1, self.pos.x2, self.pos.x3,
                     self.pos.y1, self.pos.y2, self.pos.y3,
                     self.orientation, self.color)

# == moves for bfs

    @staticmethod
    def setTruckPosition(truck, direction, a, b, c, Grid):
        """
        Set the position of the truck to position

        position: a Position object.
        """
        if direction == 'up' or direction == 'down':
            Grid.vehicles[truck].pos.y1 = a
            Grid.vehicles[truck].pos.y2 = b
            Grid.vehicles[truck].pos.y3 = c
        elif direction == 'left' or direction == 'right':
            Grid.vehicles[truck].pos.x1 = a
            Grid.vehicles[truck].pos.x2 = b
            Grid.vehicles[truck].pos.x3 = c

    def move_up(self, Grid):
        y1, y2, y3 = self.pos.y1 - 1, self.pos.y2 - 1, self.pos.y3 - 1
        check_pos = pos.GridPosition(self.pos.x1, y1)
        if Grid.isPositionEmpty(check_pos):
            new_grid = Grid.copy_grid()
            empty_pos = pos.GridPosition(self.pos.x3, self.pos.y3)
            new_grid.updateEmptyPosition(check_pos, empty_pos)
            truck = Grid.vehicles.index(self)
            self.setTruckPosition(truck, "up", y1, y2, y3, new_grid)
            return new_grid
        return False

    def move_down(self, Grid):
        y1, y2, y3 = self.pos.y1 + 1, self.pos.y2 + 1, self.pos.y3 + 1
        check_pos = pos.GridPosition(self.pos.x3, y3)
        if Grid.isPositionEmpty(check_pos):
            new_grid = Grid.copy_grid()
            empty_pos = pos.GridPosition(self.pos.x1, self.pos.y1)
            new_grid.updateEmptyPosition(check_pos, empty_pos)
            truck = Grid.vehicles.index(self)
            self.setTruckPosition(truck, "down", y1, y2, y3, new_grid)
            return new_grid
        return False

    def move_left(self, Grid):
        x1, x2, x3 = self.pos.x1 - 1, self.pos.x2 - 1, self.pos.x3 - 1
        check_pos = pos.GridPosition(x1, self.pos.y1)
        if Grid.isPositionEmpty(check_pos):
            new_grid = Grid.copy_grid()
            empty_pos = pos.GridPosition(self.pos.x3, self.pos.y3)
            new_grid.updateEmptyPosition(check_pos, empty_pos)
            truck = Grid.vehicles.index(self)
            self.setTruckPosition(truck, "left", x1, x2, x3, new_grid)
            return new_grid
        return False

    def move_right(self, Grid):
        x1, x2, x3 = self.pos.x1 + 1, self.pos.x2 + 1, self.pos.x3 + 1
        check_pos = pos.GridPosition(x3, self.pos.y3)
        if Grid.isPositionEmpty(check_pos):
            new_grid = Grid.copy_grid()
            empty_pos = pos.GridPosition(self.pos.x1, self.pos.y1)
            new_grid.updateEmptyPosition(check_pos, empty_pos)
            truck = Grid.vehicles.index(self)
            self.setTruckPosition(truck, "right", x1, x2, x3, new_grid)
            return new_grid
        return False

# === moves for random

    def setNewPosition(self, direction, a, b, c, Grid):
        """
        Set the position of the truck to position

        position: a Position object.
        """
        truck = Grid.vehicles.index(self)
        if direction == 'up' or direction == 'down':
            Grid.vehicles[truck].pos.y1 = a
            Grid.vehicles[truck].pos.y2 = b
            Grid.vehicles[truck].pos.y3 = c
        elif direction == 'left' or direction == 'right':
            Grid.vehicles[truck].pos.x1 = a
            Grid.vehicles[truck].pos.x2 = b
            Grid.vehicles[truck].pos.x3 = c
        self.pos = Grid.vehicles[truck].pos

    def up(self, Grid):
        y1, y2, y3 = self.pos.y1 - 1, self.pos.y2 - 1, self.pos.y3 - 1
        check_pos = pos.GridPosition(self.pos.x1, y1)
        if Grid.isPositionEmpty(check_pos):
            empty_pos = pos.GridPosition(self.pos.x3, self.pos.y3)
            Grid.updateEmptyPosition(check_pos, empty_pos)
            self.setNewPosition("up", y1, y2, y3, Grid)
            return True
        return False

    def down(self, Grid):
        y1, y2, y3 = self.pos.y1 + 1, self.pos.y2 + 1, self.pos.y3 + 1
        check_pos = pos.GridPosition(self.pos.x3, y3)
        if Grid.isPositionEmpty(check_pos):
            empty_pos = pos.GridPosition(self.pos.x1, self.pos.y1)
            Grid.updateEmptyPosition(check_pos, empty_pos)
            self.setNewPosition("down", y1, y2, y3, Grid)
            return True
        return False

    def left(self, Grid):
        x1, x2, x3 = self.pos.x1 - 1, self.pos.x2 - 1, self.pos.x3 - 1
        check_pos = pos.GridPosition(x1, self.pos.y1)
        if Grid.isPositionEmpty(check_pos):
            empty_pos = pos.GridPosition(self.pos.x3, self.pos.y3)
            Grid.updateEmptyPosition(check_pos, empty_pos)
            self.setNewPosition("left", x1, x2, x3, Grid)
            return True
        return False

    def right(self, Grid):
        x1, x2, x3 = self.pos.x1 + 1, self.pos.x2 + 1, self.pos.x3 + 1
        check_pos = pos.GridPosition(x3, self.pos.y3)
        if Grid.isPositionEmpty(check_pos):
            empty_pos = pos.GridPosition(self.pos.x1, self.pos.y1)
            Grid.updateEmptyPosition(check_pos, empty_pos)
            self.setNewPosition("right", x1, x2, x3, Grid)
            return True
        return False
