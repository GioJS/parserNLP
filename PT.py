def PT(NT):
	def __init__(self,rule):
		#check if rule is A->b, pre-terminal
		if len(rule.keys())==1 and rule.keys()[0].islower():
			self.NT.__init__(self,rule)
		else:
			raise Exception("Error, pre-terminal must be A->b")