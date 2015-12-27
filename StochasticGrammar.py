from Grammar import *
from StochasticDict import *
import random
class StochasticGrammar(Grammar):
	def __init__(self,S):
		Grammar.__init__(self,S)
		self.grammar_chances={}

	def init_chances(self):
		for group in self.groups:
			chances=StochasticDict()
			if len(self.groups[group])==1:
				chances[self.groups[group][0]]=1.0
				self.grammar_chances[group]=chances
			else:
				for rule in self.groups[group]:
					while True:
						try:
							chances[rule]=random.random()
							break
						except Exception as e:
							pass
					self.grammar_chances[group]=chances


