# 时间：20190510
# Exampole1:
# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.
# 难度：Medium(0.5)

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        m = len(grid[0])
        for i in range(1, n):
            grid[i][0] = grid[i - 1][0] + grid[i][0]  # 首先需要寻找左边界各点的路径总和

        for j in range(1, m):
            grid[0][j] = grid[0][j - 1] + grid[0][j]  # 寻找上边界各点的路径总和

        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]  # 以边界处为依据一步步推出内部个点的路径总和

        return grid[n - 1][m - 1]
