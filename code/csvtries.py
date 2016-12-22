"""
Csvtries.py: imports csv dataset for a game
and sets up grid with vehicles
"""
import csv
import grid as g
import car
import truck


def run(dataset, width, height, exit):
    """
    Runs csvtries for the specified dataset,
    with given width, height and exit position
    """
    grid = g.Grid(width, height, exit)
    f = dataset

    try:
        # open reading and skip first line
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            if row[0] == "car" or row[0] == "redcar":
                # get the coordinates
                x = row[1].split(", ")
                y = row[2].split(", ")
                # create new vehicle
                new_car = car.Car(x[0], x[1], y[0], y[1], row[3], row[4])
                grid.vehicles.append(new_car)
            elif row[0] == "truck":
                # get the coordinates
                x = row[1].split(", ")
                y = row[2].split(", ")
                # create new vehicle
                new_truck = truck.Truck(x[0], x[1], x[2], y[0], y[1], y[2], row[3], row[4])
                grid.vehicles.append(new_truck)

    finally:
        f.close()
        grid.removeEmptyGrid()
        return grid
