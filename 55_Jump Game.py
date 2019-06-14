# 时间：20190509
# Example1:
# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example2:
# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
#              jump length is 0, which makes it impossible to reach the last index.
# 难度：Medium(0.5)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        c = len(nums)
        pos = [0] * c
        pos[0] = 1
        temp = nums[0]
        pos[1:1+nums[0]] = [1]*nums[0]
        for i in range(1, c-1):
            if pos[i] != 0 and i+1+nums[i]>temp:
                pos[i+1:i+1+nums[i]] = [1]*nums[i]
                temp = i+1+nums[i]
                if temp >= c:
                    break
        if pos[c-1] == 1:
            return True
        else:
            return False