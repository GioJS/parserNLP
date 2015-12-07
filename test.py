from CYK import *
G=Grammar('S')
G.add_rules_from_file('gramm_test')
#print G.get_unit_productions()
s='b a b b'
parser=CYK(G,s)
print parser.parse()