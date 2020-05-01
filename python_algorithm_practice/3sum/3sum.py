from collections import Counter as mydict

class Solution(object):
    def threeSum(self, nums):

        nums_s = sorted(nums)

        i = j = k = 0
        n = len(nums)
        res = []
        prev_a = - float("inf")
        prev_b = - float("inf")
        prev_c = - float("inf")

        for k in reversed(range(n)):

            i = 0
            j = k-1
            q = nums_s[k]
            if q == prev_a:
                continue
            prev_a = q

            while i < j:

                if nums_s[i] + nums_s[j] + q == 0:
                    res.append([nums_s[i], nums_s[j], q])
                    prev_num = nums_s[j]
                    while nums_s[j] == prev_num and j > i:
                        j = j - 1
                else:
                    if nums_s[i] + nums_s[j] + q > 0:
                        prev_num = nums_s[j]
                        while nums_s[j] == prev_num  and j > 0:
                            j = j - 1
                    else:
                        if nums_s[i] + nums_s[j] + q < 0:
                            prev_num = nums_s[i]
                            while nums_s[i] == prev_num and i < j:
                                i = i + 1

        return res

a = Solution()
print(a.threeSum([0, 0, 0]))