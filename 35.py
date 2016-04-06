import euler

n = 1000000
sieve = euler.list_to_dic(euler.sieve_of_eratosthenes(n))
def check_circular_prime(n):
	n = str(n)
	return all([True if int(n[i:] + n[:i]) in sieve else False for i in range(len(n))])
		

def main():
	count = 0
	for i in sieve.keys():
		if check_circular_prime(i):
			count += 1
	return count

print main()