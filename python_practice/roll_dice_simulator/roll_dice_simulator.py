#-------------------------------------
# Roll dice simulator
#-------------------------------------


class Solution(object):
    def dieSimulator(self, n, rollMax):
        """
        :type n: int
        :type rollMax: List[int]
        :rtype: int
        """

        dp = [[0] * x for x in rollMax]

        # initialize dp
        for k in range(6):
            dp[k][0] = 1
        for k in range(1, n):
            next_dp = [[0] * n for n in rollMax]
            roll_sum = [sum(x) for x in dp]
            total = sum(roll_sum)
            for i in range(6):
                for j in range(rollMax[i]):
                    if j == 0:
                        next_dp[i][j] = total - roll_sum[i] % (10 ** 9 + 7)
                    else:
                        next_dp[i][j] = dp[i][j - 1] % (10 ** 9 + 7)
            dp = next_dp
        return sum([sum(x) for x in dp]) % (10 ** 9 + 7)


#-----------------------------------------
# Dice roll simulation
#-----------------------------------------

if False:
    n = 2
    rollMax = [1,1,1,1,1,1]

    n = 2
    rollMax = [1,1,2,2,2,3]

    n = 5000
    rollMax = [13,3,12,14,11,11]


    import numpy as np
    dp = [ [[0] * rollMax[i] for i in range(6)] for _ in range(n)]
    dp = np.array(dp)

    for i in range(6):
        dp[n-1][i][0] = 1

    for roll in reversed(range(n-1)):
        for i in range(6):
            dp[roll][i][0] = (np.sum(np.sum(dp[roll + 1]))- np.sum(np.sum(dp[roll + 1][i][:]))) % (10**9 + 7)
            for k in range(1, rollMax[i]):
                dp[roll][i][k] = dp[roll+1][i][k-1] % (10**9 + 7)

    print(np.sum(np.sum(dp[0])) % (10**9 + 7))


#-----------------------------------------
# Even faster
#-----------------------------------------

if False:
    n = 2
    rollMax = [1,1,1,1,1,1]
    n = 5000
    rollMax = [13,3,12,14,11,11]


    import numpy as np
    m = max(rollMax)
    dp = [ [0] * m * 6  for _ in range(n)]
    dp = np.array(dp)

    for i in range(6):
        dp[n-1][i * m] = 1

    for roll in reversed(range(n-1)):
        for i in range(6):
            dp[roll][i * m] = (np.sum(dp[roll + 1]) - np.sum(dp[roll + 1][i * m: i * m + m])) % (10**9 + 7)
            for k in range(1, rollMax[i]):
                dp[roll][i * m + k] = dp[roll+1][i * m + k -1] % (10**9 + 7)

    print(np.sum(dp[0]) % (10**9 + 7))


#-----------------------------------------
# Even faster than faster
#-----------------------------------------

class Solution(object):
    def dieSimulator(self, n, rollMax):
        m = max(rollMax)
        dp = [[0] * m * 6 for _ in range(n)]
        # dp = np.array(dp)

        for i in range(6):
            dp[n - 1][i * m] = 1

        for roll in reversed(range(n - 1)):
            for i in range(6):
                dp[roll][i * m] = (sum(dp[roll + 1]) - sum(dp[roll + 1][i * m: i * m + m])) % (10 ** 9 + 7)
                for k in range(1, rollMax[i]):
                    dp[roll][i * m + k] = dp[roll + 1][i * m + k - 1] % (10 ** 9 + 7)

        return sum(dp[0]) % (10 ** 9 + 7)
