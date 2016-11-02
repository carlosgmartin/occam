from functools import lru_cache
from .terms import BaseTerm, Application, zero, successor, iterate

@lru_cache(maxsize=None)
def reduce_head(term):
	if term.is_application:
		if term.function.is_application:
			if term.function.function.is_application:
				if term.function.function.function == iterate:
					if term.function.function.argument == zero:
						x = term.argument
						return x
						# iterate zero f x →β x
					if term.function.function.argument.is_application:
						if term.function.function.argument.function == successor:
							x = term.argument
							f = term.function.argument
							i = term.function.function.argument.argument
							return Application(f, Application(Application(Application(iterate, i), f), x))
						# iterate (successor i) f x →β f (iterate i f x)
	return term

@lru_cache(maxsize=None)
def reduce_body(term):
	term = reduce_head(term)
	if term.is_application:
		return Application(reduce_body(term.function), reduce_body(term.argument))
	else:
		return term

@lru_cache(maxsize=None)
def reduce(term):
	while not term == reduce_body(term):
		term = reduce_body(term)
	return term

# Eta reduction
# (f x →β g x) ⇒ (f →η g)

# Second-order eta reduction?
# (f x y →β g x y) ⇒ (f →η2 g)
