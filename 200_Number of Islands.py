# 时间：20190528
# Example 1:
# Input:
# 11110
# 11010
# 11000
# 00000
# Output: 1
# Example 2:
# Input:
# 11000
# 11000
# 00100
# 00011
#
# Output: 3
# 难度：Medium(0.5)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n = len(grid)
        if n == 0: return 0
        m = len(grid[0])
        if m == 0: return 0
        res = 0
        # 遍历每一个字符
        for i in range(n):
            for j in range(m):
                # 如果遍历字符是陆地"1"
                if grid[i][j] == "1":
                    res += 1
                    # 递归查找与这块陆地相连的所有陆地 并将他们改为零
                    self.change(grid, i, j)
        return res

    def change(self, grid, i, j):
        grid[i][j] = "0"
        # 判断上方字符
        if i > 0 and grid[i - 1][j] == "1":
            self.change(grid, i - 1, j)
        # 判断左方字符
        if j > 0 and grid[i][j - 1] == "1":
            self.change(grid, i, j - 1)
        # 判断下方字符
        if i < len(grid) - 1 and grid[i + 1][j] == "1":
            self.change(grid, i + 1, j)
        # 判断右方字符
        if j < len(grid[0]) - 1 and grid[i][j + 1] == "1":
            self.change(grid, i, j + 1)
