# 时间：20190428
# Example:
# nums1 = [1, 3]
# nums2 = [2]
# 则中位数是 2.0
# 难度：Hard(1)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_nums=sorted(nums1+nums2)
        new_len=new_nums.__len__() # new_len=len(new_nums)
        if new_len % 2 ==0:
            return (new_nums[new_len//2]+new_nums[new_len//2-1])/2
        else:
            return new_nums[new_len//2]