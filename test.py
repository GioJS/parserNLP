# from CYK import *
# G=Grammar('S')
# G.add_rules_from_file('gramm_test')
# #print G.get_unit_productions()
# s='jeff trains geometry students'
# parser=CYK(G,s)
# parser.parse()
# #print G.get_start_rules()
# parser.derivations()
from StochasticGrammar import *

G=StochasticGrammar('S')
G.add_rules_from_file('BigGrammar')
G.init_chances()
print G.grammar_chances