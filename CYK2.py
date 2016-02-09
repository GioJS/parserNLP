from Grammar import *

def create(n, constructor=list):
        for _ in xrange(n):
            yield constructor()
class CYK2:
    
    def __init__(self,G,s):
        '''
        Costruttore, prende in input la grammatica G, e la stringa da parsare s
        '''
        self.s=s
        self.G=G
        self.r=self.G.size()
        preprop = reduce(lambda a,b: a.replace(b, ' '+b), punctuation, self.s)
        self.tokens=preprop.split(' ')  
        self.n=len(self.tokens)
        self.P=[[[False]*self.r]*self.n]*self.n
        #self.D=[[list(create(self.r))]*self.n]*self.n
        self.D=[]
        for i in range(self.n):
            self.D.append(list())
            for j in range(self.n):
                self.D[i].append(list())
                for k in range(self.r):
                    self.D[i][j].append(list())