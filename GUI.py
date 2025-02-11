import re
import pygame

def valid_name(username):
	if len(username) > 20 or re.search(["^\w"]):
		return False
	else:
		return True

def get_name():
	pass


def draw_square(x, y, square_size, colour):
    #positions are changed to account size of each square and the score
    x_pos = x*square_size
    y_pos = y*square_size + 100
    pg.draw.rect(window, colour, (x_pos, y_pos, square_size, square_size))


