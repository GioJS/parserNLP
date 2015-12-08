from string import punctuation
class Rule:
	def __init__(self,H,P,index):
		self.index=index
		self.rule={H:P}
		self.productions=[]
		if self.count()>0:
			self.productions=self.production().split(' ')
	def __repr__(self):
		return self.head()+" -> "+self.production()

	def __getitem__(self,index):
		return self.productions[index]
	def head(self):
		return self.rule.keys()[0]

	def production(self):
		return self.rule.values()[0]

	def count(self):
		return self.production().count(' ')

	def is_preterminal(self):
		if self.count()==0 and self.production().islower():
			return True
		return  self.count()==0 and (self.production().isdigit() or (1 in [c in self.production() for c in punctuation]))