# 时间：20190527
# Example 1:
# Input: [3,2,3]
# Output: 3
# Example 2:#
# Input: [2,2,1,1,1,2,2]
# Output: 2
# 难度：Easy(0.25)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand = nums[0]
        count = 1
        for i in nums[1:]:
            if count == 0:
                cand, count = i, 1
            else:
                if i == cand:
                    count = count + 1
                else:
                    count = count - 1
        return cand