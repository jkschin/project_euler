import euler

n = 1000000

def main():
	total = 0
	for i in range(1,n):
		if euler.check_palindrome(str(i)) and euler.check_palindrome(bin(i)[2:]):
			total += i
	return total
			
print main()