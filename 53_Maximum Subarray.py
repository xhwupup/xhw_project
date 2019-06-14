# 时间：20190509
# Example:
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# 难度：Easy(0.25)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum=maxSum=nums[0]
        for i in range(1,len(nums)):
            curSum = max(nums[i],curSum+nums[i])
            maxSum = max(curSum,maxSum)
        return maxSum