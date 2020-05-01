from collections import Counter


class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        memory = {}
        self.q = Counter(nums)

        self.max = -float('inf')

        def rec(sum_total):

            flag = False
            if not self.q:
                if sum_total > self.max:
                    self.max = sum_total

            else:

                for elem in self.q:
                    self.q[elem] -= 1
                    if self.q[elem] == 0:
                        flag = True
                        del self.q[elem]

                    sum_total += elem

                    elem_plus = elem + 1
                    elem_minus = elem - 1
                    elem_plus_val = self.q[elem_plus]
                    elem_minus_val = self.q[elem_minus]

                    del self.q[elem_plus]
                    del self.q[elem_minus]

                    rec(sum_total)

                    self.q[elem_plus] = elem_plus_val
                    self.q[elem_minus] = elem_minus_val

                    if  flag:
                        self.q[elem] = 1
                    else:
                        flag = False
                        self.q[elem] += 1

        rec(0)
        return self.max

a = Solution()
print(a.deleteAndEarn([3,4,2]))