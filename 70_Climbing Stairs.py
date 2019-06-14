# 时间：20190510
# Exampole1:
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Exampole2:
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
# 难度：Easy(0.25)

class Solution:
    def climbStairs(self, n: int) -> int:
        count = [1,2]
        for i in range(2,n):
            count.append(count[i-1]+count[i-2])
        return count[n-1]