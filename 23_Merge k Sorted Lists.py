#时间：20190504
#EXAMPLE:
#Input:
#[
#  1->4->5,
#  1->3->4,
#  2->6
#]
#Output: 1->1->2->3->4->4->5->6
#难度：Hard（1）

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        all_node=[]
        for x in lists:
            while x is not None:
                all_node.append(x)
                x=x.next

        all_node_sort=sorted(all_node,key=lambda node:node.val)
        pHead=ListNode(-1)
        p=pHead
        for node in all_node_sort:
            p.next=node
            p=node
        p.next=None
        return pHead.next



