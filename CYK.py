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

    def parse(self):
        for i in range(self.n):
            for rule in self.G.get_unit_productions():
                if rule.production() == self.tokens[i]:
                    #print i,rule,rule.index
                    self.P[0][i][rule.index]=True
        #print "non terminals [ok]"
        #for i=1 to n -> i=0 to n-1
        for i in range(1,self.n+1):
            #for j=i-2 to 0 -> j=i-1 to 0
            for j in range(i-1,-1,-1):
                #for k=j+1 to i-1
                for k in range(j+1,i-1):
                    #print "i: %d,j: %d,k: %d" % (i,j,k)
                    for rule in self.G.get_nonunit_productions():
                        #print rule
                        B,C=rule.production().split(' ')
                        rule_B=self.G.get_rules(B)
                        rule_C=self.G.get_rules(C)
                        # print rule_B, rule_C
                        for b in rule_B:
                            for c in rule_C:
                                if self.P[i-1][k][b] and self.P[k][j][c]:
                                    #print rule
                                    #print self.G.grammar[b]
                                    #print self.G.grammar[c]
                                    #print i,j,k,b,c
                                    #print rule,",",B,",",C
                                    self.P[i-1][j][rule.index]=True
    def derivation(self,H):
        R=self.G.get_rules(H)
        #print H
        while len(R)>0:
            r=R.pop()
            if self.P[self.n-1][0][r]:
                print self.G[r]
                #print self.G.grammar[r]
                #L=self.G[r].production().split(' ')
                if self.G[r].count()==2:
                    R+=self.G.get_rules(self.G[r][0])
                    R+=self.G.get_rules(self.G[r][1])

    def derivations(self):
        for i in self.G.get_start_rules():
            if self.P[self.n-1][0][i]:
                print self.G[i]
                #L=self.G[i].production().split(' ')
                if self.G[i].count()==2:
                    self.derivation(self.G[i][0])
                    self.derivation(self.G[i][1])
