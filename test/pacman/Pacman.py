"""
@author: jormungandr1105
@desc: Quick test of Game Engine/Graphics libraries
@created: 06/26/2022
"""
import sys
import time

sys.path.insert(0, '../../graphicshell')
sys.path.insert(0, '../../graphicshell/GameEngine')

from GameEngine import *
from Object import *
from Controller import *


class Pacman:
	def __init__(self):
		self.engine = GameEngine((20,17))
		# Setup Walls
		ch,c = load_object("bigger_walls.objf")
		walls = Object(ch,c)
		self.engine.add_object(walls,0)
		# Add Pacman
		ch,c = load_object("pacman.objf")
		pacman = Object(ch,c)
		pacman.set_loc((1,1))
		self.player = pacman
		self.engine.add_object(pacman,1)
		# Add Ghosts
		self.ghosts = {}
		ch,c = load_object("pinky.objf")
		pinky = Object(ch,c)
		pinky.set_loc((10,8))
		self.ghosts["pinky"] = pinky
		self.engine.add_object(pinky,2)
		self.engine.push_frame()
		#time.sleep(10)
		#self.game_engine.terminal.cleanup()


def play(game, controller):
	# Perform Setup

	# Run Game
	while True:
		cont = controller.get_input()
		if cont != "":
			pos = controller.player.get_loc()
			if cont == "a":
				pos = (pos[0]-1,pos[1])
			elif cont == "d":
				pos = (pos[0]+1,pos[1])
			elif cont == "w":
				pos = (pos[0],pos[1]-1)
			elif cont == "s":
				pos = (pos[0],pos[1]+1)
			elif cont == "q":
				break
			else:
				continue
			if len(game.engine.check_inhabited(pos))==0:
				controller.player.set_loc(pos)
			game.engine.push_frame()

	game.engine.terminal.cleanup()
				

# Testing
if __name__ == '__main__':
	game = Pacman()
	controller = Controller(game.player,game.engine)
	play(game,controller)
