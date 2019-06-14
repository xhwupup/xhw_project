# 时间：20190604
# Example 1:
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# 难度：Medium(0.5)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = 1    # 原始数据下标
        n = len(nums)  # 原始列表长度
        output = []  # 返回列表
        for i in range(0,n):
	    # 第一个for循环，实现求前n位数的乘积
	    # 并把结果存储在output列表
            output.append(p)
            p = p * nums[i]
        p = 1  # 回到最原始数据下标
        for i in range(n-1,-1,-1):
	    # 第二个for循环，倒序遍历，实现题目要求
	    # 并把结果存储在output列表
            output[i] = output[i] * p
            p = p * nums[i] # 求后n-i位的积
        return output
