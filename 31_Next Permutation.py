# 时间：20190505
# Example:
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# 难度：Medium(0.5)

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        down = 0
        flag = 0
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                down = i - 1
                flag = 1
                break
        if not flag:
            nums.reverse()
            return

        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[down]:
                nums[i], nums[down] = nums[down], nums[i]
                last = nums[down + 1:]
                last.sort()
                nums[down + 1:] = last
                return