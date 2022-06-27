"""
@author: jormungandr1105
@desc: Controller Object
@created: 06/26/2022
"""
from KBHit import KBHit
from Object import *
#import Player


class Controller:
	def __init__(self, player, engine):
		self.player = player
		self.engine = engine
		self.kbhit = KBHit()
		self.enabled = True

	def enable_controller(self):
		if not self.enabled:
			self.kbhit.set_input_term()
			self.enabled = True

	def disable_controller(self):
		if self.enabled:
			self.kbhit.set_normal_term()
			self.enabled = False

	def get_input(self):
		value = ""
		if self.enabled:
			if self.kbhit.kbhit():
				value = self.kbhit.getch()
		#print(value,end="")
		return value


# Testing
if __name__ == '__main__':
	class_test = Controller()
