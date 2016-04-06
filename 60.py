import itertools
from numba import jit
from euler import *

sieve = sieve_of_eratosthenes(100000000)
sieve.remove(2)
sieve.remove(5)
sieve_dic = list_to_dic(sieve)


def check_prime(a,b):
	return (int(a+b) in sieve_dic and int(b+a) in sieve_dic)

def check_queue(queue,dic,n):
	for i in queue:
		if n not in dic[i]:
			return False
	return True

def get_dictionary():
	a = itertools.combinations(sieve_of_eratosthenes(10000), 2)
	dic = {}
	count = 0
	while(True):
		try:
			p1, p2 = a.next()
			if check_prime(str(p1),str(p2)):
				if p1 not in dic:
					dic[p1] = [p2]  
				else: 
					dic[p1].append(p2)
				count += 1
		except StopIteration:
			break
	return dic

def recurse(queue, dic):
	if len(queue)==5:
		return queue
	for prime in dic[queue[-1]]:
		if check_queue(queue,dic,prime):
			queue.append(prime)
			return recurse(queue,dic)

def main():
	print ("Building Dictionary")
	dic = get_dictionary()
	print ("Searching for answer")
	for prime in sieve:
		queue = [prime]
		if prime in dic:
			a = recurse(queue, dic)
			if a:
				break
	print (a)

main()
			
# for prime in sieve:
	# queue.append(prime)




# print (dic)


	