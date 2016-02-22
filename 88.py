import math
from euler import *

sieve = sieve_of_erasthothenes(100)
print prime_decomposition(100,sieve)

def find_minimal(k):
	init_set = [1] * k
	init_set[-2] = 2
	pointer = -1
	while(1):
		add = sum(init_set)
		product = multiply_list(init_set)
		if product > add:
			init_set[pointer] += 1
		elif product == add:
			return product
		break
	

