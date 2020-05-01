
nums = [3,5,2,1,6,4]

nums.sort()
middle = int(len(nums) / 2)
nums[::2], nums[1::2] = nums[middle:], nums[:middle]
print(nums)
# print(nums[1::2])
# print(middle, nums[:middle])


a = nums[:]
print(a[1:3:1])


class Solution(object):
    def wiggleSort(self, nums):

        n = len(nums)
        smaller = True
        for i in range(1, n):
            if smaller:
                if nums[i-1] <= nums[i]:
                    smaller = not smaller
                else:
                    nums[i-1], nums[i] = nums[i], nums[i-1]
                    smaller = not smaller

            else:
                if nums[i-1] >= nums[i]:
                    smaller = not smaller
                else:
                    nums[i-1], nums[i] = nums[i], nums[i-1]
                    smaller = not smaller


        return nums
a = Solution()
print(a.wiggleSort([1,5,5,2,1,6,6,100]))

class Solution(object):
    def wiggleSort(self, nums):

        n = len(nums)
        smaller = True
        i = 1
        while i < n:
            if nums[i-1] == nums[i]:
                j = i
                while nums[i-1] == nums[j]:
                    j += 1
                nums[i], nums[j] = nums[j], nums[i]
                continue

            if smaller:
                if nums[i-1] <= nums[i]:
                    smaller = not smaller
                else:
                    nums[i-1], nums[i] = nums[i], nums[i-1]
                    smaller = not smaller

            else:
                if nums[i-1] >= nums[i]:
                    smaller = not smaller
                else:
                    nums[i-1], nums[i] = nums[i], nums[i-1]
                    smaller = not smaller
            i += 1

        return nums
a = Solution()
print(a.wiggleSort([1,5,5,2,1,6,6,100]))




