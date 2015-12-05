from Rule import *

class Grammar:
	def __init__(self):
		self.grammar=[]

	def add_rule(self,rule):
		self.grammar.append(rule)

	def add_rule(self,H,P):
		self.grammar.append(Rule(H,P))

	def add_rules_from_file(self,file):
		with open(file,'r') as f:
			for line in f:
				tokens=line.rstrip('\n').split('->')
				H=tokens[0]
				P=tokens[1].split(' ')
				self.add_rule(H,P)

	def get_rules(self,H):
		result=[]
		for rule in self.grammar:
			if H==rule.rule.keys()[0]:
				result.append(rule)
		return result

	def get_unit_productions(self):
		result=[]
		for rule in self.grammar:
			if len(rule.rule.values()[0])==1:
				result.append(rule)
		return result

	def get_nonunit_productions(self):
		result=[]
		for rule in self.grammar:
			if len(rule.rule.values()[0])>1:
				result.append(rule)
		return result


	def NT_number(self):
		number=0
		visited=[]
		for rule in self.grammar:
			if not rule.rule.keys()[0] in visited:
				number+=1
				visited.append(rule.rule.keys()[0])
		return number