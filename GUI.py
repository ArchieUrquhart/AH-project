import re

def valid_name(username):
  if len(username) > 20 or re.search([^\w]):
    return False
  else:
    return True


class Window:
  def __init__(width, height, name, bg_colour):
    self.window = pygame.display.set_mode((width, height))
    pygame.display.set_caption(name)
    self.bg_colour = bg_colour
    
  def draw_square(x_pos, y_pos):
    pass

  def write_score(score):
    pass

  def refresh():
    pass

  def display_table(highscores):
    pass

  
  
