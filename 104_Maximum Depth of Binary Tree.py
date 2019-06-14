# 时间：20190519
# Example1:
# Given binary tree [3,9,20,null,null,15,7],
#
#    3
#   / \
#  9  20
#    /  \
#   15   7
#
# return its depth = 3.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)+1
        right = self.maxDepth(root.right)+1
        return max(left,right)