# from bisect import bisect_left
import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        hash_map = {}

        for num in nums:
            if not num in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num] += 1

        freqs = []
        # create priority queue
        #
        for elem in hash_map:
            freqs.append((-hash_map[elem], elem))

        heapq.heapify(freqs)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(freqs))

        res = [elem[1] for elem in res]
        return res


nums = [1,1,1,2,2,3,8,8,8,8,8,8,8,8]
a = Solution()
print(a.topKFrequent(nums, 3))


@functools.total_ordering
class Element:
    def __init__(self, count, word):
        self.count = count
        self.word = word

    def __lt__(self, other):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count

    def __eq__(self, other):
        return self.count == other.count and self.word == other.word