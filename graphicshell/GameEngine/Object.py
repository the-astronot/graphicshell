"""
@author: jormungandr1105
@desc: Standard Game Objects
@created: 06/25/2022
"""

from utils.colors import * 


class Object:

	def __init__(self,char_rep,clr_rep):
		self.char_rep = char_rep
		self.clr_rep = clr_rep
		self.size = (len(self.char_rep),len(self.char_rep[0]))
		self.pos = (0,0)

	def set_loc(self,pos):
		self.pos = pos

	def get_loc(self):
		return self.pos

	def get_char(self,pos):
		x = pos[0] - self.pos[0]
		y = pos[1] - self.pos[1]
		pos = (x,y)
		if 0<=pos[0]<len(self.char_rep) and 0<=pos[1]<len(self.char_rep[0]):
			return self.char_rep[pos[0]][pos[1]]
		return ""

	def get_clr(self,pos):
		x = pos[0] - self.pos[0]
		y = pos[1] - self.pos[1]
		pos = (x,y)
		if 0<=pos[0]<len(self.char_rep) and 0<=pos[1]<len(self.char_rep[0]):
			return self.clr_rep[pos[0]][pos[1]]
		return reset

	def check_inhabited(self, pos):
		return self.get_char((pos[0],pos[1])) != ""


def get_color(string):
	if len(string) < 3:
		return reset
	if string[:3] == "reg":
		return reg[string[3:]]
	if string[:3] == "bld":
		return bold[string[3:]]
	if string[:3] == "und":
		return underline[string[3:]]
	if string[:3] == "bck":
		return back[string[3:]]
	return reset


def load_object(filename):
	# Load in Object File
	f = open(filename,"r")
	text = f.read()
	data = text.split("\n----------\n")
	# Setup char_rep
	char_rep_rot = data[0].split("\n")
	for i in range(len(char_rep_rot)):
		char_rep_rot[i] = char_rep_rot[i].split(",")
	char_rep = [["" for _ in range(len(char_rep_rot))] for _ in range(len(char_rep_rot[0]))]
	for x in range(len(char_rep)):
		for y in range(len(char_rep[0])):
			char_rep[x][y] = char_rep_rot[y][x]
	# Setup clr_rep
	clr_rep_rot = data[1].split("\n")
	for i in range(len(clr_rep_rot)):
		clr_rep_rot[i] = clr_rep_rot[i].split(",")
	clr_rep = [["" for _ in range(len(clr_rep_rot))] for _ in range(len(clr_rep_rot[0]))]
	for i in range(len(clr_rep)):
		for j in range(len(clr_rep[0])):
			clr_rep[i][j] = get_color(clr_rep_rot[j][i])
	return char_rep, clr_rep


# Testing
if __name__ == '__main__':
	class_test = Object()
