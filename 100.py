u = 10
v = 7
x=3
y=4

while(y<1000000000000):
	new_u = 3*u+4*v
	new_v = 2*u+3*v
	u = new_u
	v = new_v
	x = (u+2)//4
	y = (v+1)//2
print (x,y)
