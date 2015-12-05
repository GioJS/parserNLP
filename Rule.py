class Rule:
	def __init__(self,H,P):
		self.rule={H:P}

	def __repr__(self):
		return self.head()+" -> "+self.production()

	def head(self):
		return self.rule.keys()[0]

	def production(self):
		return self.rule.values()[0]

	def count(self):
		return self.production().count(' ')