class Solution(object):

    def permute(self, nums):

        def permute_r(nums):
            if len(nums) == 1:
                return [nums]

            n = len(nums)
            c_res = []
            for i in range(n):

                new = permute_r(nums[:i] + nums[i+1:])
                c = [nums[i]]

                for c_new in new:
                    c_res.append(c + c_new)

            return c_res

        return permute_r(nums)

a = Solution()
print(a.permute([1,2,3]))