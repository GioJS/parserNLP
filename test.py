from CYK import *
G=Grammar(True)
G.add_rules_from_file('gramm_test')
print G.get_unit_productions()