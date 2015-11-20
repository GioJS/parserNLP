from NT import NT
class PT(NT):
	def __init__(self,rule):
		if type(rule) != dict:
			raise Exception("Error, rule must be a dict")
		#check if rule is A->b, pre-terminal
		if len(rule.keys())==1 and rule[rule.keys()[0]].islower():
			NT.__init__(self,rule)
		else:
			raise Exception("Error, pre-terminal must be A->b")