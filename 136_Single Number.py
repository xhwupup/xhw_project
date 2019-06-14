# 时间：20190524
# Example1:
# Input: Input: [2,2,1]
# Output: 1
# Example2:
# Input: [4,1,2,1,2]
# Output: 4
# 难度：Easy(0.25)


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res = res ^ i
        return res