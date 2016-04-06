import euler
from numba import jit

dic = euler.list_to_dic(euler.sieve_of_eratosthenes(10000000))

def main():
	max_val = -1
	global_a, global_b = 0, 0
	for a in range(-999,1000):
		for b in range(-999,1000):
			n = 0
			count = 0
			while(True):
				if (n**2 + a*n + b) in dic:
					count += 1
				else:
					break
				n += 1
			if count>=max_val:
				max_val = count
				global_a, global_b = a, b 
	return global_a, global_b, max_val

global_a, global_b, max_val = main()
print (global_a,global_b,max_val)


