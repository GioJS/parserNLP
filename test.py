#encoding: utf-8
import signal
import sys
import time



from CYK import *
def signal_handler(signal, frame):
        print('Sei uscito!')
        sys.exit(0)
def true_answer(ans):
    if ans.strip().lower() in ['true','1','yes','ok','sì','si','ja','da','oui']:
        return True
    return False

signal.signal(signal.SIGINT, signal_handler)

prob=true_answer(input('probabilistico? '))
start = time.clock()


s="she is cute"
if not prob:
	G=Grammar('S')
	G.add_rules_from_file('BigGrammar')
	#print G.get_unit_productions()
	#s=raw_input('write a phrase: ')

	parser=CYK(G)
	parser.parse(s)
	print(parser.C)
	print(parser.getTrees())
	#print parser.derivations()
	#pre-t
	#print parser.D

	#print parser.getTrees()
else:
	from .StochasticGrammar import *
	from .CYKProb import *

	G=StochasticGrammar('S')
	G.add_rules_from_file('BigGrammar')
	G.init_chances()
	#print G.getKMax('VP',2)
	#print G.grammar_chances
	k=1
	parser=CYKProb(G,k)

	parser.parse(s)
	#print parser.P
	#print parser.C
	print(parser.getTrees())
end = time.clock()
print("%.2gs" % (end-start))
