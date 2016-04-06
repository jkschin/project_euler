def logic(x,y,z,p):
	if (x**2 + y**2)!=z**2:
		return False
	if (x+y+z)!=p:
		return False
	if x==0 or y==0 or z==0:
		return False
	if x<0 or y<0 or z<0:
		return False
	return True

def count_solutions_given_p(p):
	count = 0
	lhs = p**2/2
	for x in range(1,p):
		if (lhs%(x-p))==0:
			y = lhs/(x-p) + p
			z = p - x - y
			if logic(x,y,z,p):
				count += 1
	return count/2

def main():
	max_val = 0
	max_ptr = 0
	for i in range(1,1000):
		val = count_solutions_given_p(i)
		if val >= max_val:
			max_val = val
			max_ptr = i
	return max_ptr, max_val

print (main())
