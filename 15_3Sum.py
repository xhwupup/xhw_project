# 时间：20190430
# Example:
# Given array nums = [-1, 0, 1, 2, -1, -4],
# A solution set is:
#[
# [-1, 0, 1],
  #[-1, -1, 2]
#]
#难度：medium（0.5）
#这个题烂熟于心
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        result=[]
        nums.sort()
        for i in range(n):
            left=i+1
            right=n-1
            if i>0 and nums[i]==nums[i-1]:
                left=left+1
                continue
            while left<right:
                sum=nums[i]+nums[right]+nums[left]
                if sum==0:
                    col=[nums[i],nums[left],nums[right]]
                    result.append(col)
                    left+=1
                    right-=1
                    while left<right and nums[left] == nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                elif sum<0:
                    left+=1
                elif sum>0:
                    right-=1
        return result