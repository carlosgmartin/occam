class Term:

	def __eq__(self, other):
		return self.__dict__ == other.__dict__

	def __repr__(self):
		return str(self)

	def __eq__(self, other):
		return self.__dict__ == other.__dict__

	def __hash__(self):
		return hash(frozenset(self.__dict__.items()))


class BaseTerm(Term):

	def __init__(self, type_, name='[none]'):
		self.is_application = False
		self.type = type_
		self.name = name

	def __str__(self):
		return self.name


class Application(Term):

	def __init__(self, function, argument):
		assert argument.type <= function.type.argument

		if function == K:
			A = argument.type
			B = top
			self.type = Function(B, A)
		elif function == S:
			A = argument.type.argument
			B = argument.type.result.argument
			C = argument.type.result.result
			self.type = Function(Function(A, B), Function(A, C))
		else:
			self.type = function.type.result

		self.is_application = True
		self.function = function
		self.argument = argument

	def __str__(self):
		return '({} {})'.format(self.function, self.argument)


from .types import natural, Function, top

zero = BaseTerm(natural, 'zero')
successor = BaseTerm(Function(natural, natural), 'succ')
iterate = BaseTerm(Function(natural, Function(Function(natural, natural), Function(natural, natural))), 'iter')

K = BaseTerm(Function(top, Function(top, top)), 'S')
S = BaseTerm(Function(Function(top, Function(top, top)), Function(Function(top, top), Function(top, top))), 'K')






