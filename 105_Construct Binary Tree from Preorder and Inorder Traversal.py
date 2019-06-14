# 时间：20190520
# Example1:
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
#
# Return the following binary tree:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 难度：Medium(0.5)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        #先序遍历的列表为[根，左，右]，中序遍历的列表为[左，根，右]，则中序遍历中根的下标为先序遍历中左的边界
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        #找到根节点在中序遍历中的下标
        n = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:n+1],inorder[:n])
        root.right = self.buildTree(preorder[n+1:],inorder[n+1:])
        return root

 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, l1, r1, l2, r2, preorder, inorder, dict):
        """
        """
        if r1 >= l1 and r2 >= l2:  # 递归的边界
            root = TreeNode(preorder[l1])
            mid = dict[root.val]  # 找到根节点在中序里的位置
            # print(mid)
            lsize = mid - l2
            rsize = r2 - mid  # 找到两个子树的范围
            root.left = self.dfs(l1 + 1, l1 + lsize, l2, l2 + lsize - 1, preorder, inorder, dict)
            root.right = self.dfs(l1 + lsize + 1, l1 + lsize + rsize, mid + 1, mid + rsize, preorder, inorder,
                                  dict)  # 对左右子树做同样的操作

            return root

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        dict = {}  # 定义一个字典
        n = len(preorder)
        if n == 0:
            return None
        for i in range(n):
            dict[inorder[i]] = i  # Inorder里的值和索引互换

        root = self.dfs(0, n - 1, 0, n - 1, preorder, inorder, dict)
        return root