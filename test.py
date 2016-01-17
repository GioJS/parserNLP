from CYK import *
G=Grammar('S')
G.add_rules_from_file('gramm_test')
#print G.get_unit_productions()
s='she eats a fish with a fork'
parser=CYK(G,s)
parser.parse()
#print parser.D
#print parser.derivations()
#pre-t
#print parser.D

'''
per ogni produzione dello start symbol
visito in profondita' e costruisco l'albero
'''
for x in G.get_start_rules():
	P=[]
	#nodo y	
	y = parser.D[parser.n-1][0][x]
	print y
	#aggiungo figlio  sx e dx alla pila
	P.append(y.l_child)
	P.append(y.r_child)
	while len(P)>0:
		#tolgo q e aggiungo i suoi figli
		q=P.pop()
		if q!=None:
			print q
			P.append(q.l_child)
			P.append(q.r_child)
# from StochasticGrammar import *

# G=StochasticGrammar('S')
# G.add_rules_from_file('BigGrammar')
# G.init_chances()
# print G.grammar_chances