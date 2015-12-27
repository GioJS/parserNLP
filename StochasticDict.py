class StochasticDict(dict):
	def __init__(self):
		dict.__init__(self)

	def __sum(self):
		sum=0
		for i in self.values():
			sum+=i
		return sum

	def normalize(self):
		for k in self.keys():
			self[k]/=self.__sum()