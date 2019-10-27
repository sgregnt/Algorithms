class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        n = len(nums)

        if n == 1:
            return nums[0]

        if n == 2:
            return max(nums)

        h = nums
        DP_plus = [0] * n
        DP_minus = [0] * n

        DP_plus[n - 1] = h[n - 1]
        DP_plus[n - 2] = h[n - 1]

        DP_minus[n - 1] = 0
        DP_minus[n - 2] = h[n - 2]

        for i in reversed(range(1, n - 1)):

            j = i - 1
            DP_minus[j] = max(h[j] + DP_minus[j + 2], DP_minus[j + 1])

            if j == 0:
                DP_plus[j] = DP_plus[1]
            else:
                DP_plus[j] = max(h[j] + DP_plus[j + 2], DP_plus[j + 1])

        max_total = max(DP_plus[0], DP_minus[0])

        return max_total

a = Solution()
print(a.rob([1,3,1,3,100]))