# 时间：20190522
# Example1:
# Input: [1,2,3]
#
#        1
#       / \
#      2   3
#
# Output: 6
#
# Example 2:
#
# Input: [-10,9,20,null,null,15,7]
#
#    -10
#    / \
#   9  20
#     /  \
#    15   7
#
# Output: 42
# 难度：Hard(1.0)


# 使用 self.max 记录全局最大值，getattr 返回自身 max 属性的值或预定义的负无穷
# 本题思路是：递归每一个节点，返回max(以当前节点为结尾的最大路径和,0)。并更新最大值全局最大路径和=max(全局最大路径和，当前节点值+左子树返回结果+右子树返回结果)
# 用ok判断是不是第一次递归，是就返回全局最大值，否则照常


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode, ok=True) -> int:
        if not root: return 0
        l, r = self.maxPathSum(root.left, False), self.maxPathSum(root.right, False)
        self.max = max(getattr(self, 'max', float('-inf')), l + root.val + r)
        return self.max if ok else max(root.val + max(l, r), 0)

