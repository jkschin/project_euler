from euler import *
import numpy as np

def prime_powers(array):
	array = [(i,array.count(i)) for i in list(set(array))]
	return array

def multiply_base(pp):
	for power in pp:
		power[1]=power[1]*2
	return pp
sieve = sieve_of_erasthothenes(100)
dic = {}
for i in range(2,3):
	base = prime_powers(prime_decomposition(i,sieve))
	base = multiply_base(base)
	dic[tuple(base)] = 1
	for j in range(1,99):
		for power in base:
			power[1]+=1
		dic[tuple(base)] = 1
