from occamus.enumerators import all_terms
from occamus.misc import compressed, size, value, encode
from occamus.types import natural, Function
from occamus.terms import Application

for term in all_terms():

	print('{} : {}'.format(term, term.type))
	input()
	continue

	print('{}\t{}'.format(size(term), compressed(term)))
	input()
	if term.type == Function(natural, natural):
		print(value(Application(term, encode(42))))
	if term.type == natural:
		print(value(term))
		print('{}\t{}'.format(value(term), term))