#-------------------------------------
# Array journey
#-------------------------------------

nums = [10, 2, -10, 5, 20, 10, -1, -50, 1]
n = len(nums)
k = 2
dp = [0] * n

dp[-1] = nums[-1]

for i in reversed(range(n-1)):
    dp[i] = nums[i] + max(dp[i+j] for j in range(1, k+1) if i+j < n)

print(dp[0])