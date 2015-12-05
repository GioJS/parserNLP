from CYK import *
G=Grammar()
G.add_rules_from_file('gramm_test')
print G.get_unit_productions()