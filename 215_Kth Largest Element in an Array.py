# 时间：20190529
# # Example 1:
# # Input: [3,2,1,5,6,4] and k = 2
# # Output: 5
# # Example 2:#
# # Input: [3,2,3,1,2,4,5,5,6] and k = 4
# # Output: 4
# # 难度：Medium(0.5)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]



# - - toulan ?..