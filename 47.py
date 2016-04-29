import euler
import math
from numba import jit

sieve = euler.sieve_of_eratosthenes(100000)
sieve_dic = euler.list_to_dic(sieve)

@jit
def main():
	n = 2
	interval = 4
	while(True):
		count = 0
		for i in range(0,interval):
			if (len(set(euler.prime_decomposition(n+i,sieve))))==interval:
				count += 1
			else:
				break
		if count == interval:
			break
		n += 1
	print n

main()
