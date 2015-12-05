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

	def get_rules(self,H):
		result=[]
		for rule in self.grammar:
			if H==rule.rule.keys()[0]:
				result.append(rule)
		return result