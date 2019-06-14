# 时间：20190605
# Example 1:
# Input: [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
#
#     There may be more than one LIS combination, it is only necessary for you to return the length.
#     Your algorithm should run in O(n2) complexity.
# 难度：Medium(0.5)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        if size < 2:
            return size
        tail = []
        for num in nums:
            # 找到大于等于 num 的第 1 个数
            l = 0
            r = len(tail)
            while l < r:
                mid = l + (r - l) // 2
                if tail[mid] < num:
                    l = mid + 1
                else:
                    r = mid
            if l == len(tail):
                tail.append(num)
            else:
                tail[l] = num
        return len(tail)
