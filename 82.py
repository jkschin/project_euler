import numpy as np

f = open('82.txt')
matrix = np.zeros((80, 80))
for idx, line in enumerate(f):
    matrix[idx, :] = [int(i) for i in line.split(',')]

memo = np.zeros((80, 80, 80))
for col in xrange(80):
    for start_idx in xrange(80):
        memo[start_idx, start_idx, col] = matrix[start_idx, col]
        for i in xrange(start_idx-1, -1, -1):
            memo[start_idx, i, col] += memo[start_idx, i+1, col] + \
                    matrix[i, col]
        for j in xrange(start_idx+1, 80, 1):
            memo[start_idx, j, col] += memo[start_idx, j-1, col] + \
                    matrix[j, col]

    if col != 0:
        updates = np.zeros((80))
        for right_idx in xrange(80):
            min_matrix = np.zeros((80, 80))
            for left_idx in xrange(80):
                min_matrix[:, left_idx] = matrix[:, col-1] + \
                        memo[right_idx, :, col]
            updates[right_idx] = np.min(min_matrix)
        matrix[:, col] = updates
print np.min(matrix[:, -1])
