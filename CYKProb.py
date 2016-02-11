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
		    for rule in self.G.groups.keys():
		    	for rule_i,rule_p in self.G.getKMax(rule,self.k):
		    		max_rule=self.G[rule_i]
		    		if not max_rule.is_preterminal():
		    			continue
			        if max_rule.production() == self.tokens[i]:
			            #inizializza il primo livello
			            #print rule
			            self.C[i,i].addChart(max_rule,0)
		            
		#print "non terminals [ok]"
		#for i=1 to n -> i=1 to n+1
		for i in range(1,self.n):
		    #for j=i-2 to 0 -> j=i-1 to 0
		    #print i
		    for j in range(0,self.n-i):
		        #for k=j+1 to i-1
		        for k in range(0,i):
					for rule in self.G.groups.keys():
						for rule_i,rule_p in self.G.getKMax(rule,self.k):
							max_rule=self.G[rule_i]
							#print max_rule
					    	#print rule
					    	if max_rule.is_preterminal():
					    		continue
					        B=max_rule[0]
					        C=max_rule[1]
					        #regole di B e C
					        rule_B=self.G.getKMax(B,self.k)
					        rule_C=self.G.getKMax(C,self.k)
					        # print rule_B, rule_C
					        for b,x in rule_B:
					            for c,y in rule_C:
					                if self.G[b] in self.C[j,j+k] and self.G[c] in self.C[j+k+1,j+i]:
					                    self.C[j,i+j].addChart(max_rule,j+k+1)