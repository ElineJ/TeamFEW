import csv     # imports the csv module
import sys      # imports the sys module

car_list = []

class Car(object):
    """
    Creates an object for a vehicle type of car
    """
    def __init__(self, orientation, color):

        self.orientation = orientation
        self.color = color


f = open(sys.argv[1], 'rb') # opens the csv file
try:
    reader = csv.reader(f)  # creates the reader object
    for row in reader:   # iterates the rows of the file in orders
        car_list.append(Car(row[3], row[4]))    # puts values in list
finally:
    f.close()      # closing

print [Car.color for Car in car_list]

# Code for the game rush hour
#
# Sets up vehicles (trucks and cars) and a grid for the game
