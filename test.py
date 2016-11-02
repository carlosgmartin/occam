from occamus.types import BaseType, Function

natural = BaseType('natural')
print(natural)

unary_function = Function(natural, natural)
print(unary_function)

binary_function = Function(natural, unary_function)
print(binary_function)

from occamus.terms import BaseTerm, Application

zero = BaseTerm(natural, 'zero')
print('{} : {}'.format(zero, zero.type))

successor = BaseTerm(unary_function, 'successor')
print('{} : {}'.format(successor, successor.type))

one = Application(successor, zero)
print('{} : {}'.format(one, one.type))

two = Application(successor, one)
print('{} : {}'.format(two, two.type))