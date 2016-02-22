import itertools
import gmpy


dic = {}
f = open("98.txt","r").read()
f = f.split(",")
for word in f:
	key = "".join(sorted(word[1:-1]))
	if key not in dic:
		dic[key] = [word[1:-1]]
	else:
		dic[key].append(word[1:-1])

words = []
for key in dic.keys():
	if len(dic[key])==2:
		words.append(dic[key])
	elif len(dic[key])>=3:
		comb = itertools.combinations(dic[key],2)
		while (1):
			try:
				words.append(list(comb.next()))
			except StopIteration:
				break

for word_pair in words:
	word0, word1 = word_pair
	a = itertools.permutations([1,2,3,4,5,6,7,8,9], len(word0))
	print word_pair
	while(1):
		try:
			numbers = list(a.next())
			dic = dict(zip(sorted(word0),numbers))
			number0 = int("".join([str(dic[i]) for i in word0]))
			if gmpy.is_square(number0):
				number1 = int("".join([str(dic[i]) for i in word1]))
				if gmpy.is_square(number1):
					print number0, number1
		except StopIteration:
			break


