from sympy.ntheory.primetest import isprime
from sympy.ntheory import totient
from sympy.ntheory import factorint
from sympy.core.numbers import ilcm, igcd
from sympy import sieve
from gmpy2 import mpz
import math
import cProfile
import re
import gmpy2
import numpy as np
import time

class Memory:
	def __init__(self,n):
		self.n = n
		self.unseen = mpz("0b"+("1"*(n-1))+"00")
		self.seen = mpz(0)
		self.prime = 0
		self.global_shift = 0
		self.totients = [i for i in range(0,n+1)]

	def updateUnseen(self):
		shift = gmpy2.bit_scan1(self.unseen)
		self.unseen = self.unseen>>shift
		self.prime = self.prime + shift
		self.global_shift+=shift

class BitIterator:
	def __init__(self,n):
		self.n = n
		self.global_shift = 0

	def next(self):
		shift = gmpy2.bit_scan1(self.n)
		if shift==None:
			return -1
		self.global_shift += shift
		self.n = self.n >> shift
		self.n = self.n.bit_flip(0)
		return self.global_shift
	
# m and n GCD = 1
def mn_phi(m,n,totients):
	a = totients[m]*totients[n]
	return a

# n is the totient to be found, p is the prime base of n
def pe_phi(n,p):
	return int(n*(1-1/float(p)))

# def buildExponents(memory):
# 	exponentiated_list = mpz(0)
# 	exponentiated = 1
# 	while True:
# 		exponentiated *= memory.prime
# 		if exponentiated <= memory.n:
# 			memory.totients[exponentiated] = pe_phi(exponentiated,memory.prime)
# 			exponentiated_list = exponentiated_list.bit_flip(exponentiated)
# 			memory.unseen = memory.unseen.bit_flip(exponentiated-memory.global_shift)
# 		else:
# 			break
# 	return exponentiated_list

# def buildSeenTimesExponent(memory,exponentiated_list_mpz):
# 	seen_times_exponentiated_list = mpz(0)
# 	seen = BitIterator(memory.seen)
# 	flag = False
# 	if seen.n==0:
# 		return seen_times_exponentiated_list
# 	while True:
# 		i = seen.next()
# 		exponentiated_list = BitIterator(exponentiated_list_mpz)
# 		count = 0
# 		while True:
# 			j = exponentiated_list.next()
# 			if j==-1:
# 				break
# 			ij = i*j
# 			if ij<=memory.n:
# 				memory.totients[ij] = mn_phi(i,j,memory.totients)
# 				seen_times_exponentiated_list = seen_times_exponentiated_list.bit_flip(ij)
# 				memory.unseen = memory.unseen.bit_flip(ij-memory.global_shift)
# 				count+=1
# 			else:
# 				if count==0:
# 					flag = True
# 				break
# 		if flag:
# 			break
# 	return seen_times_exponentiated_list

def generateTotients(n):
	print "Generating Totients"
	memory = Memory(n)
	while gmpy2.popcount(memory.unseen)!=0:
		# print bin(memory.unseen)
		memory.updateUnseen()
		exponentiated_list = buildExponents(memory)
		seen_times_exponentiated_list = buildSeenTimesExponent(memory,exponentiated_list)
		memory.seen |= (exponentiated_list|seen_times_exponentiated_list)
		# print bin(memory.seen)
	return memory.totients

def generateDots(n):
	print "Generating Dots"
	dots = [0]*(n+1)
	for i in range(1,n+1):
		dots[i]=(n-i)/i
	return dots

def multiplyTotientsAndDots(totients,dots):
	print "Multiplying Totients and Dots"
	dots = np.array(dots)
	lines = np.array(totients)
	res = np.multiply(dots,lines)
	res = np.sum(res)
	res = res*6
	return res

def correctTotients(n):
	totients = [0]*(n+1)
	for i in range(1,len(totients)):
		totients[i]=totient(i)
	return totients

def test(totients,n):
	print "Starting Test"
	a = totients
	b = correctTotients(n)
	if a==b:
		print "Pass!"
	for i in range(len(a)):
		if a[i]!=b[i]:
			print i,totient(i),a[i],b[i]
			print "Fail!"
			break

def main():
	# n = 1000
	# totients = generateTotients(n)
	# dots = generateDots(n)
	# res = multiplyTotientsAndDots(totients,dots)
	# print res
	# test(totients,n)
	cProfile.run("generateTotients(100000)")
	# test(totients,n)
	
	
	

main()
