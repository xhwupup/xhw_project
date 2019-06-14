# 时间：20190527
# Example 1:
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.
# Example 2:#
# Input: [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
#              Total amount you can rob = 2 + 9 + 1 = 12.
# 难度：Easy(0.25)

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #nums长度要分情况讨论，方法很笨
        if not len(nums):
            return 0
        if len(nums)<3:
            return max(nums)
        if len(nums)<4:
            return max(nums[1],nums[0]+nums[2])
        dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]
        dp[2] = nums[0] + nums[2]
        #常规的dp算法
        for i in range(3,len(nums)):
            dp[i] = nums[i] + max(dp[i-2],dp[i-3])
        return max(dp)