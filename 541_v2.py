from fractions import Fraction

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

def getModInverses(p,upper):
	mod_inverses = []
	for n in range(0,upper):
		mod_inverses.append(extendedEuclidean(n,upper))
	return mod_inverses

# Example: HStar(294,299,7) gives 295,296,297,298,299
def HStar(lower,upper,p):
	frac = Fraction(0)
	for i in range(lower+1,upper+1):
		if i%p!=0:
			frac += Fraction(1,i)
	return frac

# Example: isReducible(299,7,2) gives 294.
# Example: isReducible(49,7,2) gives 49
def isReducible(n,p,power):
	if n<p**power:
		return -1
	else:
		quotient = n//p**power
		return quotient*p**power

def H(n,nbar,p,power,last_memo):
	right_term = memoize[nbar]*Fraction(1,p)
	lower = isReducible(n,p,power)
	if lower==-1:
		left_term = hstar_memoize[last_memo] + HStar(last_memo,n,p)
		hstar_memoize[n] = left_term
	else:
		left_term = HStar(lower,n,p)
	return left_term+right_term

def fractionToModP(frac,p):
	numerator = frac.numerator % p 
	denominator = frac.denominator % p
	inv = mod_inverses[denominator]
	if denominator==0:
		return -1
	else:
		return (numerator*inv)%p

def getCongruences(p):
	congruences = {}
	for i in range(p):
		index = fractionToModP(harmonic_sums[i],p)
		if index not in congruences:
			congruences[index] = [i]
		else:
			congruences[index].append(i)
	return congruences

def getHarmonicSums(p):
	harmonic_sums = []
	harmonic_sums.append(Fraction(0))
	for i in range(1,p):
		harmonic_sums.append(Fraction(1,i)+harmonic_sums[-1])
	return harmonic_sums

def getPsi(frac,p):
	frac*=Fraction(1,p)
	return fractionToModP(frac,p)

def DFS(n,nbar,p,depth,last_memo):
	print n,depth
	memoize[n] = H(n,nbar,p,depth,last_memo)
	last_memo = n
	psi = getPsi(memoize[n],p)
	try:
		r_vals = congruences[(p-psi)%p]	
	except KeyError:
		return 0
	for i in r_vals:
		new = n*p + i
		J.append(new)
		DFS(new,n,p,depth-1)
	
def BFS(FIFO):
	last = 0
	while (len(FIFO)!=0):
		node = FIFO.pop(0)
		n, nbar, p, depth = node.n, node.nbar, node.p, node.depth
		memoize[n] = H(n,nbar,p,depth,last)
		last = n
		psi = getPsi(memoize[n],p)
		print node, psi
		try:
			r_vals = congruences[(p-psi)%p]	
			for i in r_vals:
				new = n*p + i
				node = Node(new,n,p,depth-1,last)
				J.append(new)
				FIFO.append(node)
		except KeyError:
			pass

class Node:
	def __init__ (self,n,nbar,p,depth,last):
		self.n = n
		self.nbar = nbar
		self.p = p
		self.depth = depth
		self.last = last
	def __str__ (self):
		return "n:%d, nBar:%d, p:%d, depth:%d, last:%d" % (self.n,self.nbar,self.p,self.depth,self.last)

J = [0]
memoize = {0:0}
hstar_memoize = {0:0}
last = 0
p = 137
depth = 8
harmonic_sums = getHarmonicSums(p)
print "Populating Mod Inverses..."
mod_inverses = getModInverses(p,p)
congruences = getCongruences(p)
FIFO = []
for i in range(1,len(harmonic_sums)):
	if harmonic_sums[i].numerator%p==0: 
		node = Node(i,0,p,depth,last)
		J.append(i)
		FIFO.append(node)
		# DFS(i,0,p,depth,last_memo)
BFS(FIFO)
J = sorted(J)
print J
print J[-1]*p + p-1

