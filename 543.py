from sympy import sieve
import bisect


def sieve(n):
    "Return all primes <= n."
    np1 = n + 1
    s = range(np1) # leave off `list()` in Python 2
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in xrange(2, sqrtn + 1): # use `xrange()` in Python 2
        if s[i]:
            # next line:  use `xrange()` in Python 2
            s[i*i: np1: i] = [0] * len(xrange(i*i, np1, i))
    return filter(None, s)

sieve = list(sieve(100))
n = 10
def base_list(sieve):
	for i in range(len(sieve)):
		if sieve[i]>n:
			break
	return sieve[:i]

def partition(prime_sums,sieve):
	a = []
	flag = False
	for i in range(len(prime_sums)):
		base = prime_sums[i]
		for j in range(i,len(sieve)):
			sum_of_two_primes = base+sieve[j]
			if (base==sieve[j] and sum_of_two_primes>n):
				flag = True
				break
			elif sum_of_two_primes>n:
				break
			else:
				try:
					if sum_of_two_primes!=a[-1]:
						v = bisect.bisect_left(a,base+sieve[j])
						a = a[:v] + [sum_of_two_primes] + a[v:]
				except IndexError:
					v = bisect.bisect_left(a,base+sieve[j])
					a = a[:v] + [sum_of_two_primes] + a[v:]
		if flag:
			break
	return a
zero = base_list(sieve)
first = partition(sieve,sieve)
second = partition(first,sieve)
third = partition(second,sieve)
fourth = partition(third,sieve)
print zero
print first
print second
print third
print fourth
total = len(zero) + len(first) + len(second) + len(third) + len(fourth)
print total

