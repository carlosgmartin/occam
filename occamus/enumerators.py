from functools import lru_cache
from .terms import BaseTerm, Application, zero, successor, iterate, S, K
from .reducers import reduce
from itertools import chain, count

@lru_cache(maxsize=None)
def terms(size):
	if size == 0:
		return [zero, successor, iterate, S, K]
	else:
		results = []
		for argument_size in range(size):
			for argument in terms(argument_size):
				for function in functions(argument.type, size - 1 - argument_size):
					term = Application(function, argument)
					
					# Check for beta duplication
					if reduce(term) in reduced(term.type, size):
						continue

					# Check for eta duplication
					if term.type.is_function:
						x = BaseTerm(term.type.argument)
						application = reduce(Application(term, x))
						applications = [reduce(Application(other_term, x)) for other_term in reduced(term.type, size)]
						if application in applications:
							continue
				
					results.append(term)

		return results

		return [
			Application(function, argument)
			for argument_size in range(size)
			for argument in terms(argument_size)
			for function in functions(argument.type, size - 1 - argument_size)
			if reduce(Application(function, argument)) not in reduced(Application(function, argument).type, size)
		]

@lru_cache(maxsize=None)
def functions(type_, size):
	return [
		term
		for term in terms(size)
		if term.type.is_function and type_ <= term.type.argument
	]

@lru_cache(maxsize=None)
def reduced(type_, size_bound):
	return [
		reduce(term)
		for size in range(size_bound)
		for term in terms(size)
		if term.type == type_
	]

def all_terms():
	for size in count():
		yield from terms(size)