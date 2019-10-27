nums = [0, 2]

n = len(nums)
dp = [[0] * n for _ in range(n)]
for i in range(n):
    dp[i][i] = nums[i]

res = nums[0]
for i in range(1, n):
    for j in range(i+1):
        if i != j:
            dp[j][i] = dp[j][i - 1] * nums[i]
        if dp[j][i] > res:
            res = dp[j][i]

print(res)