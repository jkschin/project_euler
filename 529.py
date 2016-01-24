
def check_substring(digits_list, window):
	original = window
	while window!=0:
		shift = 0
		count 
		for i in range(window):
			if sum(digits_list[i:window+shift])!=10:
				break
			if window+shift==original:
				break
			shift+=1
		window-=1
	return 1

def main():
	for i in range(100):
		digits_list = [int(char) for char in (str(i))]
		window = len(digits_list)

print check_substring([1,2,3,4,3,2,1],7)
