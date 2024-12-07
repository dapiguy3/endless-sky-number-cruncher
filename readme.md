This is the endless sky number cruncher, written by Devlyn Coulter to better min-max builds in the game.
The code is all python on the surface, but there are some shell script interactions(DOS or BASH depending on OS) under the hood to handle file management.
I've written the code to be(hopefully) future-proof and will even be adding plugin support.

The code should be incredibly simple, so i'll be making this project capable of being run either as a standalone script or imported as a library.



what this project will probably do:

1: script scans file structure of game and loads all relevant data 
    a: script scans file structure with os library(yes i know this is unsafe. i dont care, you're a big kid now), noting file paths of all text files
    b: script filters out irrelevant files(e.g. missions, sales, and trading data)
    c: script opens relevant files and loads data into data structures(i'm predicting dictionaries but i havent decided yet)

2: the script allows you to manipulate the data.
functions:
    select, filter, and sort by attribute, category, and origin of outfit/ship
    create a build tester that allows on-paper testing of capacities and damage output
    create a "shopping cart" that allows players to(somewhat) efficiently acquire an ecclectic build without clicking through the map for 10 minutes.

wish list
    goal-seeking function to optimize dps, mobility for power, and vs a specific ship type


what this project MIGHT do if i'm not a lazy PoS
put it all in a gui like https://coriolis.io did for Elite:Dangerous
