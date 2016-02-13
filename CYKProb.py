from CYK import *

class CYKProb(CYK):
	def __init__(self,G,s,k):
		self.k=k
		CYK.__init__(self,G,s)

	#override	
	def parse(self):
		'''
		    Metodo che implementa il parser CYK probabilistico
		'''
		for i in range(self.n):
		    for rule in self.G.get_unit_productions():
		        if rule.production() == self.tokens[i]:
		            #inizializza il primo livello
		            #print rule
		            self.C[i,i].addChart(rule,0)
		            
		#print "non terminals [ok]"
		#for i=1 to n -> i=1 to n+1
		for i in range(1,self.n):
		    #for j=i-2 to 0 -> j=i-1 to 0
		    #print i
		    for j in range(0,self.n-i):
		        #for k=j+1 to i-1
		        for k in range(0,i):
		            for rule in self.G.get_nonunit_productions():
		                #print rule
		                B=rule[0]
		                C=rule[1]
		                #regole di B e C
		                rule_B=self.G.get_rules(B)
		                rule_C=self.G.get_rules(C)
		                # print rule_B, rule_C
		                best=0
		                best_r=None
		                for b in rule_B:
		                    for c in rule_C:
		                        if self.G[b] in self.C[j,j+k] and self.G[c] in self.C[j+k+1,j+i]:
		                			t1=self.G.grammar_chances[self.G[b].head()][b]
		                			t2=self.G.grammar_chances[self.G[c].head()][c]
		                			candidate=t1*t2*self.G.grammar_chances[rule.head()][rule.index]
		                			if candidate>best:
		                				best=candidate
		                				best_r=rule
		                if best_r:
		                	self.C[j,i+j].addChart(best_r,j+k+1)