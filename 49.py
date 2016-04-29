import euler
import itertools

sieve = euler.sieve_of_eratosthenes(10000)
sieve_dic = euler.list_to_dic(sieve)

def check_permute(n1, n2):
	return sorted(list(str(n1)))==sorted(list(str(n2)))

for i in range(1487,10000,2):
	interval = 2
	while(True):
		if i+interval*2 >=10000:
			break
		if i not in sieve_dic:
			break
		l = [i+j*interval for j in range(0,3)]
		if (check_permute(l[0],l[1]) and check_permute(l[1],l[2])) and l[0] in sieve_dic and l[1] in sieve_dic and l[2] in sieve_dic:
			print i, interval
		interval += 1


