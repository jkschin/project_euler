
def factorial(n):
	if n == 0:
		return 1
	return reduce(lambda x, y: x*y, [i for i in range(1, n+1)])

def combinations(n, r):
	return factorial(n)/factorial(r)/factorial(n-r)

def problem_53():
	count = 0
	for n in range(1, 101):
		for r in range(0, n+1):
			if combinations(n, r) >= 1000000:
				count += 1
	return count
print problem_53()