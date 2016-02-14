def is_abundant(n):
	return sum([i if n%i==0 else 0 for i in range(1,n/2+1)])>n

abundant_numbers = []
total = 0
for i in range(1,28123+1):
	abundant_numbers.append(i) if is_abundant(i) else 0
abundant_number_sums = {}
for x in abundant_numbers:
	for y in abundant_numbers:
		if x+y>28123:
			break
		if x+y not in abundant_number_sums:
			abundant_number_sums[x+y] = 1
for j in range(1,28123+1):
	if j not in abundant_number_sums:
		total+=j
print total

# abundant_number_sums = list(set([x*y for x in abundant_numbers for y in abundant_numbers]))


