class Solution(object):
    def longestArithSeqLength(self, A):
        diffs = {}
        A =  A
        for i in range(len(A)):
            a = A[i]
            for d in diffs:

                last, count = diffs[d]
                if a - A[last] == d:
                    if d == -7:
                        print("*", d, a, i)
                    diffs[d] = (i, count + 1)

            for j in range(i):
                d = a - A[j]

                if d in diffs:
                    pass
                else:
                    if d == -7:
                        print("*", d, a, i)
                    diffs[d] = (i, 2)


        print(diffs)
        max_count = 1
        for d in diffs:
            last, count = diffs[d]
            if count > max_count:
                max_count = count
                print(last, count, d)

        return max_count

a = Solution()
# print(a.longestArithSeqLength([9,4,7,2,10]))
print(a.longestArithSeqLength([44,46,22,68,45,66,43,9,37,30,50,67,32,47,44,11,15,4,11,6,20,64,54,54,61,63,23,43,3,12,51,61,16,57,14,12,55,17,18,25,19,28,45,56,29,39,52,8,1,21,17,21,23,70,51,61,21,52,25,28]))
print()