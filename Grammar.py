from Rule import *

class Grammar:
	def __init__(self):
		self.grammar=[]

	def add_rule(self,H,P):
		self.grammar.append(Rule(H,P))

	def add_rules_from_file(self,file):
		with open(file,'r') as f:
			for line in f:
				tokens=line.rstrip('\n').split('->')
				H=tokens[0].strip()
				Ps=tokens[1].split(',')
				for P in Ps:
					self.add_rule(H,P.strip())

	def get_rules(self,H):
		result=[]
		for rule in self.grammar:
			if H==rule.head():
				result.append(rule)
		return result

	def get_unit_productions(self):
		result=[]
		for rule in self.grammar:
			if rule.count()==0 and rule.production().islower():
				result.append(rule)
		return result

	def get_nonunit_productions(self):
		result=[]
		for rule in self.grammar:
			if rule.count()>1:
				result.append(rule)
		return result


	def NT_number(self):
		number=0
		visited=[]
		for rule in self.grammar:
			if not rule.head() in visited:
				number+=1
				visited.append(rule.head())
		return number