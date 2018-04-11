import math
print()
a=input('Digite um numero para retornar seu fatorial: ')
print()
print('{0}! = {1}'.format(a,math.gamma(float(a)+1)))
if a=='0.5':
	print()
	print('{0}^2 * 4 = {1}'.format(math.gamma(float(a)+1),math.pi))
	