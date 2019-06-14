# 时间：20190527
# Example 1:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.
# 难度：Easy(0.25)


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = [(None, float('inf'))]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.data.append((x, min(x, self.data[-1][1])))

    def pop(self):
        """
        :rtype: None
        """
        if len(self.data) > 1: self.data.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.data[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()