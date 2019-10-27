class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        if not nums or len(nums) < 6:
            return False

        problem_ind = -1
        n = len(nums)
        for i in range(1, n):
            diff = nums[i] - nums[i - 1]
            if diff != 1:
                problem_ind = i
                break

                # no problem
        if problem_ind == -1:
            return True

        last_seq = 1
        seq1, seq2 = [nums[0]], []
        i = 1
        start_seq2 = False
        while i < n:
            diff = nums[i] - nums[i - 1]
            if diff != 1:
                if last_seq == 1:
                    seq2.append(nums[i])
                    last_seq = 2
                else:
                    seq1.append(nums[i])
                    last_seq = 1
            else:
                if last_seq == 1 and not start_seq2:
                    seq1.append(nums[i])
                else:
                    seq2.append(nums[i])
                    start_seq2 = True

            if len(seq1) > 1:
                if seq1[-1] - seq1[-2] != 1:
                    return False

            if len(seq2) > 1:
                if seq2[-1] - seq2[-2] != 1:
                    return False
            i += 1

        if len(seq1) < 3 or len(seq2) < 3:
            return False

        return True

a = Solution()
res  = a.isPossible([1,2,3,3,4,4,5,5])
print(res)

#-----------------------------------------------
# Hackerrank read output and print
#-----------------------------------------------

# n = int(raw_input())
# for i in range(0,n):
#     a, b = raw_input().split()
#     print int(a) + int(b)

n = int(input())
for i in range(n):
    a, b = input().strip().split(' ')
    print(int(a) + int(b))


    def findNumber(arr, k):
        return 'YES' if k in arr else 'NO'
    
def findNumber(arr, k):
    return 'YES' if k in arr else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    k = int(input().strip())

    res = findNumber(arr, k)

    fptr.write(res + '\n')

    fptr.close()