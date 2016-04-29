import euler

sieve = euler.sieve_of_eratosthenes(1000000)
sieve_dic = euler.list_to_dic(sieve)

def longest_sum(base_ptr, num_terms):
	return sum([sieve[i+base_ptr] for i in range(num_terms)])

def longest_sum_given_num_term(num_terms):
	base_ptr = 0
	max_val = 0
	while(True):
		s = longest_sum(base_ptr, num_terms)
		print (s)
		if s >= 100 and base_ptr == 0:
			return -1
		if s >= 100:
			break
		if s >= max_val and s in sieve_dic:
			max_val = s
		base_ptr += 1
	return max_val

def main():
	num_terms = 2
	max_val = 0
	max_terms = 2
	while(True):
		s = longest_sum_given_num_term(num_terms)
		if s == -1:
			break
		if num_terms >= max_terms:
			max_val = s
			max_terms = num_terms
		num_terms += 1
	print max_val, max_terms
main()


# def main():
# 	num_terms = 2
# 	while(True):
# 		base_ptr = 0
# 		while (True):
# 			s = longest_sum(base_ptr,num_terms)
# 			if s >= 100 and base_ptr == 0:
# 				break
# 			if s in sieve_dic and s >= max_val:
# 				max_val = s
# 			base_ptr += 1
# 		num_terms += 1
# 	return s

# print main()



