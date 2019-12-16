# ShortestTTR
Python script for getting shortest path connecting all given goals in the board game "Ticket to ride".


# Usage
Playing on the Europe map and having the goals Sochi, Edinburgh, Stockholm, and Cadiz:
>./ShortestTTR.py Europe Sochi Edinburgh Stockholm Cadiz

This will print the path, cost and visualize the path.
> path: ['Cadiz', 'Madrid', 'Pamplona', 'Paris', 'Dieppe', 'London', 'Edinburgh', 'London', 'Amsterdam', 'Essen', 'Kobenhavn', 'Stockholm', 'Petrograd', 'Moskva', 'Kharkov', 'Rostov', 'Sochi']\
>cost: 52

![](https://i.imgur.com/ZBQotv4.gif "Output image")

# Libraries used
* NetworkX
* Matplotlib
* OpenCV
* PyDot

# TODO
1. Improve own Dijkstra algorithm.
2. Add more maps.
3. Add colors according to original TTR map.
4. Fix Cul-de-sac's. In the usage section the shortest path visits London twice.

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

# Ticket to ride
> https://en.wikipedia.org/wiki/Ticket_to_Ride_(board_game)
