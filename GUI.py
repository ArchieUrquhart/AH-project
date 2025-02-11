import re
import pygame

def valid_name(username):
	if len(username) > 20 or re.search(["^\w"]):
		return False
	else:
		return True

def get_name():
	pass


