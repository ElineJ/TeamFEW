import positions as pos


class Car(object):
    """
    Creates an object for a vehicle type of car
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
        return (self.type == other.type and self.pos.id == other.pos.id)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.type + self.pos.id)

    def setCarPosition(self, old_pos, new_pos, Grid):
        """
        Set the position of the car to position

        position: a Position object.
        """
        car = Grid.vehicles.index(self)
        Grid.vehicles[car].pos = new_pos
        self.pos = new_pos

    def setPreviousPos(self, old_pos, new_pos, Grid):
        """
        Set the position of the car to position

        position: a Position object.
        """
        for vehicle in Grid.vehicles:
            if isinstance(vehicle, Car):
                if vehicle.pos == new_pos:
                    vehicle.pos = old_pos
        self.pos = old_pos

    def move(self, direction, Grid):
        """
        Moves car to new position
        """

        # movement for vertical car
        if self.orientation == 'V':
            # move vertical car up
            if direction == 'up':
                y1 = self.pos.y1 - 1
                y2 = self.pos.y2 - 1
                new_pos = pos.CarPosition(self.pos.x1, self.pos.x2, y1, y2)
                check_pos = pos.GridPosition(self.pos.x1, y1)
                empty_pos = pos.GridPosition(self.pos.x1, self.pos.y2)
                if Grid.isPositionEmpty(check_pos):
                    Grid.updateEmptyPosition(check_pos, empty_pos)
                    self.setCarPosition(self.pos, new_pos, Grid)
                else:
                    return False
            elif direction == 'down':
                # move vertical car down
                y1 = self.pos.y1 + 1
                y2 = self.pos.y2 + 1
                new_pos = pos.CarPosition(self.pos.x1, self.pos.x2, y1, y2)
                check_pos = pos.GridPosition(self.pos.x2, y2)
                empty_pos = pos.GridPosition(self.pos.x1, self.pos.y1)
                if Grid.isPositionEmpty(check_pos):
                    Grid.updateEmptyPosition(check_pos, empty_pos)
                    self.setCarPosition(self.pos, new_pos, Grid)
                else:
                    return False

        elif self.orientation == 'H':
            if direction == 'left':
                # move horizontal car left
                x1 = self.pos.x1 - 1
                x2 = self.pos.x2 - 1
                new_pos = pos.CarPosition(x1, x2, self.pos.y1, self.pos.y2)
                check_pos = pos.GridPosition(x1, self.pos.y1)
                empty_pos = pos.GridPosition(self.pos.x2, self.pos.y2)
                if Grid.isPositionEmpty(check_pos):
                    Grid.updateEmptyPosition(check_pos, empty_pos)
                    self.setCarPosition(self.pos, new_pos, Grid)
                else:
                    return False

            elif direction == 'right':
                # move horizontal car right
                x1 = self.pos.x1 + 1
                x2 = self.pos.x2 + 1
                new_pos = pos.CarPosition(x1, x2, self.pos.y1, self.pos.y2)
                check_pos = pos.GridPosition(x2, self.pos.y2)
                empty_pos = pos.GridPosition(self.pos.x1, self.pos.y1)
                # check if move is possible
                if Grid.isPositionEmpty(check_pos):
                    Grid.updateEmptyPosition(check_pos, empty_pos)
                    self.setCarPosition(self.pos, new_pos, Grid)
                else:
                    return False

    def checkMove(self, direction, Grid):
        """
        Checks if car can move to next position
        """
        self.old_pos = self.pos

        # movement for vertical car
        if self.orientation == 'V':
            # check if vertical car can move up
            if direction == 'up':
                y1, y2 = self.pos.y1 - 1, self.pos.y2 - 1
                check_pos = pos.GridPosition(self.pos.x1, y1)
                return bool(Grid.isPositionEmpty(check_pos))
            elif direction == 'down':
                # move vertical car down
                y1 = self.pos.y1 + 1
                y2 = self.pos.y2 + 1
                check_pos = pos.GridPosition(self.pos.x2, y2)
                return bool(Grid.isPositionEmpty(check_pos))

        elif self.orientation == 'H':
            if direction == 'left':
                # move horizontal car left
                x1 = self.pos.x1 - 1
                x2 = self.pos.x2 - 1
                check_pos = pos.GridPosition(x1, self.pos.y1)
                return bool(Grid.isPositionEmpty(check_pos))
            elif direction == 'right':
                # move horizontal car right
                x1 = self.pos.x1 + 1
                x2 = self.pos.x2 + 1
                check_pos = pos.GridPosition(x2, self.pos.y2)
                # check if move is possible
                return bool(Grid.isPositionEmpty(check_pos))
