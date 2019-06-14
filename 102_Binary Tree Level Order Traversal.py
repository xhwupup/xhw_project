# 时间：20190519
# Example1:
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# return its level order traversal as:
#
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
# 难度：Medium(0.5)



#思路：每次传入三个值：节点，节点所在的层级，保存节点值的二维数组
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ret = []

        def run(node, level, ret):
            if not node:
                return
            if level == len(ret):
                ret.append([])
            ret[level].append(node.val)
            run(node.left, level + 1, ret)
            run(node.right, level + 1, ret)

        run(root, 0, ret)
        return ret







# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        temp = [root]
        while temp:
            cur = []
            next_temp = []
            for node in temp:
                cur.append(node.val)
                if node.left:
                    next_temp.append(node.left)
                if node.right:
                    next_temp.append(node.right)
            res.append(cur)
            temp = next_temp
        return res