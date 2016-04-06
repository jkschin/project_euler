import math
from euler import *

sieve = sieve_of_erasthothenes(100)
primes_in_reduced_form = prime_decomposition(100,sieve)

def factors(prime_list):
	length = len(prime_list)
	if length==2:
		print prime_list
		return 0
	for i in range(length):
		for j in range(i+1,length):
			a = prime_list[0:i] + prime_list[i+1:j] + prime_list[j+1:] + [prime_list[j]*prime_list[i]]
			print a
			factors(a)
			


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
	
factors([2,2,5,5])
