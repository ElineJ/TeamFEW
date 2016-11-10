import csv

with open('game3.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
         print row
