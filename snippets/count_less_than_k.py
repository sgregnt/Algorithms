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
