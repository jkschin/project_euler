
i = 1
concat = ""
while True:
	concat += str(i)
	i += 1
	if len(concat)>=1000000:
		break
i = 1
count = 1
while True:
	count *= int(concat[i-1])
	if i==1000000:
		break
	i *= 10
print count
