'''
Classe che rappresenta una Grammatica utilizzabile da un parser qualsiasi
authors: Giordano Cristini, Caterina Masotti
'''

from Rule import *

class Grammar:
	
	def __init__(self, S):
		'''
		Costruttore, prende in input lo start symbol S
		'''
		self.grammar=[]
		self.index=0
		self.groups={}
		self.S=S
	
	def __getitem__(self,index):
		'''
		Overloading operatore [], in questo modo si ottiene una regola tramite indice
		'''
		return self.grammar[index]

	
	def add_rule(self,H,P):
		'''
		Aggiunge una regola alla grammatica, H (testa della produzione) di tipo string, P (produzione) di tipo string
		'''
		self.grammar.append(Rule(H,P,self.index))
		if H in self.groups:
                    self.groups[H].append(self.index)
                else:
                    self.groups[H]=[]
                    self.groups[H].append(self.index)
                self.index+=1
	
	def add_rules_from_file(self,file):
		'''
    	Aggiunge regole da una grammatica scritta su file
    	'''
		with open(file,'r') as f:
			for line in f:
				tokens=line.rstrip('\n').split('->')
				H=tokens[0].strip()
				P=tokens[1].strip()
				self.add_rule(H,P)
	
	def get_start_rules(self):
		'''
		Fornisce la lista delle regole dello start symbol S
		'''
		return self.get_rules(self.S)
	
	def get_rules(self,H):
		'''
		Data una testa di produzione fornisce la lista delle sue produzioni
		'''
		return self.groups[H]
	
	def get_unit_productions(self):
		'''
		Fornisce la lista delle produzioni A->b, dove b simbolo terminale
		'''
		result=[]
		for rule in self.grammar:
			if rule.is_preterminal():
				result.append(rule)
		return result
	
	def get_nonunit_productions(self):
		'''
		Fornisce la lista delle produzioni che non sono preterminali
		'''
		result=[]
		for rule in self.grammar:
			if not rule.is_preterminal():
				result.append(rule)
		return result
	
	def size(self):
		'''
		Fornisce la grandezza della grammatica, numero di regole
		'''
		return len(self.grammar)
	
	def NT_number(self):
		'''
		Fornisce il numero di Non Terminali della grammatica
		'''
		number=0
		visited=[]
		for rule in self.grammar:
			if not rule.head() in visited:
				number+=1
				visited.append(rule.head())
		return number