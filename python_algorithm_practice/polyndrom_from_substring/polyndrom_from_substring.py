# ----------------------------
# I didn;t noticed you could rearrange the string!
# ----------------------------

class Solution(object):
    def canMakePaliQueries(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[bool]
        """

        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] == 0

        for i in range(1, n):
            for j in range(i):
                if i - j == 1:
                    if s[i] != s[j]:
                        dp[i][j] = 1
                else:
                    if s[i] != s[j]:
                        dp[i][j] = dp[i - 1][j + 1] + 1

        res = []
        for q in queries:
            a, b, c = q
            if dp[b][a] <= c:
                res.append(True)
            else:
                res.append(False)
        return res


class Solution(object):
    def canMakePaliQueries(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        n = len(s)
        prefix = [[0] * 26 for _ in range(n + 1)]
        a_ind = ord("a")

        for i in range(1, n + 1):
            ch = s[i - 1]
            prefix[i] = prefix[i - 1][:]
            ind = int(ord(ch) - a_ind)
            prefix[i][ind] += 1

        res = []

        def count_diff(left, right):
            count = 0
            for i in range(26):
                count += (right[i] - left[i]) % 2
            return count

        for q in queries:

            a, b, c = q
            left, right = prefix[a], prefix[b + 1]
            diff = count_diff(left, right)

            if (b - a) % 2 == 1:
                if diff // 2 <= c:
                    res.append(True)
                else:
                    res.append(False)
            else:
                if (diff - 1) // 2 <= c:
                    res.append(True)
                else:
                    res.append(False)
        return res

a = Solution()
tmp = "rkzavgdmdgt"
qq = [[8,10,0]]
print(a.canMakePaliQueries(tmp, qq))