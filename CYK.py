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
    def __repr__(self):
        s=''
        for i in self:
            s+=str(i)+'\t'
        return s
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
    def __repr__(self):
        s=''
        for i in range(len(self.matrix)):
            si=''
            for j in range(len(self.matrix)):
                si+=str(self[i,j]) if self[i,j] else '\t-\t'
            s+=si+'\n'
        return s
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
                    #print rule
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
                                    self.C[j,i+j].addChart(rule,j+k+1)
    
    def getTrees(self):
        '''
        quello che mi e venuto in mente e abbastanza strambo:
        ricreo la situazione del metodo parse:
        e vado a a controllare quello che viene messo negli indici di cui sopra
        poi viene una cosa che forse non ha senso ma nemmeno troppo sbagliata
        se r1 e r2 fanno riferimento a r(r->r1 r2) vedo se il valore:
        r1.split_point+r.split_point=r2.split_point+r.split_point
        che forse mi deve dire che i due sono lo split del primo (r)
        questo funziona quasi del tutto ma solo in 3 casi e vero
        mancano altri casi, forse mi sto avvicinando XD
        '''
        trees=[]
        for i in range(1,self.n):
            for j in range(0,self.n-i):
                for k in range(0,i):
                    for r1 in self.C[j,j+k]:
                        i_r1=r1.split_point
                        for r2 in self.C[j+k+1,j+i]:
                            i_r2=r2.split_point
                            for r in self.C[j,i+j]:
                                #print r1,r2,r
                                print i_r1,i_r2,r.split_point
                                if (r.rule[0]==r1.rule.head() and r.rule[1]==r2.rule.head()) and i_r1+r.split_point==i_r2+r.split_point:
                                    print r,r1,r2


        

        