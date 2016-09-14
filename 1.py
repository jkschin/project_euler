# There are elegant solutions like binary stuff, but this question
# is simple enough and does not require speed.

# ans = []
# for i in range(1,1000):
# 	if i%3==0 or i%5==0:
# 		ans.append(i)
# print (sum(ans))
print sum([i if (i%3==0 or i%5==0) else 0 for i in range(1,1000)])
