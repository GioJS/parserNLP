class CYKProb(CYK):
	def __init__(self,G,s,k):
		self.k=k
		CYK.__init__(self,G,s)

	#override	
	def parse(self):
		pass