total = 0
init = [1,2]
while True:
	new = sum(init)
	if new>4000000:
		break
	if new%2==0:
		print new
		total+=new
	init.pop(0)
	init.append(new)
print (total+2)