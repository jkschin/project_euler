import math
import numpy as np

f = open("99.txt","r")
magnitudes = []
for line in f.readlines():
	line = line.strip("\n").split(",")
	base = int(line[0])
	exp = int(line[1])
	magnitude = math.log(base) * exp
	magnitudes.append(magnitude)
magnitudes = np.array(magnitudes)
print np.argmax(magnitudes)

