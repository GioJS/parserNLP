from Grammar import *

class CYK:
	def __init__(self,G,s):
		self.s=s
		self.G=G
		self.r=self.G.size()
		
		preprop = reduce(lambda a,b: a.replace(b, ' '+b), punctuation, self.s)
                self.tokens=preprop.split(' ')
            
		self.n=len(self.tokens)
		self.P=[[[False]*self.r]*self.n]*self.n
        '''
       
        for each i = 2 to n -- Length of span
            for each j = 1 to n-i+1 -- Start of span
                for each k = 1 to i-1 -- Partition of span
                    for each production RA -> RB RC
                        if P[k,j,B] and P[i-k,j+k,C] then set P[i,j,A] = true
        if any of P[n,1,x] is true (x is iterated over the set s, where s are all the indices for Rs) then
            S is member of language
        else
            S is not member of language
  '''
        def parse(self):

            for i in range(self.n):
                for rule in self.G.get_unit_productions():
                    if rule.production() == self.tokens[i]:
                        print i,rule,rule.index
                        self.P[0][i][rule.index]=True
                        
            for i in range(1,self.n):
                for j in range(i-1,0,-1):
                    for k in range(j+1,i):
                        for rule in self.G.get_nonunit_productions():
                            print rule
                            B,C=rule.production().split(' ')
                            rule_B=self.G.get_rules(B)
                            rule_C=self.G.get_rules(C)
                           # print rule_B, rule_C
                            for b in rule_B:
                                for c in rule_C:
                                    if self.P[i][k][b] and self.P[k][j][c]:
                                        print i,j,k,b,c
                                        print rule,",",B,",",C
                                        self.P[i][j][rule.index]=True
                                    
            #return tokens