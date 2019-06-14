# 时间：20190605
# Example 1:
#You may serialize the following tree:

#    1
#   / \
#  2   3
#     / \
#    4   5
#
# as "[1,2,3,null,null,4,5]"
# 难度：Hard(1)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    """
    Solution Method
    参考答案给的解法是将二叉树DFS序列化，然后对其反序列化
        这里我最关键的是每想到这样去反序列化，因为python传参是引用传参，通过这种先左后右虽然传
    的都是同一个data，但是其实在左子树和右子树的建立中所看到的data是不一样的，而序列化的建立过程中
    又是先左后右的，所以对一个序列用data[0]去建立节点反序列化是可以构造出原来的树的，而且这种DFS的
    方法不会像我用层次遍历一样建立很多none的空节点，效率相对来说高
    ❗️❗️❗️：
        其实第105题根据先序和中序构造二叉树也是巧妙地利用了这种传参就是传引用的特点，对二叉树进行的
    处理，可以回顾一下
        再一个是序列化的过程中要注意参数传递的意义和值，string在左右子树中就不能+=了，不然会错，因为
    此时的string 已经是+=root.val了，底下既向下传这个加后的string，又+=，就会重复导致出错
    """

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def preorder(root, string):
            if root == None:
                string += 'None,'
            else:
                string += str(root.val) + ','
                string = preorder(root.left, string)
                string = preorder(root.right, string)
            return string

        return preorder(root, '')

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def reconstructTree(data):
            if data[0] == 'None':
                data.pop(0)
                return None
            root = TreeNode(int(data[0]))
            data.pop(0)
            root.left = reconstructTree(data)
            root.right = reconstructTree(data)
            return root

        return reconstructTree(data[:-1].split(','))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


