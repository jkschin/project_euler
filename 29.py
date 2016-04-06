from euler import *
from numba import jit
import numpy as np

lower, upper = (2, 100)
sieve = sieve_of_eratosthenes(100)

@jit
def get_distinct_powers(lower,upper):
	_dict = {}
	for a in range(lower, upper+1):
		for b in range(lower, upper+1):
			_dict[a**b] = -1
	return _dict

print len(get_distinct_powers(lower,upper))