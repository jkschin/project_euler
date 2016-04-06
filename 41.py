import euler

sieve = euler.sieve_of_eratosthenes(999999999)

def check_pandigital(n):
	n = str(n)
	original_length = len(n)
	for i in range(len(n)+1,10):
		n = n.replace(str(i),"")
	n = n.replace("0","")
	if len(set(n))==original_length:
		return True
	else:
		return False

i = -1
while True:
	prime = sieve[i]
	if check_pandigital(prime):
		print prime
		break
	i -= 1

# check_pandigital(2143)