class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        a = nums
        prod = 1
        ll = 0
        rr = 0
        n = len(a)
        count = 0
        diff = 0

        for ll in range(n):

            if diff == 0:
                prod = a[ll]
                rr = ll

            while prod < k and rr < n:
                rr += 1
                if rr == n:
                    break
                prod = prod * a[rr]

            diff = rr - ll

            if diff == 0:
                pass
            else:
                count += diff
                prod = prod / a[ll]

        return count


a = Solution()
res = a.numSubarrayProductLessThanK([1,2,3], 0)
print(res)

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
