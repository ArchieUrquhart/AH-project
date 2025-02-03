from wormHead import *
from random import randint

#initialise the board height and width
gridWidth  = 13
gridHeight = 13



def place_apple():
    #pick random X,Y coordinate
    appleX = randint(0,len(grid) - 1)
    appleY = randint(0,len(grid[0]) - 1)

    #keep cahnging chosen position until a valid spae is chosen
    while grid[appleX][appleY] != 0:
        appleX = randint(0, gridWidth - 1)
        appleY = randint(0, gridHeight - 1)

    return [appleX, appleY]


def display_grid(head, appleX, appleY):
    pass
    

def gameLoop():
    #initialise the grid 
    grid = [[0]*gridWidth for i in range(gridHeight)]
    
    # initialsie the player
    head = Node(round(gridWidth /2) , round(gridHeight /2)
    head.append()
    head.nextNode.setPos(gridWidth //2, gridHeight //2 + 1)

    #get key inputs 

    #move player 

    #check colisions

    #draw grid    

def main():
    pass

            
