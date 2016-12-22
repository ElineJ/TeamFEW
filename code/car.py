"""
Car.py: initializes an object car with a position, orientation and color.
Includes methods for moving car up, down, left or right.
"""

import positions as pos


class Car(object):
    """
    Initalizes an object for a vehicle type of car
    """
    def __init__(self, x1, x2, y1, y2, orientation, color):
        position = pos.CarPosition(x1, x2, y1, y2)
        self.pos = position
        self.orientation = orientation
        self.color = color
        self.old_pos = position
        self.type = "car"

    def __str__(self):
        return (str(self.pos.x1) + str(self.pos.x2) +
                str(self.pos.y1) + str(self.pos.y2))

    def __eq__(self, other):
        return self.type == other.type and self.pos.id == other.pos.id

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.type + self.pos.id)

    def copy_self(self):
        """
        Returns a new instance of Car with attributes identical
        to current car
        """
        return Car(self.pos.x1, self.pos.x2, self.pos.y1,
                   self.pos.y2, self.orientation, self.color)

# === moves for bfs

    @staticmethod
    def setCarPosition(car, direction, a, b, Grid):
        """
        Change the current positions of car to new
        position depending on direction
        """
        if direction == 'up' or direction == 'down':
            Grid.vehicles[car].pos.y1 = a
            Grid.vehicles[car].pos.y2 = b
        elif direction == 'left' or direction == 'right':
            Grid.vehicles[car].pos.x1 = a
            Grid.vehicles[car].pos.x2 = b

    def move_up(self, Grid):
        """
        Checks if car can move up. If True it creates a copy of Grid,
        moves the car in this copy and returns it.
        """
        y1, y2 = self.pos.y1 - 1, self.pos.y2 - 1
        check_pos = pos.GridPosition(self.pos.x1, y1)
        if Grid.isPositionEmpty(check_pos):
            new_grid = Grid.copy_grid()
            empty_pos = pos.GridPosition(self.pos.x2, self.pos.y2)
            new_grid.updateEmptyPosition(check_pos, empty_pos)
            car = Grid.vehicles.index(self)
            self.setCarPosition(car, "up", y1, y2, new_grid)
            return new_grid
        return False

    def move_down(self, Grid):
        """
        Checks if car can move down. If True it creates a copy of Grid,
        moves the car in this copy and returns it.
        """
        y1, y2 = self.pos.y1 + 1, self.pos.y2 + 1
        check_pos = pos.GridPosition(self.pos.x2, y2)
        if Grid.isPositionEmpty(check_pos):
            new_grid = Grid.copy_grid()
            empty_pos = pos.GridPosition(self.pos.x1, self.pos.y1)
            new_grid.updateEmptyPosition(check_pos, empty_pos)
            car = Grid.vehicles.index(self)
            self.setCarPosition(car, "down", y1, y2, new_grid)
            return new_grid
        return False

    def move_left(self, Grid):
        """
        Checks if car can move left. If True it creates a copy of Grid,
        moves the car in this copy and returns it.
        """
        x1, x2 = self.pos.x1 - 1, self.pos.x2 - 1
        check_pos = pos.GridPosition(x1, self.pos.y1)
        if Grid.isPositionEmpty(check_pos):
            new_grid = Grid.copy_grid()
            empty_pos = pos.GridPosition(self.pos.x2, self.pos.y2)
            new_grid.updateEmptyPosition(check_pos, empty_pos)
            car = Grid.vehicles.index(self)
            self.setCarPosition(car, "left", x1, x2, new_grid)
            return new_grid
        return False

    def move_right(self, Grid):
        """
        Checks if car can move left. If True it creates a copy of Grid,
        moves the car in this copy and returns it.
        """
        x1, x2 = self.pos.x1 + 1, self.pos.x2 + 1
        check_pos = pos.GridPosition(x2, self.pos.y2)
        # check if move is possible
        if Grid.isPositionEmpty(check_pos):
            new_grid = Grid.copy_grid()
            empty_pos = pos.GridPosition(self.pos.x1, self.pos.y1)
            new_grid.updateEmptyPosition(check_pos, empty_pos)
            car = Grid.vehicles.index(self)
            self.setCarPosition(car, "right", x1, x2, new_grid)
            return new_grid
        return False

# === moves for random

    def setNewPosition(self, direction, a, b, Grid):
        """
        Change the current positions of car to new
        position depending on direction
        """
        car = Grid.vehicles.index(self)
        if direction == 'up' or direction == 'down':
            Grid.vehicles[car].pos.y1 = a
            Grid.vehicles[car].pos.y2 = b
        elif direction == 'left' or direction == 'right':
            Grid.vehicles[car].pos.x1 = a
            Grid.vehicles[car].pos.x2 = b
        self.pos = Grid.vehicles[car].pos

    def up(self, Grid):
        """
        Check if car can move up. If it can, moves car in
        current Grid and returns True.
        """
        y1, y2 = self.pos.y1 - 1, self.pos.y2 - 1
        check_pos = pos.GridPosition(self.pos.x1, y1)
        if Grid.isPositionEmpty(check_pos):
            empty_pos = pos.GridPosition(self.pos.x2, self.pos.y2)
            Grid.updateEmptyPosition(check_pos, empty_pos)
            self.setNewPosition("up", y1, y2, Grid)
            return True
        return False

    def down(self, Grid):
        """
        Check if car can move down. If it can, moves car in
        current Grid and returns True.
        """
        y1, y2 = self.pos.y1 + 1, self.pos.y2 + 1
        check_pos = pos.GridPosition(self.pos.x2, y2)
        if Grid.isPositionEmpty(check_pos):
            empty_pos = pos.GridPosition(self.pos.x1, self.pos.y1)
            Grid.updateEmptyPosition(check_pos, empty_pos)
            self.setNewPosition("down", y1, y2, Grid)
            return True
        return False

    def left(self, Grid):
        """
        Check if car can move left. If it can, moves car in
        current Grid and returns True.
        """
        x1, x2 = self.pos.x1 - 1, self.pos.x2 - 1
        check_pos = pos.GridPosition(x1, self.pos.y1)
        if Grid.isPositionEmpty(check_pos):
            empty_pos = pos.GridPosition(self.pos.x2, self.pos.y2)
            Grid.updateEmptyPosition(check_pos, empty_pos)
            self.setNewPosition("left", x1, x2, Grid)
            return True
        return False

    def right(self, Grid):
        """
        Check if car can move right. If it can, moves car in
        current Grid and returns True.
        """
        x1, x2 = self.pos.x1 + 1, self.pos.x2 + 1
        check_pos = pos.GridPosition(x2, self.pos.y2)
        if Grid.isPositionEmpty(check_pos):
            empty_pos = pos.GridPosition(self.pos.x1, self.pos.y1)
            Grid.updateEmptyPosition(check_pos, empty_pos)
            self.setNewPosition("right", x1, x2, Grid)
            return True
        return False
