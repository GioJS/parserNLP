from Rule import *
from NT import *
from PT import *
class Grammar:
	def __init__(self):
		self.grammar=[]
	def add_rule(self,rule):
		self.grammar.append(rule)

	def add_rule(self,H,P):
		self.grammar.append(Rule(H,P))