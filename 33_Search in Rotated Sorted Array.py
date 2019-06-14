# 时间：20190506
# Example1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# 难度：Medium(0.5)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        pol = r
        ans = self.binary_search(target, nums[:pol])
        if ans == -1:
            ans = self.binary_search(target, nums[pol:])
            if ans != -1:
                ans += len(nums[:pol])

        return ans

    def binary_search(self, target, nums):
        n = len(nums)
        index = -1
        l = 0
        r = n - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                index = mid
                break
        return index

