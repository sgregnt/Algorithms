class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        count = [0] * 26
        a_ind = ord('a')
        for ch in p:
            ind = ord(ch) - a_ind
            count[ind] += 1

        n = len(s)
        n_p = len(p)

        compare_count = [0] * 26

        for ch in s[0:n_p]:
            ind = ord(ch) - a_ind
            compare_count[ind] += 1

        res = []
        if compare_count == count:
            res.append(0)

        for i in range(n_p, n):

            new_ch = s[i]
            oldest_ch = s[i - n_p]

            new_ch_ind = ord(new_ch) - a_ind
            oldest_ch_ind = ord(oldest_ch) - a_ind

            compare_count[oldest_ch_ind] -= 1
            compare_count[new_ch_ind] += 1

            if compare_count == count:
                res.append(i - n_p + 1)
        return res

a = Solution()
res = a.findAnagrams("cbaebabacd", "abc")
print(res)
