from Grammar import *

class CYK:
	def __init__(self,G,s):
		self.s=s
		self.G=G
		r=self.G.NT_number()
		n=len(self.s)
		self.P=[[[False]*n]*n]*r
        
        def parse(self):
            preprop = reduce(lambda a,b: a.replace(b, ' '+b), punctuation, self.s)
            tokens=preprop.split(' ')
            return tokens