import bisect


class Solution(object):
    def nextPermutation(self, nums):
        #         """
        #         :type nums: List[int]
        #         :rtype: None Do not return anything, modify nums in-place instead.
        #         """

        #         if not nums:
        #             return []

        #         n = len(nums)
        #         max_so_far = nums[0]

        #         for j in range(n):
        #             max_so_far = nums[0]
        #             for i in range(n-j):
        #                 if max_so_far < num[i]:
        #                     max_so_far = num[i]
        #                     index = i

        #             if nums[n-j] != max_so_far:

        #         nums = list(reversed(nums))
        #         return nums
        def reverse(alist, left, right):
            # intializing pointers
            # left = 0
            # right = len(alist) - 1

            # condition for termination
            while left < right:
                # swapping
                temp = alist[left]
                alist[left] = alist[right]
                alist[right] = temp

                # updating pointers
                left += 1
                right -= 1

            return alist


        n = len(nums)
        i = n - 2

        while i > -1:
            if nums[i + 1] > nums[i]:
                break
            else:
                i -= 1

        if i == -1:
            reverse(nums, 0, len(nums)-1)
        else:
            pivot = nums[i]
            swap_ind1 = i

            stil_large = float('inf')

            # can do bisection

            j = len(nums)
            while j > i:
                j -= 1
                if nums[j] > pivot and nums[j] < stil_large:
                    stil_large = nums[j]
                    swap_ind2 = j

            nums[swap_ind1], nums[swap_ind2] = nums[swap_ind2], nums[swap_ind1]
            reverse(nums, swap_ind1+1, len(nums) - 1)


a = Solution()
b = [2,3,1,3,3]
a.nextPermutation(b)
print(b)
