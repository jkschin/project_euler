import itertools

def check_divisiblity(n):
	n = str(n)
	primes = [2, 3, 5, 7, 11, 13, 17]
	for i in range(1,8):
		if int(n[i:i+3])%primes[i-1]!=0:
			return False
	return True

pandigital_numbers = ["".join(n) for n in list(itertools.permutations("1234567890", 10))]

total = 0
for number in pandigital_numbers:
	if check_divisiblity(number):
		total += int(number)
print (total)

