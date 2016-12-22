# Rush Hour
A solver and visualization of the game Rush Hour for the Heuristieken course. 

## Usage

In `main` the program will run the `random` and `breadth first search` algorithm. You can run the program in the terminal with the following command: 

```
python main.py 1
```

The number represents one of the seven boards the algoritm can solve. In order to have the algorithm solve one of the other seven boards, enter a different number between 1 - 7. 

-----

In `visualdata` the program will run a visualisation of the boards 1 - 4, which have already been solved by a breadth-first search algorithm. You can run the program in the terminal with the following command: 

```
python visualdata.py 1
```

The number represents one of the four boards the algoritm can solve with the breadth-first search algorithm. In order to see the visualisation for one of the other four boards, enter a different number between 1 - 4.  

### Prerequisites

The code is written in `Python 2.7`. Running it in Python 3 might cause problems. Running the program requires installation of `Matplotlib`. If this is not yet installed on your computer, you can find installation instructions for your operating system [here](http://matplotlib.org/users/installing.html).


## Methods

## Files ##

File          | Description
------------- | -------------
main          | Main file to run the program
bfs           | A breadth-first search algorithm 
rndm          | A random algorithm
rndm_2        | A second random algorithm
combo         | A combination algorithm of random and breadth-first search
positions     | Position classes for Grid, Car and Truck
grid          | Implementation of the grid of the game
car           | Car 
truck         | Truck
visualize     | Visualization of the game
csvtries      | File to import the game data from csv and set-up board
visualdata    | File to visualize breadth-first search solution of games 1 - 4


## Authors

* Wietske Dotinga - [WWWietske](https://github.com/WWWietske)
* Fjodor van Rijsselberg - [fjodor-rs](https://github.com/fjodor-rs)
* Eline Jacobse - [ElineJ](https://github.com/ElineJ)

