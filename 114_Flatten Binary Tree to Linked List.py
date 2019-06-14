# 时间：20190520
# Example1:
# For example, given the following tree:
#
#    1
#   / \
#  2   5
# / \   \
#3   4   6
#
#The flattened tree should look like:
#
#1
# \
#  2
#  \
#   3
#    \
#      4
#       \
#       5
#        \
#         6

# 难度：Medium(0.5)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Definition for a binary tree node.
        #递归之后如果存在左子树，把右子树保留，右子树置换成左子树，左子树置空
        #找到该树的最终节点，即最右节点，再链接开始保留的右子树，即r
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left:
            tmp = root.right
            root.right = root.left
            root.left = None
            node = root.right
            while node.right:
                node = node.right
            node.right = tmp