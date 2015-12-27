from Grammar import *
from StochasticDict import *
import random
class StochasticGrammar(Grammar):
	def __init__(self,S):
		Grammar.__init__(self,S)
		self.grammar_chances={}

	def init_chances(self):
		for group in self.groups:
			chances={}
			if len(self.groups[group])==1:
				chances[self.groups[group][0]]=1.0
				self.grammar_chances[group]=chances
				#print self.grammar[self.groups[group][0]], 1.0
			else:
				rands=[random.uniform(0,1) for i in range(len(self.groups[group]))]
				s = sum(rands)
				rands = [ i/s for i in rands ]
				for rule in self.groups[group]:
					#while True:
					#	try:
					chances[rule]=rands.pop()
							#break
					#	except Exception as e:
					#		pass
					#print self.grammar[rule], chances[rule]
				
				#chances.normalize()
				self.grammar_chances[group]=chances


