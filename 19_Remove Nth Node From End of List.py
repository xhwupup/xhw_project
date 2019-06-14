# 时间：20190502
# Example:
# Given linked list: 1->2->3->4->5, and n = 2.
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# 难度：Medium(0.5)




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        List = []
        count = 0
        while (head):
            List.append(head)
            head = head.next
            count = count + 1

        if count == 1:
            return None
        if List[-n].next == None:
            List[-n - 1].next = None
            return List[0]
        else:
            List[-n].val = List[-n].next.val
            List[-n].next = List[-n].next.next
        return List[0]