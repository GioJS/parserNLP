from CYK import *
G=Grammar('S')
G.add_rules_from_file('gramm_test')
#print G.get_unit_productions()
s='she eats a fish with a fork'
parser=CYK(G,s)
print parser.parse()