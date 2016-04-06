import itertools

#1, 4
#2, 3
def get_permutations(elements, r):
	return [int("".join(list(i))) for i in list(itertools.permutations(elements,r))]

def find_pandigital(n1, n2):
	products = []
	n1_list = get_permutations("123456789", n1)
	n2_list = get_permutations("123456789", n2)
	for i in n1_list:
		for j in n2_list:
			concat = str(i*j) + str(i) + str(j)
			if len(set(concat.replace("0","")))==9 and len(concat)==9:
				products.append(i*j)
	return products

products = find_pandigital(1,4) + find_pandigital(2,3)
print sum(list(set(products)))
