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

print parser.getTrees()
# from StochasticGrammar import *

# G=StochasticGrammar('S')
# G.add_rules_from_file('BigGrammar')
# G.init_chances()
# print G.grammar_chances