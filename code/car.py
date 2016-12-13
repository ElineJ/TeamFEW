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

    def getCarPosition(self):
        """
        Returns the current position of vehicle
        """
        return self.pos

    def setCarPosition(self, old_pos, new_pos, Grid):
        """
        Set the position of the car to position

        position: a Position object.
        """
        for i in range(0, len(Grid.all_vehicles)):
            if isinstance(Grid.all_vehicles[i], Car):
                if (Grid.all_vehicles[i].pos.x1 == old_pos.x1 and
                   Grid.all_vehicles[i].pos.y1 == old_pos.y1 and
                   Grid.all_vehicles[i].pos.x2 == old_pos.x2 and
                   Grid.all_vehicles[i].pos.y2 == old_pos.y2):
                    Grid.all_vehicles[i].pos = new_pos
        self.pos = new_pos

    # def setPreviousPos(self, old_pos, new_pos, Grid):
    #     """
    #     Set the position of the car to position
    #
    #     position: a Position object.
    #     """
    #     for i in range(0, len(Grid.all_vehicles)):
    #         if isinstance(Grid.all_vehicles[i], Car):
    #             if (Grid.all_vehicles[i].pos.x1 == new_pos.x1 and
    #                Grid.all_vehicles[i].pos.y1 == new_pos.y1 and
    #                Grid.all_vehicles[i].pos.x2 == new_pos.x2 and
    #                Grid.all_vehicles[i].pos.y2 == new_pos.y2):
    #                 Grid.all_vehicles[i].pos = old_pos
    #     self.pos = old_pos

    def moveCar(self, direction, Grid):
        """
        Moves car to new position
        """
        old_pos = self.getCarPosition()

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
                    self.setCarPosition(old_pos, new_pos, Grid)
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
                    self.setCarPosition(old_pos, new_pos, Grid)
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
                    self.setCarPosition(old_pos, new_pos, Grid)
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
                    self.setCarPosition(old_pos, new_pos, Grid)
                else:
                    return False

    def checkMove(self, direction, Grid):
        """
        Checks if car can move to next position
        """
        old_pos = self.getCarPosition()

        # movement for vertical car
        if self.orientation == 'V':
            # check if vertical car can move up
            if direction == 'up':
                y1, y2 = self.pos.y1 - 1, self.pos.y2 - 1
                new_pos = pos.CarPosition(self.pos.x1, self.pos.x2, y1, y2)
                check_pos = pos.GridPosition(self.pos.x1, y1)
                empty_pos = pos.GridPosition(self.pos.x1, self.pos.y2)
                if Grid.isPositionEmpty(check_pos):
                    return True
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
                    return True
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
                    return True
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
                    return True
                else:
                    return False
