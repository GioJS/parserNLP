'''
Classe che implementa il parser CYK
autori: Giordano Cristini, Caterina Masotti
'''

from Grammar import *
class Node:
    def __init__(self,rule,parent,l_child,r_child):
        self.rule=rule
        self.parent=parent
        self.l_child=l_child
        self.r_child=r_child
        self.flag=False
    def __repr__(self):
        return str(self.rule)+' => '+(str(self.l_child.rule) if self.l_child else '')+' & '+(str(self.r_child.rule) if self.r_child else '')
    def checked(self):
        return self.flag
    def check(self):
        self.flag=True
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
        self.D=[]
        for i in range(self.n):
            self.D.append(list())
            for j in range(self.n):
                self.D[i].append(list())
                for k in range(self.r):
                    self.D[i][j].append(Node(None,None,None,None))

    def parse(self):
        '''
        Metodo che implementa il parser CYK
        '''
        for i in range(self.n):
            for rule in self.G.get_unit_productions():
                if rule.production() == self.tokens[i]:
                    
                    self.D[0][i][rule.index].rule=rule
                    self.D[0][i][rule.index].check()
        #print "non terminals [ok]"
        #for i=1 to n -> i=1 to n+1
        for i in range(1,self.n+1):
            #for j=i-2 to 0 -> j=i-1 to 0
            for j in range(0,self.n-i):
                #for k=j+1 to i-1
                for k in range(0,i+1):
                    for rule in self.G.get_nonunit_productions():
                        #print rule
                        B=rule[0]
                        C=rule[1]
                        rule_B=self.G.get_rules(B)
                        rule_C=self.G.get_rules(C)
                        # print rule_B, rule_C
                        for b in rule_B:
                            for c in rule_C:
                                if  self.D[k][j][b].checked() and self.D[i-k][j+k][c].checked():
                                    
                                    
                                    self.D[i][j][rule.index].l_child=self.D[k][j][b]
                                    self.D[i][j][rule.index].r_child=self.D[i-k][j+k][c]
                                    self.D[i][j][rule.index].rule=rule
                                    self.D[i][j][rule.index].check()

                                    self.D[k][j][b].parent=rule
                                    self.D[i-k][j+k][c].parent=rule
                                    
                                    


    def derivation(self,H):
        '''
        Visualizza la derivazione di una data testa di produzione H
        '''
        R=self.G.get_rules(H)
        d=''
        #print H
        while len(R)>0:
            #print R
            r=R.pop()
            #print r
            #print self.D[self.n-1][0][r]
            if (self.D[self.n-1][0][r]).rule:
                #print H,":",self.G[r]
                d+=str(self.D[self.n-1][0][r])+'\n'
                #print self.G.grammar[r]
                #L=self.G[r].production().split(' ')
                if self.G[r].count()==1:
                    R+=self.G.get_rules(self.G[r][0])
                    R+=self.G.get_rules(self.G[r][1])
        return d+'\n'

    def derivations(self):
        '''
        Partendo dalla start symbol, visualizza ogni sua derivazione
        '''
        d=''
        for i in self.G.get_start_rules():
           # print i
            if (self.D[self.n-1][0][i]).rule:
                #print self.G[i]
                d+=str(self.D[self.n-1][0][i])+'\n'
                #L=self.G[i].production().split(' ')
                if self.G[i].count()==1:
                    d+=self.derivation(self.G[i][0])
                    d+=self.derivation(self.G[i][1])
        return d
