import math
from numba import jit

'''
Inputs:
	n: An integer to generate primes up to and including n.
Outputs:
	array: An array of primes.
Example:
	n = 10, returns [2,3,5,7]
	n = 11, returns [2,3,5,7,11]
'''
@jit
def sieve_of_erasthothenes(n):
	array = [0]+[0]+[1]*(n-1)
	out = []
	for i in range(2,int(math.ceil(math.sqrt(n)))):
		if array[i]==1:
			for j in range(i*i,n+1,i):
				array[j] = 0
	for i in range(len(array)): 
		if array[i]==1:
			out.append(i)
	return out

'''
Inputs:
	n: An integer for prime decomposition.
Outputs:
	array: An array of prime factors, with repeats.
Example:
	n = 1000, returns [2,2,2,5,5,5]
	n = 10, returns [2,5]
'''
@jit
def prime_decomposition(n,sieve):
	array = []
	for i in sieve:
		while True:
			if n%i==0:
				n/=i
				array.append(i)
			else:
				break
		if n==1:
			break
	return array

@jit
def multiply_list(l):
	out = 1
	for element in l:
		out *= element
	return out

