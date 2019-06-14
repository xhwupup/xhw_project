# 时间：20190605
# Example:
#
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# 难度：Easy(0.25)


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        for num in nums:
            if num != 0:
                nums[index] = num
                index += 1
        for i in range(index,len(nums)):
            nums[i] = 0