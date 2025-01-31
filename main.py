from wormHead import *
from random import randint

gridX, gridY = 13,13

grid = [[0]*gridX for i in range(gridY)]

def place_apple():
    appleX = randint(0,len(grid) - 1)
    appleY = randint(0,len(grid) - 1)

    while grid[appleX][appleY] != 0:
        appleX = randint(0,len(grid) - 1)
        appleY = randint(0,len(grid[0]) - 1)

    return [appleX, appleY]

