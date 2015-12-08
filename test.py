from CYK import *
G=Grammar('S')
G.add_rules_from_file('gramm_test')
#print G.get_unit_productions()
s='b a a b a'
parser=CYK(G,s)
parser.parse()
#print G.get_start_rules()
parser.derivations()
