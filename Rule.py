'''
Classe che rappresenta una regola di una grammatica
autori: Giordano Cristini, Caterina Masotti
'''


from string import punctuation
class Rule:
	
	def __init__(self,H,P,index):
		'''
		Costruttore, prende in input H (testa della produzione), P (Produzione), index (indice nella lista)
		'''
		self.index=index
		self.rule={H:P}
		self.productions=[]
		if self.count()>0:
			self.productions=self.production().split(' ')
	
	def __repr__(self):
		'''
		Rappresentazione in stringa della regola, (Debug)
		'''
		return self.head()+" -> "+self.production()
	
	def __getitem__(self,index):
		'''
		Overloading operatore [] per ottenere una dato simbolo
		'''
		return self.productions[index]
	
	def head(self):
		'''
		Fornisce la testa della produzione
		'''
		return list(self.rule.keys())[0]
	
	def production(self):
		'''
		Fornisce la produzione
		'''
		return list(self.rule.values())[0]
	
	def count(self):
		'''
		Conta il numero di simboli che vengono prodotti
		'''
		return self.production().count(' ')
	
	def is_preterminal(self):
		'''
		Restituisce True se la regola e' Pre-Terminale, False altrimenti
		'''
		if self.count()==0 and self.production().islower():
			return True
		return  self.count()==0 and (self.production().isdigit() or (1 in [c in self.production() for c in punctuation]))