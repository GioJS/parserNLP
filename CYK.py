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
        for each i = 1 to n
            for each unit production Rj -> ai
                set P[1,i,j] = true
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
                
            #return tokens