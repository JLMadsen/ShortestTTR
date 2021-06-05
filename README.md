# ShortestTTR
Python script for getting shortest path connecting all given goals in the board game "Ticket to ride".


# Usage
Format:
>./ShortestTTR.py map goal1 goal2 goal3 goal4

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

# Ticket to ride
> https://en.wikipedia.org/wiki/Ticket_to_Ride_(board_game)
