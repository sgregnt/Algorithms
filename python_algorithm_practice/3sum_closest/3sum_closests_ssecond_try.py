class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        best_diff = float('inf')

        triple = (0,0,0)
        for end in range(2, n):
            i = 0
            j = end - 1
            while i < j:
                q = target - nums[i] - nums[j] - nums[end]
                if q == 0:
                    best_diff =0
                    triple = (i,j,end)
                    break

                if abs(q) < best_diff:
                    best_diff = abs(q)
                    triple = (i, j, end)

                    if q < 0:
                        j -= 1

                    if q > 0:
                        i += 1
                else:
                    if q > 0:
                        i += 1

                    if q < 0:
                        j -= 1

        i, j, end = triple
        return nums[i] + nums[j] + nums[end]

a = Solution()
# res = a.threeSumClosest([1,2,4,8,16,32,64,128], 82)
res = a.threeSumClosest([-1, 2, 1, -4], 1)
print(res)