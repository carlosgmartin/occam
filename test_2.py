from occamus.terms import Application, zero, successor, iterate
from occamus.reducers import reduce

one = Application(successor, zero)
two = Application(successor, one)

term = Application(
	Application(
		Application(
			iterate, 
			two
		), 
		successor
	),
	one
)

print(term)
print(reduce(term))

