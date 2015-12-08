from CYK import *
G=Grammar('S')
G.add_rules_from_file('gramm_test')
#print G.get_unit_productions()
s='the cat is cute'
parser=CYK(G,s)
print parser.parse()
#print G.get_start_rules()
for i in G.get_start_rules():
	print parser.P[parser.n-1][0][i]
