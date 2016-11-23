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
        for i in range(0, len(Grid.all_vehicles)):
            if Grid.all_vehicles[i] == old_pos:
                Grid.all_vehicles[i] = new_pos
        self.pos = new_pos

    def moveTruck(self, position, direction):
        """
        Moves truck to new position
        """
        old_pos = self.getCarPosition()
        
        if direction == 'right' or direction == 'down':
            # move vertical car down
            if self.orientation == 'V':
                
                y1 = self.pos.y1 + 1
                y2 = self.pos.y2 + 1
                y3 = self.pos.y3 + 1
                new_pos = CarPosition(self.pos.x1, self.pos.x2, self.pos.x3, y1, y2, y3)
                check_pos = GridPosition(self.pos.x1, y3)
                empty_pos = GridPosition(self.pos.x1, self.pos.y1)
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
                check_pos = GridPosition(x3, self.pos.y1)
                empty_pos = GridPosition(self.pos.x1, self.pos.y1)
                if Grid.isPositionEmpty(check_pos):
                    Grid.updateEmptyPosition(check_pos, empty_pos)
                    self.setCarPosition(old_pos, new_pos)
                else:
                    print("dit kan dus niet he")
                    
        elif direction == 'left' or direction == 'up':
            # move vertical car up
            if self.orientation == 'V':
                y1 = self.pos.y1 - 1
                y2 = self.pos.y2 - 1
                y3 = self.pos.y3 - 1
                new_pos = CarPosition(self.pos.x1, self.pos.x2, self.pos.x3, y1, y2, y3)
                self.setCarPosition(new_pos)
                check_pos = GridPosition(self.pos.x1, y1)
                empty_pos = GridPosition(self.pos.x3, self.pos.y3)
                if Grid.isPositionEmpty(check_pos):
                    Grid.updateEmptyPosition(check_pos, empty_pos)
                    self.setCarPosition(old_pos, new_pos)
                else:
                    print("dit kan dus niet he")
                    
            # move horizontal car left
            else:
                x2 = self.pos.x2 - 1
                x1 = self.pos.x1 - 1
                x3 = self.pos.x3 - 1
                new_pos = CarPosition(x1, x2, x3, self.pos.y1, self.pos.y2, self.pos.y3)
                self.setCarPosition(new_pos)
                check_pos = GridPosition(x1, self.pos.y1)
                empty_pos = GridPosition(self.pos.x3, self.pos.y3)
                if Grid.isPositionEmpty(check_pos):
                    Grid.updateEmptyPosition(check_pos, empty_pos)
                    self.setCarPosition(old_pos, new_pos)
                else:
                    print("dit kan dus niet he")

        # TODO: update position in all_vehicles?
