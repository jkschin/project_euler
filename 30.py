n = 5
dic = dict(zip([i for i in range(10)],[i**n for i in range(10)]))

count = 0
for i in range(199999):
	if sum([dic[int(j)] for j in list(str(i))])==i:
		count += i
print (count-1)
