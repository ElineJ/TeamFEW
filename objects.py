# Cars and grid

class carType:
    def _init_(self,name):
        self.name = name
        if name == "RedCar":
            self.size = 2
        elif name == "Truck":
            self.size = 3

class grid:
    cars = []
    width = widthgrid
    height = heightgrid
