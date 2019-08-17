# ShortestTTR
Python script for getting shortest path connecting all given goals in the board game "Ticket to ride".

# Libraries used
* NetworkX
* Matplotlib
* OpenCV
* PyDot

# Usage
Playing on the Europe map and having the goals Sochi, Edinburgh, Stockholm, and Cadiz:
>./ShortestTTR.py Europe Sochi Edinburgh Stockholm Cadiz

This will print the path, cost and visualize the path.
> path: ['Cadiz', 'Madrid', 'Pamplona', 'Paris', 'Dieppe', 'London', 'Edinburgh', 'London', 'Amsterdam', 'Essen', 'Kobenhavn', 'Stockholm', 'Petrograd', 'Moskva', 'Kharkov', 'Rostov', 'Sochi']\
>cost: 52


![](https://i.imgur.com/rdre8bG.jpg "Output image")

# TODO
1. Make own Dijkstra algorithm.
2. Add more maps.
3. Add colors according to original TTR map.
4. Export script to either an app or webpage.

# Scripts
There are some unecessary scripts in this repository, they are mostly for my own sake.
If you want to use this you only need ShortestTTR, se usage above.

* ShortestTTR\
    Main script, use this.

* Board\
    Class that contains all the boards.

* Dijkstra\
    Contains the dijkstra algorithm.\
    This is used as an alternativ to the NetworkX dijkstra.

* Mapper\
    Script which makes it easier to get the graph and positions.

* Libraries\
    Script that installs all the necessary libraries.\
    If there are any dependencies i missed let me know and i will add them.

# Ticket to ride
> https://en.wikipedia.org/wiki/Ticket_to_Ride_(board_game)
