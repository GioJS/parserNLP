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
print parser.D
for x in G.get_start_rules():
	P=[]
	y = parser.D[0][1][x]
	print y
	P.append(y.l_child)
	P.append(y.r_child)
	while len(P)>0:
		q=P.pop()
		print q
		P.append(q.l_child)
		P.append(q.r_child)

# from StochasticGrammar import *

# G=StochasticGrammar('S')
# G.add_rules_from_file('BigGrammar')
# G.init_chances()
# print G.grammar_chances