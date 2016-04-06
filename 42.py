dic = dict(zip([chr(i) for i in range(65,65+26)],[i for i in range(1,1+26)]))

def generate_triangle_numbers():
	tri = [1]
	for i in range(2,1000):
		tri.append(tri[-1]+i)
	return tri

def get_word_value(word):
	return sum([dic[char] for char in list(word)])

tri = generate_triangle_numbers()


f = open("42.txt", "r")
count = 0
words = [word.strip("\"") for word in f.read().split(",")]
for word in words:
	if get_word_value(word) in tri:
		count += 1
print count
