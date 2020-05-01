# Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.
#
# Formally the function should:
#
#     Return true if there exists i, j, k
#     such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
#
# Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

nums = [2, 7, 1, 6, 4, 5]


def increasingTriplet(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """

    n = len(nums)
    if n < 3:
        return False

    max_so_far = nums[-1]
    max_to_the_right = [nums[-1]] * n
    min_to_the_left = [nums[0]] * n

    for i in reversed(range(n - 1)):
        if nums[i] > max_to_the_right[i + 1]:
            max_to_the_right[i] = nums[i]
        else:
            max_to_the_right[i] = max_to_the_right[i + 1]

    for i in range(1, n):
        if nums[i] < min_to_the_left[i - 1]:
            min_to_the_left[i] = nums[i]
        else:
            min_to_the_left[i] = min_to_the_left[i - 1]

    for i in range(n):
        if min_to_the_left[i] < nums[i] and nums[i] < max_to_the_right[i]:
            return True

    return False

print(increasingTriplet(nums))


nums =  [5,0,9,9,1,1,1,1,8]
def increasingTriplet(nums):
    first = second = float('inf')
    for n in nums:
        if n <= first:
            first = n
        elif n <= second:
            second = n
        else:
            return True
    return False

print(increasingTriplet(nums))

#==========================================
# general approach to increasing sequence
#==========================================

# find the smallest integer to the left
# find the second smalelst integer to the left
# find the third smallest integer to the left and so on


nums =  [5,1,9,9,0,0,0,10,8]
min1 = nums[0]
min2 = float('inf')
min3 = float('inf')

n = len(nums)
for i in range(1, n):

    # the smallest number to the left
    if nums[i] < min1:
        min1 = nums[i]

    # the second smallest to the left
    if nums[i] > min1 and min2 > nums[i]:
        min2 = nums[i]

    # the second smallest to the left
    if nums[i] > min2 and min3 > nums[i]:
        min3 = nums[i]

    if nums[i] > min2:
        print("True")
        1/0
        break


