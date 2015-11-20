class NT:
	def __init__(self,rule):
		if type(rule) != dict:
			raise Exception("Error, rule must be a dict")
		if rule.keys()[0].islower():
				raise Exception("Error, rule must be A->b")
		self.rule=rule
