# Cars and grid
import numpy as np
class Position(obhject):
    

class VeGrid(object):

    def __init__(self, width, height, exit):
        self.width = width
        self.height = height
        self.exit = exit
        grid = []
        self.grid = grid
        
    def isRedOnExit(self, pos):
        if pos == self.exit:
            return True
        return False
    def isPositioninGrid(self, pos)
        if 0 > vehicle.x1 <= self.width and 0 > vehicle.x2 <= self.width and 0 > vehicle.y1 < self.height and 0 > vehicle.y1 < self.height:
            return True
        return False


class Vehicle:
    
    def __init__(self, x1, x2, y1, y2):
        
        # kan eigenlijk niet hier omdat trucks 3 lang zijn
        self.pos = position
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        
    def getVehiclePosition(self):
        
        return self.pos
    
    def setVehiclePosition(self, x1, x2, y1, y2):
        
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        # niet erg mooi
        
class Hcar(Vehicle):
    def __init__(self):
 
    def movement(self):
        
