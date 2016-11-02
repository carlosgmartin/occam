class Type:

	def __eq__(self, other):
		return self.__dict__ == other.__dict__

	def __repr__(self):
		return str(self)

	def __eq__(self, other):
		return self.__dict__ == other.__dict__

	def __hash__(self):
		return hash(frozenset(self.__dict__.items()))

	def __le__(self, other):
		return (self == other) or (other == top)


class BaseType(Type):

	def __init__(self, name):
		self.is_function = False
		self.name = name

	def __str__(self):
		return self.name


class Function(Type):

	def __init__(self, argument, result):
		self.is_function = True
		self.argument = argument
		self.result = result

	def __str__(self):
		return '({} → {})'.format(self.argument, self.result)


natural = BaseType('natural')

top = BaseType('⊤')