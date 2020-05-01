class Solution(object):

    def permuteUnique(self, nums):
        ans = [[]]
        for num in nums:
            new_ans = []
            for c in ans:
                for i in range(len(c) + 1):
                    new_ans.append(c[:i] + [num] + c[i:])
                    if i < len(c) and c[i] == num: break  # handles duplication
            ans = new_ans
        return ans

a = Solution()
print(a.permuteUnique([2,1, 1]))