#Leetcode 31. Next Permuation
#Implement next permutation, which rearranges numbers into the lexicographically next greater #permutation of numbers.

#If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

#The replacement must be in-place and use only constant extra memory.

#Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

#1,2,3 → 1,3,2
#3,2,1 → 1,2,3
#1,1,5 → 1,5,1


import bisect

class Solution(object):
    def nextPermutation(self, nums):
       
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
