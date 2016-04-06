


def check_pandigital(n):
	i, concat = 1, ""
	while True:
		concat += str(i*n)
		i += 1
		if len(concat)==9:
			return concat
		elif len(concat)>9:
			return False

def main():
	for i in range(9999):
		concat = check_pandigital(i)
		if concat and len(set(list(concat.replace("0",""))))==9:
			print i, concat

main()
			

