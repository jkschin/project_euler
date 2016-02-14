import math
from fractions import Fraction


mod_inverses = []
H = {}

p = 7

def extendedEuclidean(a,n):
	t = 0
	r = n
	newt = 1
	newr = a
	while newr!=0:
		quotient = r/newr
		t,newt = newt, t - quotient * newt
		r,newr = newr, r - quotient * newr
	if r>1:
		return -1
	if t<0:
		t = t+n
	return t

def reduceModP(frac,p):
	return Fraction(frac.numerator%p,frac.denominator%p)

def fractionToModP(frac,p):
	numerator = frac.numerator % p 
	denominator = frac.denominator % p
	inv = mod_inverses[denominator]
	if denominator==0:
		return -1
	else:
		return (numerator*inv)%p

def Harmonic(n):
	frac = Fraction(0)
	for i in range(1,n):
		frac += Fraction(1,i)
	return frac

def populateModInverse(p,psquare):
	for n in range(0,psquare):
		mod_inverses.append(extendedEuclidean(n,psquare))

def getCongruences(p):
	for i in range(p):
		index = fractionToModP(harmonic_sums[i],p)
		if index not in congruences:
			congruences[index] = [i]
		else:
			congruences[index].append(i)

def HStar(n,p,t):
	q = n/(p**t)
	lower = (p**t)*q
	upper = n
	frac = Fraction(0)
	for i in range(lower+1,upper+1):
		if i%(p**t)!=0:
			frac += Fraction(1,i)
	return frac

def getPsi(index,p):
	return fractionToModP(H[index]*Fraction(1,p),p)

def Wolstenholme(p):
	frac = fractionToModP(Fraction(1,p**2)*H[6],p)
	return frac

def DFS(cur,p,psi,depth):
	if depth==5:
		return 0
	try:
		r_vals = congruences[(p-psi)%p]
	except KeyError:
		return 0
	for i in r_vals:
		new = cur*p + i
		if new==(p*(p-1)) or new==(p**2-1):
			W = Wolstenholme(p)
			psi = W
			H[new] = (p*W)%(p**2)
			print "TOP"
			print new, H[new], getPsi(new,p)
			DFS(new,p,psi,depth+1)
			J.append(new)
		else:
			H[new] = fractionToModP(HStar(new,p) + H[cur]*Fraction(1,p),p**2)
			psi = getPsi(new,p)
			print "BTM"
			print new, H[new], H[cur], getPsi(new,p)
			DFS(new,p,psi,depth+1)
			J.append(new)
		
# print HStar(295,7,2)
# H[6] = Fraction(49,20)
# populateHarmonicSums(p)
# populateModInverse(p,p**3)
# for i in range(295,300):
# 	print mod_inverses[i]
# populateCongruences(p)
# print congruences
# print HStar(295,p) + 42*Fraction(1,p)
# print Harmonic(42)
# congruences = {0:[0,6],1:[1,5],3:[2,4],5:[3]}
# print congruences
# print HStar(299,p)+6
# print fractionToModP(HStar(299,p) + 6,p**2)
# DFS(6,p,0,0)
# print sorted(J)

def adhoc():
	frac = Fraction(0)
	for k in range(1,6):
		frac += Fraction(294,k*(294+k))
	return frac+7

# populateModInverse(p,p**6)

# print fractionToModP(adhoc(),343)

