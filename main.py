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

# initialise the width and height for the game grid
gridWidth, gridHeight = 11, 11





# draw the game grid - FR 1.5
def draw_table(HighScores):
    #fill background colour
    window.fill((0,0,0))

    # write 'LEADERBOARD' to the screen
    font = pg.font.Font(None, 100)
    header = font.render("LEADERBOARD", True,(255,255,255))
    window.blit(header,(70,30))

    # write field headings to screen
    font = pg.font.Font(None, 50)
    USERNAME = font.render("Username", True, (200, 40, 100))
    HIGHSCORE = font.render("Highscore", True, (90, 150, 240))
    GAMESPLAYED = font.render("Games", True, (230, 220, 70))

    window.blit(USERNAME, (30, 150))
    window.blit(HIGHSCORE, (280, 150))
    window.blit(GAMESPLAYED, (500, 150))


    size = 40
    font = pg.font.Font(None, size)


    # start from best player
    counter =0
    # display top 10 players or the number of players if fewer than 10 players have played
    while counter < 10 and counter < len(HighScores):
        # display the current players username score and played games to screen
        username = font.render("{}".format(HighScores[counter][0]), True, (200, 40, 100))
        highscore = font.render("{}".format(HighScores[counter][1]), True, (90, 150, 240))
        games = font.render("{}".format(HighScores[counter][2]), True, (230, 220, 70))

        window.blit(username, (30, counter * size +200))
        window.blit(highscore, (330, counter * size +200))
        window.blit(games, (550, counter * size +200))

        # move to next best player
        counter += 1

    # write 'press any key to start' prompt at bottom of screen
    prompt = font.render("press any key to start", True, (70, 70, 70))
    window.blit(prompt, (180,650))

    pg.display.update()







# function to place apple in valid square - FR 5.2
def place_apple(grid):
    # pick random X,Y coordinate
    appleX = randint(0, gridWidth - 1)
    appleY = randint(0, gridHeight - 1)

    # keep changing chosen position until a valid space is chosen
    while grid[appleX][appleY] != 0:
        appleX = randint(0, gridWidth - 1)
        appleY = randint(0, gridHeight - 1)

    #return validated x y position of apple
    return appleX, appleY






# updates the values of the game grid - FR 3.4 , FR 5.3
def update_grid(head, appleX, appleY):
    # set grid to all 0s
    grid = [[0] * gridWidth for i in range(gridHeight)]

    # loop through entire worm and update the grid for each segment - FR 3.4
    segment = head
    while segment is not None:
        # get the current x y position
        x = segment.getPos()[0]
        y = segment.getPos()[1]

        # set the element in the 2d array at that x y position to 1
        grid[x][y] = 1

        # go to the next segement in the list
        segment = segment.nextNode()

    # add the apple to the grid - FR 5.3
    grid[appleX][appleY] = 2

    return grid





#draw the game grid and players score - FR 3.5
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
            # get the colour of square
            square_colour = colour_map[grid[x][y]]
            square_size = 60

            # positions are multiplied by size to scale up the locations from array indexes to pixels on the screen
            x_pos = x * square_size
            # positions are moved down to make room for the score
            y_pos = y * square_size + 100

            # draw square to screen at calculated position and chosen colour
            pg.draw.rect(window, square_colour, (x_pos, y_pos, square_size, square_size))

    # writes players score to the topleft of window
    font = pg.font.Font(None, 150)
    text = font.render("{}".format(score), True, (255, 255, 255))
    window.blit(text, (0, 0))







def game_loop():
    # initialise the players score
    score = 0

    # get the players username
    username = get_username()
    if username != '':
        # initialsie the player
        head = Node(gridWidth // 2, gridHeight // 2)
        head.append()
        head.nextNode().setPos(gridWidth // 2, gridHeight // 2 + 1)
        direction = 'up'

        # initialise the grid and apple position
        grid = [[0] * gridWidth for i in range(gridHeight)]
        grid = update_grid(head, 0, 0)
        appleX, appleY = place_apple(grid)

        # run game until player loses or quits
        lost = False
        while not lost:
            window.fill((0, 0, 0))

            # get inputs
            for event in pg.event.get():
                # end game if player quit - FR 6.3
                if event.type == pg.QUIT:
                    return username, score

                # get arrow key input - FR 3.1 
                if event.type == pg.KEYDOWN:
                    # check that when a key is pressed it doesn't oppose current direction
                    if event.key == pg.K_LEFT and direction != 'right':
                        direction = 'left'
                    elif event.key == pg.K_RIGHT and direction != 'left':
                        direction = 'right'
                    elif event.key == pg.K_UP and direction != 'down':
                        direction = 'up'
                    elif event.key == pg.K_DOWN and direction != 'up':
                        direction = 'down'

            # get current position of worm head
            headx, heady = head.getPos()[0], head.getPos()[1]

            # move all nodes except the head forward - FR 3.3
            move_player(head)

            # move head node depending on the current direction - FR 3.3
            if direction == 'left':
                head.setPos(headx - 1, heady)
            elif direction == 'right':
                head.setPos(headx + 1, heady)
            elif direction == 'up':
                head.setPos(headx, heady - 1)
            else:
                head.setPos(headx, heady + 1)

            # check if player has eaten an apple - FR 4.1, FR 5.1
            if detect_eat(head, appleX, appleY):
                # replace apple - FR 5.2
                appleX, appleY = place_apple(grid)
                # increase players score - 4.2
                score = score + 100

            # check if player has lost the game - FR 6.1, FR 6.2
            if check_loss(head,grid):
                return username, score

            # update the values on the grid - FR 3.4, FR 5.3
            grid = update_grid(head, appleX, appleY)

            # draw the grid to the screen
            draw_grid(grid, score)
            pg.display.update()
            clock.tick(5)

    return username, score


#reoeat until game closed
closed = False
while not closed:
    #get table from database and draw it - FR 1.1 -> 1.5
    table = get_table()
    draw_table(table)
    
    keypressed = False
    while not keypressed:
        for event in pg.event.get():
            # end game if quit - FR 1.6
            if event.type == pg.QUIT:
                closed = True
                keypressed=True
                pg.quit()
            # end loop is key pressed
            if event.type == pg.KEYDOWN:
                keypressed = True

    if not closed:
        # get the game details by starting a new game
        username, score = game_loop()

        # check if username was not null
        if username != '':
            # insert game details into table - Fr 2.3
            add_game(username, score)
        else:
            # if no username was entered 
            closed = True
