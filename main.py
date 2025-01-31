from wormHead import *
from random import randint

#initialise the board with a height and width
gridWidth, gridHeight = 13,13
grid = [[0]*gridWidth for i in range(gridHeight)]

def place_apple():
    #pick random X,Y coordinate
    appleX = randint(0,len(grid) - 1)
    appleY = randint(0,len(grid) - 1)

    #keep cahnging chosen position until a valid spae is chosen
    while grid[appleX][appleY] != 0:
        appleX = randint(0,gridWidth - 1)
        appleY = randint(0,gridHeight - 1)

    return [appleX, appleY]

