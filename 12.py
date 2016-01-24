import math
import itertools
from sympy import sieve

length = 100000
sieve.extend(length)

divisors = [0]*length
divisors[1] = [1]
divisors[2] = [1,2]

def get_two_factors(n):
	i = 2
	while((n%i)!=0):
		i+=1
	return (n/i, i)

for i in range(3,length):
	if i in sieve:
		divisors[i] = [1,i]
	else:
		a,b = get_two_factors(i)
		divisors[i] = list(set([x * y for (x, y) in itertools.product(divisors[a], divisors[b])]))

for i in range(1,length):
	small = i if i%2!=0 else i/2
	big = i+1 if (i+1)%2!=0 else (i+1)/2
	total = len(divisors[small]) * len(divisors[big])
	if (total)>500:
		print small,big,total
		break




