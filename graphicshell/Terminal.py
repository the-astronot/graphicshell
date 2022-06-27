"""
@author: jormungandr1105
@desc: A graphics object for the terminal
@created: 06/25/2022
"""
import os
from utils.colors import *


class Terminal:

	def __init__(self):
		self.width,self.height = os.get_terminal_size()
		self.chars = [[" " for _ in range(self.height)] for _ in range(self.width)]
		self.colors = [[reset for _ in range(self.height)] for _ in range(self.width)]

	def resize(self, size):
		(x,y) = size
		print("\033[H",end="")
		print(reset,end="")
		for _ in range(self.height):
			print("\033[K")
		print("\033[H",end="")
		self.width = x
		self.height = y
		print("\033[8;{1};{0}t".format(self.width,self.height),end="")
		self.chars = [[" " for _ in range(self.height)] for _ in range(self.width)]
		self.colors = [[reset for _ in range(self.height)] for _ in range(self.width)]
		print("\033[H",end="")

	def print(self):
		print(reset,end="")
		print("\033[H",end="")
		output = ""
		for j in range(self.height):
			for i in range(self.width):
				output += self.colors[i][j]+self.chars[i][j]
			if j !=	self.height-1:
				output+="\n"
		print(output,end="")
		print("\033[H",end="")

	def set_pixel(self, pos, char, clr):
		if 0<=pos[0]<self.width and 0<=pos[1]<self.height:
			self.chars[pos[0]][pos[1]] = char[0]
			self.colors[pos[0]][pos[1]] = reset+clr
			return True
		return False

	def set_line(self, startpos, chars, clr, contnextline=False):
		(x,y) = startpos
		if 0<=y<self.height:
			char_index = 0
			j = y
			for i in range(x,self.width):
				if char_index < len(chars):
					self.set_pixel((i,j),chars[char_index],clr)
					char_index += 1
			if contnextline:
				while char_index < len(chars):
					j += 1
					if j == self.height:
						break
					for i in range(x,self.width):
						if char_index < len(chars):
							self.set_pixel((i,j),chars[char_index],clr)
							char_index += 1
			return True
		return False

	def erase_pixel(self, pos):
		if 0<=pos[0]<self.width and 0<=pos[1]<self.height:
			self.chars[pos[0]][pos[1]] = " "
			self.colors[pos[0]][pos[1]] = reset
			return True
		return False

	def clear(self):
		self.chars = [[" " for _ in range(self.height)] for _ in range(self.width)]
		self.colors = [[reset for _ in range(self.height)] for _ in range(self.width)]

	def cleanup(self):
		print("\033[H",end="")
		print(reset,end="")
		for _ in range(self.height):
			print("\033[K")
		print("\033[H",end="")


# Testing
if __name__ == '__main__':
	import time
	class_test = Terminal()
	class_test.resize((40,10))
	time.sleep(1)
	class_test.set_pixel((5,5),"@$$",reg["blue"])
	class_test.print()
	time.sleep(1)
	class_test.resize((99,11))
	string = "#####################################################################"
	red = reg["red"]
	bluebg = back["blue"]
	black = reg["black"]
	class_test.set_line((50,5),string,red,contnextline=True)
	class_test.print()
	time.sleep(2)
	class_test.set_line((60,5),string,bluebg+black)
	class_test.erase_pixel((65,5))
	class_test.print()
	time.sleep(2)
	class_test.cleanup()
