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
	
    segment = head

	
#loops through the entire worm and sets the elements in the grid to 1 where a segment is there
    while segment.nextNode() not None:
	    x = segment.getPos()[0]
	    y = segment.getPos()[1]
	
	    grid[x][y] = 1

	    segment = segment.nextNode()

    #set the gid at the position of the apple to 2
    grid[appleX][appleY] = 2

	#list of colours for each square type
	colour_dict = {
		0: (0,0,0);
		1: (240,100,200);
		2: (80,230,120)
	}

    for i in range(0, gridWidth-1):
    	for j in range(0, gridHeight-1):
    		colour = colour_dict[gid[i][j]]
		#CALCULATE WORLD POSITION
    		#DRAW SQUARE TO SCREEN
            
    
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

            
