# 时间:20190513
# Example:
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Follow up:
#   A rather straight forward solution is a two-pass algorithm using counting sort.
#   First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
#   Could you come up with a one-pass algorithm using only constant space?
# 难度：Medium(0.5)

#思路：
#1）首先找出数组中的最小值的索引，然后将最小值与第一个元素交换位置。
#2）设置三个变量，一个是j表示当前指针，l表示当前还需遍历的长度，k表示k之前的所有元素都为0.从第一个元素开始循环遍历，遇到2，则pop(j),然后在尾部插入2，l–，遇到0则与索引值为k的元素交换。
#保证2永远在尾部，0永远在头部，1无需任何操作。
class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        index = 0
        for i in range(1, l):
            if nums[i] < nums[index]:
                index = i
        nums[0], nums[index] = nums[index], nums[0]
        k = j = 1
        while j < l:
            if nums[j] == 2:
                nums.pop(j)
                nums.append(2)
                l -= 1
            elif nums[j] == 0:
                nums[k], nums[j] = nums[j], nums[k]
                k += 1
                j += 1
            else:
                j += 1
