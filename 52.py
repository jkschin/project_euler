import euler

def problem_52():
	i = 1
	while True:
		base = euler.count_unique_digits(i)
		for j in range(2, 7):
			comp = euler.count_unique_digits(i * j)
			print comp
			if base != comp:
				break
			if j == 6:
				return i
		i += 1