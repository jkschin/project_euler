def isPalindrome(n):
	n = str(n)
	for i in range(len(n)):
		if n[i]!=n[-i-1]:
			return False
	return True

def countDown(n):
	palindromes = []
	for i in range(n,0,-1):
		for j in range(n,0,-1):
			t = i*j
			if isPalindrome(t):
				palindromes.append(t)
	return max(palindromes)

print countDown(999)