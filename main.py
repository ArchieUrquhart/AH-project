from wormHead import *
from GUI import *
from highscoretable import *

from random import randint

#initialise the board height and width
gridWidth  = 13
gridHeight = 13


def place_apple():
    #pick random X,Y coordinate
    appleX = randint(0,gridWidth - 1)
    appleY = randint(0,gridHeight - 1)

    #keep cahnging chosen position until a valid spae is chosen
    while grid[appleX][appleY] != 0:
        appleX = randint(0, gridWidth - 1)
        appleY = randint(0, gridHeight - 1)

    return [appleX, appleY]



def display_grid(head, appleX, appleY):
#set grid to all 0s
    grid = [[0]*gridWidth for i in range(gridHeight)]
    
#account for the position of the head of the worm
    segment = head
    x = segment.getPos()[0]
    y = segment.getPos()[1]

    grid[x][y] = 1

    #loop through entire worm to set the squares in the grid to the correct value
    while segment.nextNode() is not None:
        x = segment.getPos()[0]
        y = segment.getPos()[1]

        grid[x][y] = 1

        segment = segment.nextNode()

    #add the identifier for the apple position
    grid[appleX][appleY] = 2

    #map of colours for each square type
    colour_map = {
        0: (0,0,0),
        1: (240,100,200),
        2: (80,230,120)
    }

    #loop for each square in the grid
    for x in range(0, gridWidth-1):
        for y in range(0, gridHeight-1):
            #get colour at square
            square_colour = colour_map[grid[x][y]]
            #draw square to grid in the correct position
            draw_square(x,y, 50, square_colour)

    #WRITE SCORE TO SCREEN



    

def gameLoop():
    #get key inputs 

    #move player 

    #check colisions

    #draw grid    



def main():
    #initialise the grid 
    grid = [[0]*gridWidth for i in range(gridHeight)]
    
    # initialsie the player
    head = Node(round(gridWidth /2) , round(gridHeight /2)
    head.append()
    head.nextNode.setPos(gridWidth //2, gridHeight //2 + 1)

            
