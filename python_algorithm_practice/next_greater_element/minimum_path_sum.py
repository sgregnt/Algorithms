class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """



        m = len(grid)
        n = len(grid[0])
        sums = [[float('inf')] * n for _ in range(m)]
        sums[m-1][n-1] = grid[m-1][n-1]

        for row in reversed(range(m)):
            for col in reversed(range(n)):
                if row < m - 1:
                    sums[row][col] = min([sums[row][col], grid[row][col] + sums[row+1][col]])

                if col < n - 1:
                    sums[row][col] = min([sums[row][col], grid[row][col] + sums[row][col+1]])

        return sums[0][0]

a = Solution()
# res = a.minPathSum([ [1,3,1],  [1,5,1],  [4,2,1]])
res = a.minPathSum([[1,2,3],[4,5,6]])
print(res)