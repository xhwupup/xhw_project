# 时间：20190605
# Example 1:
#
# Input: [1,3,4,2,2]
# Output: 2
# Example 2:
#
# Input: [3,1,3,4,2]
# Output: 3
# 难度：Medium(0.5)


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(0, len(nums)):
            res ^= nums[i]
        b = list(set(nums))
        for j in range(0, len(b)):
            res ^= b[j]
        return res