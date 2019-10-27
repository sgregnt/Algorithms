"beginWord, endWord, wordList"
from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):

        auxlist = {}

        wordList =  [list(word) for word in wordList]

        for word in wordList:
            n  = len(word)
            for i in range(n):
                tmp = word[:]
                tmp[i] = "*"
                if tuple(tmp) in auxlist:
                    auxlist[tuple(tmp)].append(word)
                else:
                    auxlist[tuple(tmp)] = [word]

        my_hash = {}
        for word in wordList:
            my_hash[tuple(word)] = False

        q = deque()
        q.append((list(beginWord), 0))

        # breadth first search
        while q:

            word, gen = q.pop()
            n = len(word)

            for i in range(n):

                tmp = word[:]
                tmp[i] = "*"

                if tuple(tmp) in auxlist:
                    for next_word in auxlist[tuple(tmp)]:
                        if next_word == list(endWord):
                            return gen + 1
                        if my_hash[tuple(next_word)] == False:
                            q.appendleft((next_word, gen + 1))
                            my_hash[tuple(next_word)] = True

        return 0

a = Solution()
print(a.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
