from bisect import bisect_left


class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """

        ages.sort()
        i = bisect_left(ages, 100)

        below_100 = ages[:i]
        above_100 = ages[i:]

        count = 0

        for part in [below_100, above_100]:
            if len(part) > 0:
                pass
            else:
                break
            n = len(part)
            i = 0
            j = 1
            prev = part[0]
            if part[0] == part[1]:
                equal = 2
            else:
                equal = 1

            while j < n:
                if part[i] <= 0.5 * part[j] + 7:
                    i += 1
                else:
                    dif = (j - i)
                    j += 1

                    if j < n and prev == part[j]:
                        equal += 1
                        j += 1
                    else:
                        if j < n:
                            prev = part[j]
                            count += dif * equal + equal * (equal - 1)
                        else:
                            count += dif * (equal - 1) + equal * (equal - 1)

                        equal = 1

        return count

a = Solution()
print(a.numFriendRequests([16, 16]))
