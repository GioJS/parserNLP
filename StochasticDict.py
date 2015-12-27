class StochasticDict(dict):
	def __init__(self):
		dict.__init__(self)
	def __setitem__(self,key,item):
		if (self.__sum()+item)<=1:
			self.setdefault(key,item)
		else:
			raise Exception('sum of chances must be <= 1')
	def __sum(self):
		sum=0
		for i in self.values():
			sum+=i
		return sum