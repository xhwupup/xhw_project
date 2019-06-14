# 时间：20190603
# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
# Example 1:
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
# Example 2:
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
# 难度：Medium(0.5)


# Lagrange 四平方定理： 任何一个正整数都可以表示成不超过四个整数的平方之和。
# 也就是说，这个题目返回的答案只有1、2、3、4这四种可能。 我们可以将输入的数字除以4来大大减少计算量，并不改变答案
# 一个数除以8的余数，如果余数为7， 则其必然由四个完全平方数组成
# 然后检测是否可以将简化后的数拆分为两个完全平方数，否则一定由三个完全平方数组成。
# 满足四数平方和定理的数n（四个整数的情况），必定满足 n=（4^ a） * (8b+7)
import math
class Solution:
    def numSquares(self, n: int) -> int:
        while n % 4 == 0: n = n // 4
        if n % 8 == 7: return 4
        if int(math.sqrt(n)) ** 2 == n: return 1
        i = 1
        while i*i <= n:
            j = math.sqrt(n - i*i)
            if int(j) == j: return 2
            i += 1
        return 3
