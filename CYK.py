from Grammar import *

class CYK:
	def __init__(self,G,s):
		self.s=s
		self.G=G
		r=self.G.NT_number()
		n=len(self.s)
		self.P=[[[False]*n]*n]*r