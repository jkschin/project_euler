import itertools
from fractions import Fraction
import euler


def extract_common_number(n1,n2):
	numbers_to_remove = list(itertools.chain.from_iterable([[i if i==j else "-1" for i in str(n1)] for j in str(n2)]))
	return [[int(str(n1).replace(number,"",1)), int(str(n2).replace(number,"",1))] if number!="-1" and number!="0" else [-1] for number in numbers_to_remove]

def main():
	fractions = []
	for i in range(10,100):
		for j in range(i+1,100):
			extracted_numbers = extract_common_number(i,j)
			for pair in extracted_numbers:
				if len(pair)==2:
					x, y = pair
					try:
						if Fraction(i,j)==Fraction(x,y):
							fractions.append(Fraction(i,j))
					except ZeroDivisionError:
						pass
	print euler.multiply_list(fractions)
