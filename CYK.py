'''
Classe che implementa il parser CYK
autori: Giordano Cristini, Caterina Masotti
'''

from Grammar import *

def create(n, constructor=list):
        for _ in xrange(n):
            yield constructor()
class CYK:
    
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
       # print self.D

    def parse(self):
        '''
        Metodo che implementa il parser CYK
        '''
        for i in range(self.n):
            for rule in self.G.get_unit_productions():
                if rule.production() == self.tokens[i]:
                    #print i,rule,rule.index
                    self.P[i][i][rule.index]=True
                    self.D[i][i][rule.index].append(rule.index)
        #print "non terminals [ok]"
        #for i=1 to n -> i=1 to n+1
        for i in range(1,self.n):
            #for j=i-2 to 0 -> j=i-1 to 0
            for j in range(0,self.n-i+1):
                #for k=j+1 to i-1
                for k in range(0,i-1):
                    for rule in self.G.get_nonunit_productions():
                        #print rule
                        B=rule[0]
                        C=rule[1]
                        rule_B=self.G.get_rules(B)
                        rule_C=self.G.get_rules(C)
                        # print rule_B, rule_C
                        for b in rule_B:
                            for c in rule_C:
                                if len(self.D[k][j][b])>0 and len(self.D[i-k][j+k][c])>0:
                                    self.P[i][j][rule.index]=True
                                    #if not rule.index in self.D[i][j][rule.index]:
                                    self.D[i][j][rule.index].append(rule.index)
    def derivation(self,H):
        '''
        Visualizza la derivazione di una data testa di produzione H
        '''
        R=self.G.get_rules(H)
        #print H
        while len(R)>0:
            r=R.pop()
            #print self.D[self.n-1][0][r]
            if len(self.D[self.n-1][0][r])>0:
                print H,":",self.G[r]
                #print self.G.grammar[r]
                #L=self.G[r].production().split(' ')
                if self.G[r].count()==1:
                    R+=self.G.get_rules(self.G[r][0])
                    R+=self.G.get_rules(self.G[r][1])

    def derivations(self):
        '''
        Partendo dalla start symbol, visualizza ogni sua derivazione
        '''
        for i in self.G.get_start_rules():
            if len(self.D[self.n-1][0][i])>0:
                print self.G[i]
                #L=self.G[i].production().split(' ')
                if self.G[i].count()==1:
                    self.derivation(self.G[i][0])
                    self.derivation(self.G[i][1])
