from CYK import *

class CYKProb(CYK):
	def __init__(self,G,s,k):
		self.k=k
		CYK.__init__(self,G,s)
		self.P=[]
		for i in range(self.n):
			self.P.append([])
			for j in range(self.n):
				self.P[i].append([])
				for k in range(self.G.size()):
					self.P[i][j].append(0)
		

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
		            self.P[i][i][rule.index]=self.G.getPr(rule)
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
		            	limit=0
		                #print rule
		                B=rule[0]
		                C=rule[1]
		                #regole di B e C
		                rule_B=self.G.get_rules(B)
		                rule_C=self.G.get_rules(C)
		                # print rule_B, rule_C
		                
		                for b in rule_B:
		                    for c in rule_C:
	                        #if self.G[b] in self.C[j,j+k] and self.G[c] in self.C[j+k+1,j+i]:
	                			t1=self.P[j][j+k][b]
	                			t2=self.P[j+k+1][j+i][c]

	                			prob=t1*t2*self.G.getPr(rule)

	                			if prob>self.P[j][j+i][rule.index]:
	                				limit+=1
	                				print limit,prob,rule
	                				self.P[j][j+i][rule.index]=prob
	                				self.C[j,i+j].addChart(rule,j+k+1)
	                			if limit==self.k:
	                				break
		                    if limit == self.k:
		                    	break