import numpy as np
import gmpy

f = open("13.txt","r")

total = 0
count = 1
for line in f:
	total += gmpy.mpz(line)
	print count 
	count += 1
print total