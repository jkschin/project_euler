import euler
import math

sieve = euler.sieve_of_eratosthenes(100000)
sieve_dic = euler.list_to_dic(sieve)

def check_goldbach(n):
	prime_ptr = 0
	while(True):
		prime = sieve[prime_ptr]
		if prime > n:
			break
		if euler.is_square((n - prime)/2):
			return True
		prime_ptr += 1
	return False

def main():
	n = 9
	while(True):
		if n not in sieve_dic:
			if not check_goldbach(n):
				break
		n += 2
	return n


print main()
