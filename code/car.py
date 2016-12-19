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

    # def __eq__(self, other):
    #     return (self.pos == other.pos)
    #
    # def __ne__(self, other):
    #     return not self.__eq__(other)

    def setCarPosition(self, old_pos, new_pos, Grid):
        """
        Set the position of the car to position

        position: a Position object.
        """
        for i in range(0, len(Grid.vehicles)):
            if isinstance(Grid.vehicles[i], Car):
                if (Grid.vehicles[i].pos.x1 == old_pos.x1 and
                   Grid.vehicles[i].pos.y1 == old_pos.y1 and
                   Grid.vehicles[i].pos.x2 == old_pos.x2 and
                   Grid.vehicles[i].pos.y2 == old_pos.y2):
                    Grid.vehicles[i].pos = new_pos
        self.pos = new_pos

    def setPreviousPos(self, old_pos, new_pos, Grid):
        """
        Set the position of the car to position

        position: a Position object.
        """
        for i in range(0, len(Grid.vehicles)):
            if isinstance(Grid.vehicles[i], Car):
                if (Grid.vehicles[i].pos.x1 == new_pos.x1 and
                   Grid.vehicles[i].pos.y1 == new_pos.y1 and
                   Grid.vehicles[i].pos.x2 == new_pos.x2 and
                   Grid.vehicles[i].pos.y2 == new_pos.y2):
                    Grid.vehicles[i].pos = old_pos
        self.pos = old_pos

    def move(self, direction, Grid):
        """
        Moves car to new position
        """
        self.old_pos = self.pos

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
                    self.setCarPosition(self.old_pos, new_pos, Grid)
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
                    self.setCarPosition(self.old_pos, new_pos, Grid)
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
                    self.setCarPosition(self.old_pos, new_pos, Grid)
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
                    self.setCarPosition(self.old_pos, new_pos, Grid)
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
