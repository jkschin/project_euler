#Not an entirely correct solution, since I misunderstood one part.

import euler
import itertools

prime_max = 100000000
prime_family = 8

#assume the target is within prime_max
sieve_list = euler.sieve_of_eratosthenes(prime_max)
sieve_dic = euler.list_to_dic(sieve_list)

def get_combinations_iterator(n, r):
	return itertools.combinations(range(len(str(n))-1), r)

def get_digits_iterator(n, positions):
	n = list(reversed([i for i in str(n)]))
	for i in range(0, 10):
		for position in positions:
			n[position] = str(i)
		yield int("".join(list(reversed(n))))

def check_one_number(n):
	length = len(str(n))
	for i in range(1, length):
		combinations_iterator = get_combinations_iterator(n, i)
		while True:
			try:
				positions = [i+1 for i in list(combinations_iterator.next())]
				print positions
				digits_iterator = get_digits_iterator(n, positions)
				index = 0
				count = 0
				while True:
					try:
						test_number = digits_iterator.next()
						if len(str(test_number)) != length:
							continue
						if test_number in sieve_dic:
							print test_number
							count += 1
						index += 1
						if (index - count) == (10 - prime_family + 1):
							break
					except StopIteration:
						break
				if count == (prime_family):
					return n
			except StopIteration:
				break

for prime in sieve_list:
	print "Checking: ", prime
	answer = check_one_number(prime)
	if answer:
		print answer
		break




