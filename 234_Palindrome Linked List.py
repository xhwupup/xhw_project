# 时间：20190530
# Example 1:
# Input: 1->2
# Output: false
# Example 2:
# Input: 1->2->2->1
# Output: true
# 难度：Easy(0.25)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        :type head: ListNode
        :rtype: bool
        """
        res = []
        cur = head
        while cur:
            res.append(cur.val)
            cur = cur.next
        return res == res[: : -1]