import math
import collections

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
def sieve_of_eratosthenes(n):
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
'''
Inputs:
Outputs:
Example:
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

'''
Inputs:
	l: A list of numbers.
Outputs:
	out: All numbers in the list multiplied together.
Example:
	l = [2,3,4,5,6], returns 720
'''
@jit
def multiply_list(l):
	out = 1
	for element in l:
		out *= element
	return out

@jit
def list_to_dic(l):
	dic = {}
	for i in l:
		dic[i] = -1
	return dic

@jit
def factorial(n):
	if n==0:
		return 1
	else:
		ans = 1
		for i in range(1,n+1):
			ans *= i
		return ans

@jit
def is_square(n):
	sq = math.sqrt(n)
	if (int(sq))**2 == n:
		return True
	return False

'''
Inputs:
	str: A string.
Outputs:
	True or False.
Example:
	str = "585", returns True
	str = "589", returns False
'''
@jit
def check_palindrome(str):
	for i in range(len(str)):
		if str[i] != str[-1-i]:
			return False
	return True

def count_unique_digits(n):
	dic = collections.defaultdict(int)
	while (n / 10) != 0:
		dic[n % 10] += 1
		n /= 10
	dic[n % 10] += 1
	return dic
