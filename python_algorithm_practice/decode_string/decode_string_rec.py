class Solution(object):
    def decodeString(self, s):
        def rec(s):
            res = ""
            n = len(s)
            i = 0
            while  i < n:
                if s[i] == "]":
                    return res, i
                if ord(s[i]) in range(ord("a"), ord("z")+1):
                    res += s[i]
                    i += 1
                    continue
                num = ""
                while s[i] in ["1", "2","3", "4", "5", "6", "7", "8", "9", "0"]:
                    num += s[i]
                    i += 1

                prod = int(num)
                i += 1
                string, last = rec(s[i:])
                i = i + last + 1
                res = res + prod * string

            return res

        all = rec(s)

        return all

a = Solution()
print(a.decodeString("30[a]jhg2[2[bc]]"))