
# IO routine

def parse():
    f = open('81.txt')
    matrix = []
    for line in f:
        matrix.append([int(i) for i in line.split(',')])
    return matrix

matrix = parse()
memo = [[0 for i in xrange(80)] for j in xrange(80)]
memo[0][0] = matrix[0][0]
for i in xrange(1, 80):
    memo[0][i] += (memo[0][i-1] + matrix[0][i])
    memo[i][0] += (memo[i-1][0] + matrix[i][0])

for i in xrange(1, 80):
    for j in xrange(1, 80):
        if memo[i][j] == 0:
            shortest = min(memo[i][j-1], memo[i-1][j])
            memo[i][j] = matrix[i][j] + shortest
print memo[-1][-1]
