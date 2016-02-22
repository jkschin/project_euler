import math
from numba import jit
'''
64 bit prime: 18446744073709551557
'''


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
def prime_decomposition(n,sieve):
	array = []
	for i in sieve:
		while(1):
			if n%i==0:
				n/=i
				array.append(i)
			else:
				break
		if n==1:
			break
	return array

'''
Inputs:
	n: An integer for prime decomposition.
Outputs:
	array: An array of prime factors, with repeats.
Example:
	n = 1000, returns [2,2,2,5,5,5]
	n = 10, returns [2,5]
'''
def modular_pow(base, exponent, modulus):
	if (modulus-1)**2 > (2**64-1): raise Exception( "Invalid Modulus. Use a smaller one." )
	if modulus == 1:
		return 0
	result = 1
	base = base % modulus
	while exponent > 0:
		if (exponent%2)==1:
			result = (result * base) %  modulus
			quotient = (result * base) // modulus
			print quotient
		exponent = exponent >> 1
		base = (base**2) % modulus
	return result




