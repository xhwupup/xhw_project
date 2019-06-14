# 时间：20190518
# Example1:
#    2
#    / \
#   1   3
#
# Input: [2,1,3]
# Output: true
#
#  5
#   / \
#  1   4
#     / \
#    3   6
##
# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
# 难度：Medium(0.5)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower, upper):
            if not node:
                return True

            if node.val > lower and node.val < upper:
                return helper(node.left, lower, node.val) and helper(node.right, node.val, upper)
            else:
                return False

        return helper(root, float('-inf'), float('inf'))


