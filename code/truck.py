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

    def getTruckPosition(self):
        """
        Returns the current position of vehicle
        """
        return self.pos

    # @profile
    def setTruckPosition(self, old_pos, new_pos, Grid):
        """
        Set the position of the truck to position

        position: a Position object.
        """
        truck = Grid.vehicles.index(self)
        Grid.vehicles[truck].pos = new_pos
        self.pos = new_pos

    # @profile
    def move(self, direction, Grid):
        """
        Moves truck to new position
        """

        # movement for vertical Truck
        if self.orientation == 'V':
            # move vertical Truck up
            if direction == 'up':
                y1 = self.pos.y1 - 1
                y2 = self.pos.y2 - 1
                y3 = self.pos.y3 - 1
                check_pos = pos.GridPosition(self.pos.x1, y1)
                if Grid.isPositionEmpty(check_pos):
                    new_pos = pos.TruckPosition(self.pos.x1, self.pos.x2, self.pos.x3, y1, y2, y3)
                    empty_pos = pos.GridPosition(self.pos.x3, self.pos.y3)
                    Grid.updateEmptyPosition(check_pos, empty_pos)
                    self.setTruckPosition(self.pos, new_pos, Grid)
                else:
                    return False
            elif direction == 'down':
                # move vertical Truck down
                y1 = self.pos.y1 + 1
                y2 = self.pos.y2 + 1
                y3 = self.pos.y3 + 1
                check_pos = pos.GridPosition(self.pos.x1, y3)
                if Grid.isPositionEmpty(check_pos):
                    new_pos = pos.TruckPosition(self.pos.x1, self.pos.x2, self.pos.x3, y1, y2, y3)
                    empty_pos = pos.GridPosition(self.pos.x1, self.pos.y1)
                    Grid.updateEmptyPosition(check_pos, empty_pos)
                    self.setTruckPosition(self.pos, new_pos, Grid)
                else:
                    return False

        elif self.orientation == 'H':
            if direction == 'left':
                # move horizontal Truck left
                x1 = self.pos.x1 - 1
                x2 = self.pos.x2 - 1
                x3 = self.pos.x3 - 1
                check_pos = pos.GridPosition(x1, self.pos.y1)
                if Grid.isPositionEmpty(check_pos):
                    new_pos = pos.TruckPosition(x1, x2, x3, self.pos.y1, self.pos.y2, self.pos.y3)
                    empty_pos = pos.GridPosition(self.pos.x3, self.pos.y3)
                    Grid.updateEmptyPosition(check_pos, empty_pos)
                    self.setTruckPosition(self.pos, new_pos, Grid)
                else:
                    return False
            elif direction == 'right':
                # move horizontal Truck right
                x1 = self.pos.x1 + 1
                x2 = self.pos.x2 + 1
                x3 = self.pos.x3 + 1
                check_pos = pos.GridPosition(x3, self.pos.y1)
                if Grid.isPositionEmpty(check_pos):
                    new_pos = pos.TruckPosition(x1, x2, x3, self.pos.y1, self.pos.y2, self.pos.y3)
                    empty_pos = pos.GridPosition(self.pos.x1, self.pos.y1)
                    Grid.updateEmptyPosition(check_pos, empty_pos)
                    self.setTruckPosition(self.pos, new_pos, Grid)
                else:
                    return False

    def checkMove(self, direction, Grid):
        """
        Checks if car can move to next position
        """
        # movement for vertical Truck
        if self.orientation == 'V':
            # move vertical Truck up
            if direction == 'up':
                y1 = self.pos.y1 - 1
                check_pos = pos.GridPosition(self.pos.x1, y1)
                return bool(Grid.isPositionEmpty(check_pos))
            elif direction == 'down':
                # move vertical Truck down
                y3 = self.pos.y3 + 1
                check_pos = pos.GridPosition(self.pos.x1, y3)
                return bool(Grid.isPositionEmpty(check_pos))

        elif self.orientation == 'H':
            if direction == 'left':
                # move horizontal Truck left
                x1 = self.pos.x1 - 1
                check_pos = pos.GridPosition(x1, self.pos.y1)
                return bool(Grid.isPositionEmpty(check_pos))

            elif direction == 'right':
                # move horizontal Truck right
                x3 = self.pos.y3 + 1
                check_pos = pos.GridPosition(x3, self.pos.y1)
                return bool(Grid.isPositionEmpty(check_pos))
