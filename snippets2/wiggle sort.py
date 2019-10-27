
nums = [3,5,2,1,6,4]

nums.sort()
middle = int(len(nums) / 2)
nums[::2], nums[1::2] = nums[middle:], nums[:middle]
print(nums)
# print(nums[1::2])
# print(middle, nums[:middle])


a = nums[:]
print(a[1:3:1])