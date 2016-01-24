i = 2
n = 600851475143
cur = 0

while (i*i)<n:
	while n%i==0:
		n=n/i
	i+=1
print n