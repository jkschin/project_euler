# import copy
# from numba import jit

# global count
# count = 0

# @jit
# def DFS(total, coins, stack):
# 	count = 0
# 	top = stack[-1]
# 	if total==200:
# 		return 1
# 	elif total<200:
# 		for coin in coins:
# 			if coin <= top:
# 				new_stack = copy.deepcopy(stack)
# 				new_stack.append(coin)
# 				count += DFS(total+coin, coins, new_stack)
# 	return count

# total = 0
# coins = [1, 2, 5, 10, 20, 50, 100, 200]
# for coin in coins:
# 	total += DFS(coin, coins, [coin])
# print (total)

# The above solution is inefficient. This is actually a DP problem.

# total = 200
# dic = dict(zip([i for i in range(201)],[1 if i==0 else 0 for i in range(201)]))
# coins = [1, 2, 5, 10, 20, 50, 100, 200]
# for coin in coins:
# 	for i in range(1,201):
# 		try:
# 			dic[i]+=dic[i-coin]
# 		except KeyError:
# 			pass
# print (dic[200])


#GOLF!
# dic = dict(zip([i for i in range(201)],[1 if i==0 else 0 for i in range(201)]))
# [[dic[i]+=1 if i-coin in dic.keys() else 0 for i in range(1,201)] for coin in [1, 2, 5, 10, 20, 50, 100, 200]]