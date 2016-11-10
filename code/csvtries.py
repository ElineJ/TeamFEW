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
    # skip first line of csv file
    next(reader)
    for row in reader:   # iterates the rows of the file in orders
        # get string of x coordinates
        str = row[1]
        # split this string
        list = str.split(", ")
        # save values from list
        x1 = list[0]
        x2 = list[1]
        # print "coordinates are x1 = " + x1 + x2

        # add car with the values from csv file to the list of cars
        car_list.append(Car(row[3], row[4]))    # puts values in list
finally:
    f.close()      # closing

print [Car.color for Car in car_list]
