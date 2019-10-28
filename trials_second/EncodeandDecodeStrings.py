# Design an algorithm to encode a list of strings to a string. The encoded
# string is then sent over the network and is decoded back to the original
# list of strings.
class Codec:

    def encode(self, strs):
        return ''.join('%d:' % len(s) + s for s in strs)

    def decode(self, s):
        strs = []
        i = 0
        while i < len(s):
            j = s.find(':', i)
            i = j + 1 + int(s[i:j])
            strs.append(s[j+1:i])
        return strs

    class Codec:

        def encode(self, strs):
            """Encodes a list of strings to a single string.

            :type strs: List[str]
            :rtype: str
            """
            if not strs:
                return "34"

            encode = ''
            for elem in strs:
                for i in elem:
                    encode += i
                    encode += i

                encode += "12"
            return encode[:-2]

        def decode(self, s):
            """Decodes a single string to a list of strings.

            :type s: str
            :rtype: List[str]
            """

            if s == "34":
                return []

            res = []
            n = len(s)
            tmp = ''
            i = 0
            while i < n:
                if s[i] != s[i + 1]:
                    res.append(tmp)
                    tmp = ""
                else:
                    tmp += s[i]
                i += 2

            res.append(tmp)

            return res   