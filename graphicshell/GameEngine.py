"""
@author: jormungandr1105
@desc: The foundation for a game engine
       utilizing the terminal class
@created: 06/25/2022
"""
#import os

from Terminal import Terminal
from utils.colors import *


class GameEngine:
	def __init__(self, size, default_color=None):
		(self.width,self.height) = size
		assert(type(self.width)==int)
		assert(type(self.height)==int)
		self.terminal = Terminal()
		self.terminal.resize((self.width,self.height))
		if default_color is not None:
			for i in range(self.width):
				for j in range(self.height):
					self.terminal.set_pixel((i,j)," ",default_color)
		self.render_pipeline = []

	def add_object(self, new_object, index):
		if index < 0:
			index = 0
		if index < len(self.render_pipeline):
			self.render_pipeline.insert(index,new_object)
		else:
			self.render_pipeline.append(new_object)

	def check_inhabited(self,pos):
		inhabitants = []
		for obj in self.render_pipeline():
			if obj.check_inhabited(pos):
				inhabitants.append(obj)
		return inhabitants

	def remove_object(self, obj):
		self.render_pipeline.remove(obj)

	def push_frame(self):
		self.terminal.clear()
		for obj in self.render_pipeline:
			for i in range(obj.pos[0],obj.pos[0]+obj.size[0]):
				for j in range(obj.pos[1],obj.pos[1]+obj.size[1]):
					if obj.get_char((i,j)) != "":
						self.terminal.set_pixel((i,j),obj.get_char((i,j)),obj.get_clr((i,j)))
		self.terminal.print()


# Testing
if __name__ == '__main__':
	class_test = GameEngine()
