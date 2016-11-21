import positions
import grid

class Truck(object):
    """
    Creates an object for a vehicle type of truck
    """
    def __init__(self, x1, x2, x3, y1, y2, y3, orientation, color):
        position = TruckPosition(x1, x2, x3, y1, y2, y3)
        self.pos = position
        self.orientation = orientation
        self.color = color

    def getTruckPosition(self):
        """
        Returns the current position of vehicle
        """
        return self.pos

    def setTruckPosition(self, position):
        """
        Set the position of the car to position

        position: a Position object.
        """
        self.pos = position

    def moveTruck(self, position, direction):
        """
        Moves truck to new position
        """
        if direction == 'right' or direction == 'down':
            # move vertical car down
            if self.orientation == 'V':
                y1 = self.pos.y1 + 1
                y2 = self.pos.y2 + 1
                y3 = self.pos.y3 + 1
                new_pos = CarPosition(self.pos.x1, self.pos.x2, self.pos.x3, y1, y2, y3)
                self.setCarPosition(new_pos)
                check_pos = GridPosition(x1, self.pos.y1)
                empty_pos = GridPosition(self.pos.x2, self.pos.y2)
                if Grid.isPositionEmpty(check_pos):
                    Grid.updateEmptyPosition(check_pos, empty_pos)
                    self.setCarPosition(old_pos, new_pos)
                else:
                    print("dit kan dus niet he")
            # move horizontal car right
            else:
                x1 = self.pos.x1 + 1
                x2 = self.pos.x2 + 1
                x3 = self.pos.x3 + 1
                new_pos = CarPosition(x1, x2, x3, self.pos.y1, self.pos.y2, self.pos.y3)
                self.setCarPosition(new_pos)

        elif direction == 'left' or direction == 'up':
            # move vertical car up
            if self.orientation == 'V':
                y1 = self.pos.y1 - 1
                y2 = self.pos.y2 - 1
                y3 = self.pos.y3 - 1
                new_pos = CarPosition(self.pos.x1, self.pos.x2, self.pos.x3, y1, y2, y3)
                self.setCarPosition(new_pos)
            # move horizontal car left
            else:
                x2 = self.pos.x2 - 1
                x1 = self.pos.x1 - 1
                x3 = self.pos.x3 - 1
                new_pos = CarPosition(x1, x2, x3, self.pos.y1, self.pos.y2, self.pos.y3)
                self.setCarPosition(new_pos)

        # TODO: update position in all_vehicles?
