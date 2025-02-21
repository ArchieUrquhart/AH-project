from wormHead import *
from UI import *
from highscoretable import *

from random import randint
import pygame as pg

# initialise window settings
width, height = 660, 760
window = pg.display.set_mode((width, height))
pg.display.set_caption("Worm")
clock = pg.time.Clock()
pg.font.init()

# initialise width and height of grid
gridWidth, gridHeight = 11, 11

#draw square procedure for readability
def draw_square(x, y, square_size, colour):
    #positions multiplied by size to scale up locations from array indexes to pixels on screen
    x_pos = x * square_size
    #positions moved down to make room for score
    y_pos = y * square_size + 100

    #draw square to screen at calculated position and chosen colour
    pg.draw.rect(window, colour, (x_pos, y_pos, square_size, square_size))


# function to place apple in valid square
def place_apple(grid):
    # pick random X,Y coordinate
    appleX = randint(0, gridWidth - 1)
    appleY = randint(0, gridHeight - 1)

    # keep changing chosen position until a valid space is chosen
    while grid[appleX][appleY] != 0:
        appleX = randint(0, gridWidth - 1)
        appleY = randint(0, gridHeight - 1)

    return appleX, appleY


# draws grid and score to window
def update_grid(head, appleX, appleY):
    # set grid to all 0s
    grid = [[0] * gridWidth for i in range(gridHeight)]


    #identify all squares with worm
    #loop through worm
    segment = head
    while segment is not None:
        #get current x y position
        x = segment.getPos()[0]
        y = segment.getPos()[1]

        #set 2d array at current position to 1
        grid[x][y] = 1

        #go to next segement in list
        segment = segment.nextNode()

    # add apple to grid
    grid[appleX][appleY] = 2

    return grid


def draw_grid(grid, score):
    # map of colours for each square type
    colour_map = {
        0: (20, 20, 30),
        1: (240, 100, 200),
        2: (80, 230, 120)
    }

    # loop for each square in grid
    for x in range(0, gridWidth):
        for y in range(0, gridHeight):
            # get colour at square
            square_colour = colour_map[grid[x][y]]

            # draw square to grid at correct position and colour
            draw_square(x, y, 60, square_colour)

    # writes player's score to window
    font = pg.font.Font(None, 150)
    text = font.render("{}".format(score), True, (255, 255, 255))
    window.blit(text, (0, 0))


# detects if worm head is on square with apple
def detect_eat(head,appleX,appleY):
    targNode = head
    #check if head position = apple position
    if head.getPos()[0] == appleX and head.getPos()[1] == appleY:
        #find last node in list
        while targNode.nextNode() is not None:
            targNode = targNode.nextNode()
        #add a new node to end of list
        targNode.append()

        return True

    return False



def check_loss(head):
    targNode = head.nextNode()

    #get position of head
    headX = head.getPos()[0]
    headY = head.getPos()[1]

    #check if head is out of bounds of grid
    if headX< 0 or headX>= gridWidth or headY<0 or headY>=gridHeight:
        return True
    else:
        #loop through whole worm
        while targNode.nextNode() is not None:
            targNode = targNode.nextNode()
            #check if segment intersects with head
            if targNode.getPos()[0] == headX and targNode.getPos()[1] == headY:
                return True

    return False


def game_loop():
    # initialsie player
    head = Node(gridWidth // 2, gridHeight // 2)
    head.append()
    head.nextNode().setPos(gridWidth // 2, gridHeight // 2 + 1)
    head.nextNode().append()
    direction = 'up'

    # initialise player's score
    score = 0

    #get player's username
    username = get_username()

    # initialise grid with placeholder apple position
    grid = [[0] * gridWidth for i in range(gridHeight)]
    grid = update_grid(head, 0, 0)
    appleX, appleY = place_apple(grid)

    #run game until value is returned
    lost = False
    while not lost:
        window.fill((0, 0, 0))

        #get inputs
        for event in pg.event.get():
            # lose game if quit
            if event.type == pg.QUIT:
                return username, score

            #get arrow key input
            if event.type == pg.KEYDOWN:
                # check that when a key is pressed it doesnt apose current direction
                if event.key == pg.K_LEFT and direction != 'right':
                    direction = 'left'
                elif event.key == pg.K_RIGHT and direction != 'left':
                    direction = 'right'
                elif event.key == pg.K_UP and direction != 'down':
                    direction = 'up'
                elif event.key == pg.K_DOWN and direction != 'up':
                    direction = 'down'

        #get current position of head
        headx, heady = head.getPos()[0], head.getPos()[1]

        #move all nodes except head forward
        move_player(head)
        
        #move head node depending on cuurent direction
        if direction == 'left':
            head.setPos(headx - 1, heady)
        elif direction == 'right':
            head.setPos(headx + 1, heady)
        elif direction == 'up':
            head.setPos(headx, heady - 1)
        else:
            head.setPos(headx, heady + 1)

        #check if player has eaten an apple
        if detect_eat(head, appleX, appleY):
            #replace apple
            appleX, appleY = place_apple(grid)
            #increase players score
            score = score + 100

        #check if player has lost game
        if check_loss(head):
            return username, score

        #update squares on grid 
        grid = update_grid(head, appleX, appleY)

        #draw grid to screen
        draw_grid(grid, score)
        pg.display.update()
        clock.tick(5)



closed = False
while not closed:
    print(game_loop())
    closed = True
