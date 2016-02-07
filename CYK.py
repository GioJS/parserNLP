'''
Classe che implementa il parser CYK
autori: Giordano Cristini, Caterina Masotti
'''

from Grammar import *

'''
Classe che rappresenta il Chart ( regola , split point)
'''
class Chart:
    def __init__(self,rule,split_point=0):
        self.rule=rule
        self.split_point=split_point
    def __repr__(self):
        return "("+str(self.rule)+","+str(self.split_point)+")"
'''
Lista dei Chart
'''
class ChartList(list):
    def __init__(self,l=[]):
        list.__init__(self,l)
    def addChart(self,rule,split_point):
        self.append(Chart(rule,split_point))
    def __contains__(self,x):
        for i in self:
            if x==i.rule:
                return True
        return False
'''
Struttura utilizzabile in un algoritmo di chart parsing
'''
class ChartMatrix:
    def __init__(self,n):
        self.matrix=[]
        for i in range(n):
            self.matrix.append([])
            for j in range(n):
                self.matrix[i].append(ChartList())
    #chartmatrix[i,j]
    def __getitem__(self,pos):
        x,y=pos
        return self.matrix[x][y]
# class Node:
#     def __init__(self,rule,parent,l_child,r_child):
#         self.rule=rule
#         self.parent=parent
#         self.l_child=l_child
#         self.r_child=r_child
#         '''
#         flag di visita
#         '''
#         self.flag=False
#     def __repr__(self):
#         return str(self.rule)+' => '+(str(self.l_child.rule) if self.l_child else '')+' & '+(str(self.r_child.rule) if self.r_child else '')
#     def checked(self):
#         return self.flag
#     def check(self):
#         self.flag=True
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
        #self.D=[]
        #definisce la struttura chart
        self.C=ChartMatrix(self.n)
        #print self.C.matrix
        '''
        crea matrice 3D di nodi
        '''
        # for i in range(self.n):
        #     self.D.append(list())
        #     for j in range(self.n):
        #         self.D[i].append(list())
        #         for k in range(self.r):
        #             self.D[i][j].append(Node(None,None,None,None))

    def parse(self):
        '''
        Metodo che implementa il parser CYK
        '''
        for i in range(self.n):
            for rule in self.G.get_unit_productions():
                if rule.production() == self.tokens[i]:
                    #inizializza il primo livello
                    self.C[i,i].addChart(rule,0)
                    # self.D[0][i][rule.index].rule=rule
                    # self.D[0][i][rule.index].check()
        #print "non terminals [ok]"
        #for i=1 to n -> i=1 to n+1
        for i in range(1,self.n):
            #for j=i-2 to 0 -> j=i-1 to 0
            #print i
            for j in range(0,self.n-i):
                #for k=j+1 to i-1
                for k in range(0,i):
                    for rule in self.G.get_nonunit_productions():
                        #print rule
                        B=rule[0]
                        C=rule[1]
                        #regole di B e C
                        rule_B=self.G.get_rules(B)
                        rule_C=self.G.get_rules(C)
                        # print rule_B, rule_C
                        for b in rule_B:
                            for c in rule_C:
                                #print i
                                #print k,i-k
                                #print j+k+1,self.n
                                #print self.D[k][j][b].checked(),self.D[i-k][j+k+1][c].checked()
                                # if  self.D[k][j][b].checked() and self.D[i-k][j+k+1][c].checked():
                                #     '''
                                #     se k,j,b e i-k,j+k,c sono stati visitati dal CYK
                                #     allora li aggiunge come figli di i,j,rule.index
                                #     e si marca come visitato
                                #     '''
                                #     self.D[i+1][j][rule.index].l_child=self.D[k][j][b]
                                #     self.D[i+1][j][rule.index].r_child=self.D[i-k][j+k+1][c]
                                #     self.D[i+1][j][rule.index].rule=rule
                                #     self.D[i+1][j][rule.index].check()
                                #     '''
                                #     assegna ai figli il padre
                                #     '''
                                #     self.D[k][j][b].parent=rule
                                #     self.D[i-k][j+k+1][c].parent=rule
                                #print j,k,self.C[j,j+k]
                                if self.G[b] in self.C[j,j+k] and self.G[c] in self.C[j+k+1,j+i]:
                                    self.C[j,i+j].addChart(rule,j+k)

                                    
                                    


    def getTrees(self):
        '''
        per ogni produzione dello start symbol
        visito in profondita' e costruisco l'albero
        '''
        trees=[]

        