# 时间：20190507
# Example1:
# Input:  [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# 难度：Hard(1)

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0

        max_height = 0
        max_height_index = 0

        # top
        for i in range(len(height)):
            h = height[i]
            if h > max_height:
                max_height = h
                max_height_index = i
        area = 0

        # left to right
        tmp = height[0]
        for i in range(max_height_index):
            if height[i] > tmp:
                tmp = height[i]
            else:
                area = area + (tmp - height[i])

        # right to left
        tmp = height[-1]
        for i in reversed(range(max_height_index + 1, len(height))):
            if height[i] > tmp:
                tmp = height[i]
            else:
                area = area + (tmp - height[i])

        return area