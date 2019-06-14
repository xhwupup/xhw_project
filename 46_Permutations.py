# 时间：20190508
# Example:
# Input: [1,2,3]
# Output:
# [
#  [1,2,3],
#  [1,3,2],
#  [2,1,3],
#  [2,3,1],
#  [3,1,2],
#  [3,2,1]
#]
# 难度：Medium(0.5)

#1:
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        if len(nums) == 1:
            return [nums]

        for i in range(len(nums)):
            for r in self.permute(nums[:i] + nums[i + 1:]):
                result.append([nums[i]] + r)
        return result

#2:
from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums))


#3:class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        if len(nums) == 1:
            return [nums]

        for i in range(len(nums)):
            for r in self.permute(nums[:i] + nums[i + 1:]):
                result.append([nums[i]] + r)
        return result

