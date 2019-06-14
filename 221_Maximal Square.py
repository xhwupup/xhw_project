# 时间：20190530
# Example 1:
# Input:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# Output: 4
# 难度：Medium(0.5)

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        dp[i][j]表示以第i行第j列为右下角所能构成的最大正方形边长, 则递推式为:
        dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        """
        row = len(matrix)
        if row < 1:
            return 0
        col = len(matrix[0])
        Max = 0
        dp = [[0 for _ in range(col + 1)] for _ in range(row + 1)]

        for i in range(1, row + 1):
            for j in range(1, col + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = 1 + int(min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]))
                    Max = max(Max, dp[i][j])
        return Max ** 2