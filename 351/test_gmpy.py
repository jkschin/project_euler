import gmpy2
import random
from gmpy2 import mpz
from gmpy2 import mpz_random
import time

def profileLSB():
	start = time.time()
	for i in range(0,100):
		print bin(i)
		print gmpy2.bit_scan1(mpz(i))
	end = time.time()
	print end-start

def profileSetBit():
	start = time.time()
	x = mpz_random(gmpy2.random_state(0),100000000)
	for i in range(1000):
		x = x.bit_set(random.randint(0,100000000))
	end = time.time()
	print end-start

def profileCountSetBits():
	start = time.time()
	x = mpz("0xFFFFFFFF298123987123982FFF")
	for i in range(1000000):
		gmpy2.popcount(x)
	end = time.time()
	print end-start

def testShift():
	x = mpz(100)
	print (bin(x))
	x = x >> 2
	print (bin(x))

def createMPZ(n):
	x = mpz("0b"+("1"*(n-1))+"00")
	print bin(x)

# testShift()
# profileCountSetBits()
# profileLSB()
# profileSetBit()
mpz("0b"+"1"*100000000)

# 100 000 000 takes 33.43 seconds