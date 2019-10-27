class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        nums = A
        k = K
        if not nums:
            return []

        n = len(nums)

        if n == 1:
            if nums[0] % k == 0:
                return nums

        integral = [0] * (n + 1)
        integral[0] = 0

        # compute running sum
        for i in range(1, n + 1):
            integral[i] = integral[i - 1] + nums[i-1]

        my_hash = {}

        # build lookup table to find
        # values that complete the some to multiple of k
        for i in range(1, n + 1):
            if integral[i] % k in my_hash:
                my_hash[integral[i] % k].append(i)
            else:
                my_hash[integral[i] % k] = [i]

        results = []

        for i, elem in enumerate(integral):
            if (elem % k) in my_hash:
                for counterpart in my_hash[elem % k]:
                    if counterpart > i:
                        results.append(nums[i:counterpart])

        print(results)
        return len(results)

a = Solution()
print(a.subarraysDivByK([0, 0, 0, 2,-3,1], 2))