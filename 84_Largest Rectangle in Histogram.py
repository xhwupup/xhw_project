# 时间：20190515
# Example:
# Input: [2,1,5,6,2,3]
# Output: 10
# 难度：Hard(1.0)

#递增栈：栈中只放递增序列
#思路：1.我们首先将2加入到栈中，我们接着访问1，我们发现1比栈顶元素2小，所以我们将栈顶元素2弹出，并且记录此时的面积2。我们发现栈已经空了，所以我们要接着压栈。
#2.接着我们通过不断遍历找到第二个递增栈。
#3.我们接着访问2，我们发现此时2比栈顶元素6小，所以我们弹出栈顶元素6，并且记录此时的面积6*1=6。
#4.此时栈中还有元素，我们发现此时2依旧比栈顶元素5大，所以我们需要将栈顶元素5弹出，并且我们记录此时出栈元素构成的最大面积5*2=10。
#5.我们发现此时的2比栈顶元素大了，我们就将2压入栈中，接着将3压入栈中。此时遍历结束，我们发现栈不为空，所以我们需要进行出栈操作，出栈的同时记录出栈元素构成的最大面积即可。

class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = list()
        res, i = 0, 0
        while i < len(heights):
            if not stack or (heights[i] >= heights[stack[-1]]):
                stack.append(i)
                i += 1
            else:
                k = stack.pop()
                res = max(res, heights[k] * ((i - stack[-1] - 1) if stack else i))

        while stack:
            k = stack.pop()
            res = max(res, heights[k] * ((i - stack[-1] - 1) if stack else i))

        return res


class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = [-1]
        res = 0
        heights.append(-1)

        for idx, val in enumerate(heights):
            while heights[stack[-1]] > val:
                h = heights[stack.pop()]
                res = max(res, h * (idx - stack[-1] - 1))

            stack.append(idx)

        return res
