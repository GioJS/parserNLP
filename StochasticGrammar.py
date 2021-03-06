'''
Classe che rappresenta una grammatica probabilistica
autori: Giordano Cristini, Caterina Masotti
'''

from .Grammar import *
import random
import copy
import heapq
import operator
class StochasticGrammar(Grammar):

	def __init__(self,S):
		'''
		Costruttore, prende in input lo start symbol
		'''
		Grammar.__init__(self,S)
		self.grammar_chances={}

	def init_chances(self):
		'''
			Assegna per ogni gruppo di produzioni, le probabilita' ad ogni regola del gruppo
		'''
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
				rands.sort(reverse=True)
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

	def getPr(self,rule):
		return self.grammar_chances[self[rule.index].head()][rule.index]
	def getHeadIndex(self,H):
		return list(self.groups.keys()).index(H)
	# def getKMax(self,H,k):
	# 	itemlist=[(key,v) for key,v in self.grammar_chances[H].iteritems()]
	# 	return heapq.nlargest(k,itemlist)
		



