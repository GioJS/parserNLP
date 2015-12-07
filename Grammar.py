from Rule import *

class Grammar:
	def __init__(self, S):
		self.grammar=[]
		self.index=0
		self.groups={}
                self.S=S
        
	def add_rule(self,H,P):
		self.grammar.append(Rule(H,P,self.index))
		if H in self.groups:
                    self.groups[H].append(self.index)
                else:
                    self.groups[H]=[]
                    self.groups[H].append(self.index)
                self.index+=1
	def add_rules_from_file(self,file):
		with open(file,'r') as f:
			for line in f:
				tokens=line.rstrip('\n').split('->')
				H=tokens[0].strip()
				P=tokens[1].strip()
				self.add_rule(H,P)
	def get_start_rules(self):
			return self.get_rules(self.S)

	def get_rules(self,H):
		return self.groups[H]

	def get_unit_productions(self):
		result=[]
		for rule in self.grammar:
			if rule.is_preterminal():
				result.append(rule)
		return result

	def get_nonunit_productions(self):
		result=[]
		for rule in self.grammar:
			if not rule.is_preterminal():
				result.append(rule)
		return result

       
        def size(self):
            return len(self.grammar)

	def NT_number(self):
		number=0
		visited=[]
		for rule in self.grammar:
			if not rule.head() in visited:
				number+=1
				visited.append(rule.head())
		return number