from .CYK import *

class CYKProb(CYK):
	def __init__(self,G,s,k):
		self.k=k
		CYK.__init__(self,G,s)
		self.P=[]
		for i in range(self.n):
			self.P.append([])
			for j in range(self.n):
				self.P[i].append([])
				for k in range(self.G.NT_number()):
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
		            self.P[i][i][self.G.getHeadIndex(rule.head())]=self.G.getPr(rule)
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
		                print(rule)
		                B=rule[0]
		                C=rule[1]
		                #regole di B e C
		                rule_B=self.G.get_rules(B)
		                rule_C=self.G.get_rules(C)
		                # print rule_B, rule_C
		                
		                for b in rule_B:
		                    for c in rule_C:
	                        #if self.G[b] in self.C[j,j+k] and self.G[c] in self.C[j+k+1,j+i]:
	                			t1=self.P[j][j+k][self.G.getHeadIndex(self.G[b].head())]
	                			t2=self.P[j+k+1][j+i][self.G.getHeadIndex(self.G[c].head())]
	                			if t1==0 or t2==0:
	                				continue
	                			prob=t1*t2*self.G.getPr(rule)

	                			# print prob
	                			# print self.P[j][j+i][rule.index]
	                			if prob>=self.P[j][j+i][self.G.getHeadIndex(rule.head())]:
	                				limit+=1
	                				#print limit,prob,rule
	                				print(t1)
	                				print(t2)
	                				print(self.G.getPr(rule))
	                				print(prob)
	                				print(self.P[j][j+i][self.G.getHeadIndex(rule.head())])
	                				self.P[j][j+i][self.G.getHeadIndex(rule.head())]=prob
	                				if len(self.C[j,i+j])>0:
	                					self.C[j,i+j].pop()
	                				self.C[j,i+j].addChart(rule,j+k+1)
	                			if limit==self.k:
	                				break
		                    if limit == self.k:
		                    	break