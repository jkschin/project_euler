import math

fib = [1,1,2]

i = 3
while(len(str(fib[-1]))!=1000):
	fib.append(fib[-1]+fib[-2])
	i+=1
print (i)