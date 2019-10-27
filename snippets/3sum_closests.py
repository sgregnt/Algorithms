class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        diff = float('inf')
        flag = True
        i = 0
        while i < n - 2:

            left = i + 1
            right = n - 1

            while left < right:
                num = nums[left] + nums[right] + nums[i]
                diff_c = abs(num - target)

                if diff_c == 0:
                    return num

                if diff_c < diff:
                    diff = diff_c
                    sum_res = num

                if num > target:
                    right -= 1

                if num < target:
                    left += 1


            i += 1

            if nums[i - 1] == nums[i]:
                while i < n - 2 and nums[i - 1] == nums[i]:
                    i += 1

        return sum_res

a = Solution()
res = a.threeSumClosest([1,2,4,8,16,32,64,128], 82)
print(res)