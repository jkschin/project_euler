import euler
from numba import jit

@jit
def main(memoize):
	i = 0
	for i in range(3000000):
		s = 0
		for j in list(str(i)):
			s += memoize[int(j)]
		if s==i:
			print s

memoize = dict(zip([i for i in range(0,10)],[euler.factorial(int(i))for i in range(0,10)]))
main(memoize)