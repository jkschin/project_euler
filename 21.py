
def d(n):
	return sum([i if n%i==0 else 0 for i in range(1,n/2+1)])

total = 0
list_of_d = [d(n) for n in range(0,10000)]
for i in range(len(list_of_d)):
	try:
		if list_of_d[list_of_d[i]]==i and list_of_d[list_of_d[i]]!=list_of_d[i]:
			total += i
	except IndexError:
		continue
print total
