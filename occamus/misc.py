from functools import lru_cache

from .types import natural
from .terms import zero, Application, successor
from .reducers import reduce

@lru_cache(maxsize=None)
def size(term):
	if term.is_application:
		return 1 + size(term.function) + size(term.argument)
	else:
		return 0

@lru_cache(maxsize=None)
def value(term):
	assert term.type == natural
	term = reduce(term)
	if term == zero:
		return 0
	else:
		return 1 + value(term.argument)


@lru_cache(maxsize=None)
def encode(number):
	assert isinstance(number, int)
	if number == 0:
		return zero
	else:
		return Application(successor, encode(number - 1))

@lru_cache(maxsize=None)
def compressed(term):
	if term.type == natural:
		return value(reduce(term))
	elif term.is_application:
		return '({} {})'.format(compressed(term.function), compressed(term.argument))
	else:
		return term