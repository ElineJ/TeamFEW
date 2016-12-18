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

    def getTruckPosition(self):
        """
        Returns the current position of vehicle
        """
        return self.pos

    def setTruckPosition(self, old_pos, new_pos, Grid):
        """
        Set the position of the truck to position

        position: a Position object.
        """
        for i in range(0, len(Grid.vehicles)):
            if isinstance(Grid.vehicles[i], Truck):
                if (Grid.vehicles[i].pos.x1 == old_pos.x1 and
                   Grid.vehicles[i].pos.y1 == old_pos.y1 and
                   Grid.vehicles[i].pos.x2 == old_pos.x2 and
                   Grid.vehicles[i].pos.y2 == old_pos.y2 and
                   Grid.vehicles[i].pos.x3 == old_pos.x3 and
                   Grid.vehicles[i].pos.y3 == old_pos.y3):
                    Grid.vehicles[i].pos = new_pos
        self.pos = new_pos

    def move(self, direction, Grid):
        """
        Moves truck to new position
        """

        old_pos = self.getTruckPosition()

        # movement for vertical Truck
        if self.orientation == 'V':
            # move vertical Truck up
            if direction == 'up':
                y1 = self.pos.y1 - 1
                y2 = self.pos.y2 - 1
                y3 = self.pos.y3 - 1
                new_pos = pos.TruckPosition(self.pos.x1, self.pos.x2, self.pos.x3, y1, y2, y3)
                check_pos = pos.GridPosition(self.pos.x1, y1)
                empty_pos = pos.GridPosition(self.pos.x3, self.pos.y3)
                if Grid.isPositionEmpty(check_pos):
                    Grid.updateEmptyPosition(check_pos, empty_pos)
                    self.setTruckPosition(old_pos, new_pos, Grid)
                else:
                    return False
            elif direction == 'down':
                # move vertical Truck down
                y1 = self.pos.y1 + 1
                y2 = self.pos.y2 + 1
                y3 = self.pos.y3 + 1
                new_pos = pos.TruckPosition(self.pos.x1, self.pos.x2, self.pos.x3, y1, y2, y3)
                check_pos = pos.GridPosition(self.pos.x1, y3)
                empty_pos = pos.GridPosition(self.pos.x1, self.pos.y1)
                if Grid.isPositionEmpty(check_pos):
                    Grid.updateEmptyPosition(check_pos, empty_pos)
                    self.setTruckPosition(old_pos, new_pos, Grid)
                else:
                    return False

        elif self.orientation == 'H':
            if direction == 'left':
                # move horizontal Truck left
                x1 = self.pos.x1 - 1
                x2 = self.pos.x2 - 1
                x3 = self.pos.y3 - 1
                new_pos = pos.TruckPosition(x1, x2, x3, self.pos.y1, self.pos.y2, self.pos.y3)
                check_pos = pos.GridPosition(x1, self.pos.y1)
                empty_pos = pos.GridPosition(self.pos.x3, self.pos.y3)
                if Grid.isPositionEmpty(check_pos):
                    Grid.updateEmptyPosition(check_pos, empty_pos)
                    self.setTruckPosition(old_pos, new_pos, Grid)
                else:
                    return False
            elif direction == 'right':
                # move horizontal Truck right
                x1 = self.pos.x1 + 1
                x2 = self.pos.x2 + 1
                x3 = self.pos.y3 + 1
                new_pos = pos.TruckPosition(x1, x2, x3, self.pos.y1, self.pos.y2, self.pos.y3)
                check_pos = pos.GridPosition(x3, self.pos.y1)
                empty_pos = pos.GridPosition(self.pos.x1, self.pos.y1)
                if Grid.isPositionEmpty(check_pos):
                    Grid.updateEmptyPosition(check_pos, empty_pos)
                    self.setTruckPosition(old_pos, new_pos, Grid)
                else:
                    return False

    def checkMove(self, direction, Grid):
        """
        Checks if car can move to next position
        """
        old_pos = self.getTruckPosition()

        # movement for vertical Truck
        if self.orientation == 'V':
            # move vertical Truck up
            if direction == 'up':
                y1 = self.pos.y1 - 1
                y2 = self.pos.y2 - 1
                y3 = self.pos.y3 - 1
                new_pos = pos.TruckPosition(self.pos.x1, self.pos.x2, self.pos.x3, y1, y2, y3)
                check_pos = pos.GridPosition(self.pos.x1, y1)
                empty_pos = pos.GridPosition(self.pos.x3, self.pos.y3)
                if Grid.isPositionEmpty(check_pos):
                    return True
                else:
                    return False
            elif direction == 'down':
                # move vertical Truck down
                y1 = self.pos.y1 + 1
                y2 = self.pos.y2 + 1
                y3 = self.pos.y3 + 1
                new_pos = pos.TruckPosition(self.pos.x1, self.pos.x2, self.pos.x3, y1, y2, y3)
                check_pos = pos.GridPosition(self.pos.x1, y3)
                empty_pos = pos.GridPosition(self.pos.x1, self.pos.y1)
                if Grid.isPositionEmpty(check_pos):
                    return True
                else:
                    return False

        elif self.orientation == 'H':
            if direction == 'left':
                # move horizontal Truck left
                x1 = self.pos.x1 - 1
                x2 = self.pos.x2 - 1
                x3 = self.pos.y3 - 1
                new_pos = pos.TruckPosition(x1, x2, x3, self.pos.y1, self.pos.y2, self.pos.y3)
                check_pos = pos.GridPosition(x1, self.pos.y1)
                empty_pos = pos.GridPosition(self.pos.x3, self.pos.y3)
                if Grid.isPositionEmpty(check_pos):
                    return True
                else:
                    return False
            elif direction == 'right':
                # move horizontal Truck right
                x1 = self.pos.x1 + 1
                x2 = self.pos.x2 + 1
                x3 = self.pos.y3 + 1
                new_pos = pos.TruckPosition(x1, x2, x3, self.pos.y1, self.pos.y2, self.pos.y3)
                check_pos = pos.GridPosition(x3, self.pos.y1)
                empty_pos = pos.GridPosition(self.pos.x1, self.pos.y1)
                if Grid.isPositionEmpty(check_pos):
                    return True
                else:
                    return False
