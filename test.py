#encoding: utf-8
from CYK import *

def true_answer(ans):
    if ans.strip().lower() in ['true','1','yes','ok','sì','si','ja','da','oui']:
        return True
    return False

prob=true_answer(raw_input('probabilistico? '))

s="she eats a fish with a fork"
if not prob:
	G=Grammar('S')
	G.add_rules_from_file('BigGrammar')
	#print G.get_unit_productions()
	#s=raw_input('write a phrase: ')
	
	parser=CYK(G,s)
	parser.parse()
	print parser.C
	print parser.getTrees()
	#print parser.derivations()
	#pre-t
	#print parser.D

	#print parser.getTrees()
else:
	from StochasticGrammar import *
	from CYKProb import *
	
	G=StochasticGrammar('S')
	G.add_rules_from_file('gramm_test')
	G.init_chances()
	#print G.getKMax('VP',2)
	#print G.grammar_chances
	k=5000
	parser=CYKProb(G,s,k)
	parser.parse()
	print parser.C
	print parser.getTrees()