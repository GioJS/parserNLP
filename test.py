#encoding: utf-8
from CYK import *

def true_answer(ans):
    if ans.strip().lower() in ['true','1','yes','ok','sì','si','ja','da','oui']:
        return True
    return False

prob=true_answer(raw_input('probabilistico? '))


if not prob:
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
else:
	from StochasticGrammar import *

	G=StochasticGrammar('S')
	G.add_rules_from_file('BigGrammar')
	G.init_chances()
	print G.grammar_chances