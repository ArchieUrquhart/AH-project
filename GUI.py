import re
import pygame

def valid_name(username):
	if len(username) > 20 or re.search(["^\w"]):
		return False
	else:
		return True

def get_name():
	pass


class Window:
	def __init__(width, height, name):
		self.window = pygame.display.set_mode((width, height))
		pygame.display.set_caption(name)
	
	def draw_square(x_pos, y_pos,colour):
		pygame.draw.rect(self.window, (x_pos,y_pos, self.square_size, self.square_size), colour)
	
	def write_score(score):
		font = pg.font.Font(64)
		text = font.render("{}".format(score), True, (255, 255, 255))
		self.window.blit(text, (0,0))
	
	def refresh():
		pass
	
	def display_table(highscores):
		font = pg.font.Font(64)
		text = font.render("Highscores".format(score), True, (255, 255, 255))
		self.window.blit(text, (0,0))

  
  
