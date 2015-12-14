import cProfile
import random


def generateRandomList():
	return [random.randint(0,10000) for _ in range(0,10000)]

def compare(x,n):
	return x<=n

def multiply(i,j):
	return i*j

def forLoopTest(a,b,n):
	ans = []
	for i in a:
		for j in b:
			x = multiply(i,j)
			if compare(x,n):
				y = multiply(i,j)
				ans.append(y)
			else:
				break
	return ans

def forLoopTest2(a,b):
	for i in a:
		print i
		for j in b:
			pass

def forLoopXRangeTest(a,b,n):
	ans = []
	for i in xrange(len(a)):
		for j in xrange(len(b)):
			x = multiply(a[i],b[j])
			if compare(x,n):
				y = multiply(a[i],b[j])
				ans.append(y)
			else:
				break
	return ans

#          300060008 function calls in 116.908 seconds

#    Ordered by: standard name

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000  116.908  116.908 <string>:1(<module>)
#     20000    0.033    0.000    0.035    0.000 random.py:175(randrange)
#     20000    0.010    0.000    0.045    0.000 random.py:238(randint)
# 200000000   28.604    0.000   28.604    0.000 test_forloop.py:11(multiply)
#         1   74.147   74.147  116.853  116.853 test_forloop.py:14(forLoopTest)
#         1    0.000    0.000  116.907  116.907 test_forloop.py:23(main)
#         2    0.009    0.004    0.055    0.027 test_forloop.py:5(generateRandomList)
# 100000000   14.102    0.000   14.102    0.000 test_forloop.py:8(compare)
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#     20000    0.002    0.000    0.002    0.000 {method 'random' of '_random.Random' objects}
#         2    0.000    0.000    0.000    0.000 {range}

def counterForLoopTest(a,b,n):
	a_counter=0
	b_counter=0
	count = 0
	ans = []
	while True:
		if a_counter==len(a):
			break
		x = multiply(a[a_counter],b[b_counter])
		if compare(x,n):
			y = multiply(a[a_counter],b[b_counter])
			ans.append(y)
			b_counter+=1
		else:
			a_counter+=1
			b_counter=0
		if b_counter==len(b):
			a_counter+=1
			b_counter=0
	return ans

# a = [1,2,3,4,5]
# b = [1,2,3,4,5]
# n = 9
# ans1 = counterForLoopTest(a,b,n)
# ans2 = forLoopTest(a,b,n)
# ans3 = forLoopXRangeTest(a,b,n)
# print ans1
# print ans2
# print ans3
# print ans1==ans2 and ans2==ans3

def main():
	a = generateRandomList()
	b = generateRandomList()
	n = 1000000000000
	# forLoopTest(a,b,n)
	forLoopTest2(a,b)

cProfile.run("main()")

  #        3006008 function calls in 1.178 seconds

  #  Ordered by: standard name

  #  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  #       1    0.000    0.000    1.178    1.178 <string>:1(<module>)
  #    2000    0.003    0.000    0.003    0.000 random.py:175(randrange)
  #    2000    0.001    0.000    0.005    0.000 random.py:238(randint)
  # 2000000    0.287    0.000    0.287    0.000 test_forloop.py:11(multiply)
  #       1    0.744    0.744    1.173    1.173 test_forloop.py:14(forLoopTest)
  #       2    0.001    0.000    0.005    0.003 test_forloop.py:5(generateRandomList)
  #       1    0.000    0.000    1.178    1.178 test_forloop.py:72(main)
  # 1000000    0.142    0.000    0.142    0.000 test_forloop.py:8(compare)
  #       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  #    2000    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}
  #       2    0.000    0.000    0.000    0.000 {range}

  #          3007009 function calls in 1.323 seconds

  #  Ordered by: standard name

  #  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  #       1    0.000    0.000    1.323    1.323 <string>:1(<module>)
  #    2000    0.003    0.000    0.003    0.000 random.py:175(randrange)
  #    2000    0.001    0.000    0.004    0.000 random.py:238(randint)
  # 2000000    0.287    0.000    0.287    0.000 test_forloop.py:11(multiply)
  #       1    0.888    0.888    1.318    1.318 test_forloop.py:23(forLoopXRangeTest)
  #       2    0.001    0.000    0.005    0.002 test_forloop.py:5(generateRandomList)
  #       1    0.000    0.000    1.323    1.323 test_forloop.py:73(main)
  # 1000000    0.143    0.000    0.143    0.000 test_forloop.py:8(compare)
  #    1001    0.000    0.000    0.000    0.000 {len}
  #       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  #    2000    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}
  #       2    0.000    0.000    0.000    0.000 {range}

