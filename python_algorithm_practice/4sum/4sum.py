class Solution(object):
    def fourSum(self, nums, target):

        nums.sort()
        n = len(nums)

        i1 = 0
        i2 = 0
        i3 = 0
        i4 = 0
        res = []

        while i1 < n-3:

            if i1 > 0 and nums[i1 - 1] == nums[i1]:
                i1 += 1
                continue

            t = target - nums[i1]
            i2 = i1 + 1

            while i2 < n-2:
                if i2 > i1 + 1 and nums[i2-1] == nums[i2]:
                    i2 += 1
                    continue
                else:

                    i3 = i2 + 1
                    i4 = n-1

                    while i3 < i4:
                        if i3 > i2 + 1 and nums[i3-1] == nums[i3]:
                            i3 += 1
                            continue
                        else:
                            if nums[i2] + nums[i3] + nums[i4] == t:
                                res.append([nums[i1], nums[i2], nums[i3], nums[i4]])
                                i3 += 1
                            else:
                                if nums[i2] + nums[i3] + nums[i4] > t:
                                    i4 -= 1
                                else:
                                    i3 += 1

                    i2 += 1
            i1 += 1

        return res

a = Solution()
# res = a.fourSum([1,0,-1,0,-2,2], 0)
res = a.fourSum([0, 0, 0, 0, 0, 0, 1, -1], 0)
print(res)