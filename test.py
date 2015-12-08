from CYK import *
G=Grammar('S')
G.add_rules_from_file('gramm_test')
#print G.get_unit_productions()
s='a a b'
parser=CYK(G,s)
print parser.parse()
#print G.get_start_rules()
print parser.get_derivations()
