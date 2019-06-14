# 时间：20190530
# Example 1:
# Input:
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
#
# Output:
#
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
# 难度：Easy(0.25)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left,root.right = self.invertTree(root.right),self.invertTree(root.left)
            return root