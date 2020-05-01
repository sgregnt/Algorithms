# Given a 2D binary matrix filled with 0's and 1's,
# find the largest square containing only 1's and return its area.


#==========================================
#  Slow implementation
#==========================================

# Input:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# Output: 4


# dynamic programming
# examine bottom right corner and width
# start by scanning according to width
# from 1 to n, keep previous width and next width.
#
# cur_width[row][col] = if num[row][col] == 1 and
# prev_width[row-1][col-1] and prev_width[row][col-1] and prev_width[row-1][col]
#

matrix =  [[1, 1, 1, 0, 0],
           [1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1],
           [1, 0, 0, 1, 0]]

cur_dp = [x[:] for x in matrix]
prev_dp = [x[:] for x in matrix]

r_n = len(matrix)

if r_n == 0:
    print(0)

c_n = len(matrix[0])

if r_n == 1:
    print(max([int(d) for d in matrix[0]]))

n = min([r_n, c_n])
max_size = 0

for i in range(r_n):
    for j in range(c_n):
        if matrix[i][j] == '1':
            max_size = 1
r_n =  len(matrix)
c_n = len(matrix[0])
n = min([r_n, c_n])

max_size = 0

for w in range(1, n):
    prev_dp = [x[:] for x in cur_dp]
    for r in range(w, r_n):
        for c in range(w, c_n):
                if prev_dp[r-1][c-1] == 1 and matrix[r][c] == 1 and prev_dp[r-1][c] == 1 and prev_dp[r][c-1] == 1:
                    cur_dp[r][c] = 1
                    max_size = max([max_size, w+1])
                else:
                    cur_dp[r][c] = 0

print(max_size)


#==========================================
#  Faster implementation
#==========================================

matrix =  [[0, 1, 1, 0, 0],
           [1, 1, 1, 1, 1],
           [1, 1, 1, 1, 1],
           [1, 0, 0, 1, 0]]

matrix = [[1,0,1,1,0,1],
          [1,1,1,1,1,1],
          [0,1,1,0,1,1],
          [1,1,1,0,1,0],
          [0,1,1,1,1,1],
          [1,1,0,1,1,1]]


cur_dp = [x[:] for x in matrix]
prev_dp = [x[:] for x in matrix]

r_n = len(matrix)

if r_n == 0:
    print(0)

c_n = len(matrix[0])

if r_n == 1:
    print(max([int(d) for d in matrix[0]]))

n = min([r_n, c_n])
max_size = 0

for i in range(r_n):
    for j in range(c_n):
        if matrix[i][j] == '1':
            max_size = 1

if max_size == 0:
    print(0)

r_n =  len(matrix)
c_n = len(matrix[0])
n = min([r_n, c_n])

for r in range(1, r_n):
    for c in range(1, c_n):
            if matrix[r][c] == '1':
                cur_dp[r][c] = min([cur_dp[r-1][c-1], cur_dp[r-1][c], cur_dp[r][c-1]]) + 1
                if cur_dp[r][c] > max_size:
                    max_size = cur_dp[r][c]

print(max_size)

