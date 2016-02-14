
f = open('67.txt','r')
pyramid = []
for line in f:
	pyramid.append([int(i) for i in line.split()])

for row_number in range(len(pyramid)-1):
	new_row = [-1000]
	for element_number in range(len(pyramid[row_number])):
		left = pyramid[row_number+1][element_number]
		new_left = left + pyramid[row_number][element_number]
		right = pyramid[row_number+1][element_number+1]
		new_right = right + pyramid[row_number][element_number]
		new_row[-1]=max(new_row[-1],new_left)
		new_row.append(new_right)
	pyramid[row_number+1] = new_row

for i in pyramid:
	print max(i)
