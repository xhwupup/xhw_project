# 时间：20190531
# Example 1:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# Example 2:
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
# 难度：Easy(0.5)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        dic={root:None}
        def bfs(node):
            if node:
                if node.left:dic[node.left]=node
                if node.right:dic[node.right]=node
                bfs(node.left)
                bfs(node.right)
        bfs(root)
        l1,l2=p,q
        while(l1!=l2):
            l1=dic.get(l1) if l1 else q
            l2=dic.get(l2) if l2 else p
        return l1