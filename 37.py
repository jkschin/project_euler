import euler

sieve = euler.list_to_dic(euler.sieve_of_eratosthenes(1000000))

def truncatable(n):
	return all([True if int(n[i:]) in sieve and int(n[0:len(n)-i]) in sieve else False for i in range(len(n))])

count = 0
total = 0
for prime in sieve.keys():
	if truncatable(str(prime)) and prime not in [2,3,5,7]:
		count += 1
		total += prime
	if count==11:
		break
print (total)




