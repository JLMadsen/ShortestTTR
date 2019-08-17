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

![](https://i.imgur.com/rdre8bG.jpg "Output image")

# TODO
1. Make own Dijkstra algorithm.
2. Add more maps.
3. Add colors according to original TTR map.
4. Export script to either an app or webpage.

# Ticket to ride
> https://en.wikipedia.org/wiki/Ticket_to_Ride_(board_game)
