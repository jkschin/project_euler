def alphabet_value(letter):
	return ord(letter)-96

multiplier = 1
total = 0 
f = open('22.txt','r')
names = sorted(f.read().split(','))
for name in names:
	name = name.lower().strip('"')
	total += sum([alphabet_value(letter) for letter in name])*multiplier
	multiplier += 1
print total

