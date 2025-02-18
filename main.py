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


#draw square procedure for readability
def draw_square(x, y, square_size, colour):
    #positions are multiplied by size to scale up the locations from array indexes to pixels on the screen
    x_pos = x * square_size
    #positions are moved down to make room for the score
    y_pos = y * square_size + 100

    #draw square to screen at calculated position
    pg.draw.rect(window, colour, (x_pos, y_pos, square_size, square_size))


# initialise the game grid with a height and width
gridWidth, gridHeight = 11, 11


# function to place apple in valid square
def place_apple(grid):
    # pick random X,Y coordinate
    appleX = randint(0, gridWidth - 1)
    appleY = randint(0, gridHeight - 1)

    # keep cahnging chosen position until a valid spae is chosen
    while grid[appleX][appleY] != 0:
        appleX = randint(0, gridWidth - 1)
        appleY = randint(0, gridHeight - 1)

    return appleX, appleY


# draws the game grid and score to the window
def update_grid(head, appleX, appleY):
    # set grid to all 0s
    grid = [[0] * gridWidth for i in range(gridHeight)]

    # account for the position of the head of the worm
    segment = head
    x = segment.getPos()[0]
    y = segment.getPos()[1]

    grid[x][y] = 1

    # loop through entire worm and identify all the segment position in the grid where a segment is present
    segment = segment.nextNode()
    while segment is not None:
        x = segment.getPos()[0]
        y = segment.getPos()[1]

        grid[x][y] = 1

        segment = segment.nextNode()

    # add the apple to the grid
    grid[appleX][appleY] = 2

    return grid


def draw_grid(grid, score):
    # map of colours for each square type
    colour_map = {
        0: (20, 20, 30),
        1: (240, 100, 200),
        2: (80, 230, 120)
    }

    # loop for each square in the grid
    for x in range(0, gridWidth):
        for y in range(0, gridHeight):
            # get colour at square
            square_colour = colour_map[grid[x][y]]

            # draw square to grid in the correct position
            draw_square(x, y, 60, square_colour)

    # writes players score to the window

    font = pg.font.Font(None, 150)
    text = font.render("{}".format(score), True, (255, 255, 255))
    window.blit(text, (0, 0))



def detect_eat(head,appleX,appleY):
    targNode = head
    if targNode.getPos()[0] == appleX and targNode.getPos()[1] == appleY:
        while targNode.nextNode() is not None:
            targNode = targNode.nextNode()

        targNode.append()

        return True

    return False



def check_loss(head):
    targNode = head.nextNode()
    headX = head.getPos()[0]
    headY = head.getPos()[1]

    if headX< 0 or headX>= gridWidth or headY<0 or headY>=gridHeight:
        return True
    else:
        while targNode.nextNode() is not None:
            targNode = targNode.nextNode()
            if targNode.getPos()[0] == headX and targNode.getPos()[1] == headY:
                return True

    return False


def game_loop():
    # initialsie the player
    head = Node(gridWidth // 2, gridHeight // 2)
    head.append()
    head.nextNode().setPos(gridWidth // 2, gridHeight // 2 + 1)
    head.nextNode().append()
    direction = 'up'

    # initialise the players score
    score = 0

    username = ""

    # initialise the grid
    grid = [[0] * gridWidth for i in range(gridHeight)]
    grid = update_grid(head, 0, 0)
    appleX, appleY = place_apple(grid)

    lost = False

    while not lost:
        window.fill((0, 0, 0))

        # if check_loss(head):

        for event in pg.event.get():
            # close window
            if event.type == pg.QUIT:
                return username, score

            if event.type == pg.KEYDOWN:
                # key inputs for direction
                if event.key == pg.K_LEFT and direction != 'right':
                    direction = 'left'
                elif event.key == pg.K_RIGHT and direction != 'left':
                    direction = 'right'
                elif event.key == pg.K_UP and direction != 'down':
                    direction = 'up'
                elif event.key == pg.K_DOWN and direction != 'up':
                    direction = 'down'

        headx, heady = head.getPos()[0], head.getPos()[1]

        move_player(head)

        if direction == 'left':
            head.setPos(headx - 1, heady)
        elif direction == 'right':
            head.setPos(headx + 1, heady)
        elif direction == 'up':
            head.setPos(headx, heady - 1)
        else:
            head.setPos(headx, heady + 1)

        if detect_eat(head, appleX, appleY):
            appleX, appleY = place_apple(grid)
            score = score + 100

        if check_loss(head):
            return username, score

        grid = update_grid(head, appleX, appleY)

        draw_grid(grid, score)
        pg.display.update()
        clock.tick(5)



print(game_loop())
