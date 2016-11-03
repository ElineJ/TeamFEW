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

# ondergrens = minimaal aantal stappen om eruit te komen
# bovengrens = maximaal aantal stappen om eruit te komen

# kijken wat rode auto blokkeert --> die moet je verplaatsen
# kan je die niet verplaatsen --> verplaats wat die auto blokkeert, etc

# boom strategie met alle oplossingen zoeken

# bovengrens en ondergrens kijken naar het aantal mogelijke borden

# ondergrens is bijvoorbeeld het aantal auto's dat in de weg staan

# bij blokkeer strategie kijken naar terugkerende bewegingen voor rode auto

# eindpresentatie: WAAROM? is dit nuttig? Waarom wil je dit oplossen?
