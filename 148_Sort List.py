# 时间：20190526
# Example 1:
#
# Input: 4->2->1->3
# Output: 1->2->3->4
# Example 2:
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5
# 难度：Medium(0.5)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
	"""
	:type head: ListNode
	:rtype: ListNode
	"""
	def partition(start, end):
	    node = start.next.next
	    pivotPrev = start.next
	    pivotPrev.next = end
	    pivotPost = pivotPrev
	    while node != end:
		temp = node.next
		if node.val > pivotPrev.val:
		    node.next = pivotPost.next
		    pivotPost.next = node
		elif node.val < pivotPrev.val:
		    node.next = start.next
		    start.next = node
		else:
		    node.next = pivotPost.next
		    pivotPost.next = node
		    pivotPost = pivotPost.next
		node = temp
	    return [pivotPrev, pivotPost]

	def quicksort(start, end):
	    if start.next != end:
		prev, post = partition(start, end)
		quicksort(start, prev)
		quicksort(post, end)

	newHead = ListNode(0)
	newHead.next = head
	quicksort(newHead, None)
	return newHead.next