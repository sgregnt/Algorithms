from collections import Counter
class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        myd = Counter(s)
        outputs =  {}
        n = len(s)
        def back_tracking(left, comb):
            if len(comb) == n:
                if comb in outputs:
                    pass
                else:
                    outputs[comb] = True

            if len(comb) == n - 1:
                half = int(len(comb) / 2)
                for k in left.keys():
                    if left[k] == 1:
                        final_comb = comb[:half] + k + comb[half:]
                        break

                if final_comb in outputs:
                    pass
                else:
                    outputs[final_comb] = True

            for k in left.keys():
                if left[k] == 1:
                    continue
                else:
                    if left[k] > 0:
                        left[k] = left[k] - 2
                        back_tracking(left, k + comb + k)
                        left[k] = left[k] + 2

        back_tracking(myd, "")
        return outputs.keys()

a = Solution()
print(a.generatePalindromes("abbaqf"))


# time limit exceeded. How to solve this?