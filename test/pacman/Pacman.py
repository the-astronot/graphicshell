"""
@author: jormungandr1105
@desc: Quick test of Game Engine/Graphics libraries
@created: 06/26/2022
"""
from json import load
import sys
import time

sys.path.insert(0, '../../graphicshell')
sys.path.insert(0, '../../graphicshell/GameEngine')

from GameEngine import *
from Object import *


class Pacman:
	def __init__(self):
		self.game_engine = GameEngine((50,17))
		# Setup Walls
		ch,c = load_object("bigger_walls.objf")
		walls = Object(ch,c)
		self.game_engine.add_object(walls,0)
		# Add Pacman
		ch,c = load_object("pacman.objf")
		pacman = Object(ch,c)
		pacman.set_loc((1,1))
		self.player = pacman
		self.game_engine.add_object(pacman,1)
		# Add Ghosts
		self.ghosts = {}
		ch,c = load_object("pinky.objf")
		pinky = Object(ch,c)
		pinky.set_loc((10,8))
		self.ghosts["pinky"] = pinky
		self.game_engine.add_object(pinky,2)
		self.game_engine.push_frame()
		time.sleep(10)
		self.game_engine.terminal.cleanup()

# Testing
if __name__ == '__main__':
	class_test = Pacman()
