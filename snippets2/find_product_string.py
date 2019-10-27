import math
import bisect

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        if k == 0: return 0
        k = math.log(k)

        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + math.log(x))

        ans = 0
        for i, x in enumerate(prefix):
            j = bisect.bisect(prefix, x + k - 1e-9)
            s_len = j - i - 1
            if s_len > 0:
                ans += s_len
        return ans

a = Solution()

print(a.numSubarrayProductLessThanK([1,1,1], 1))
