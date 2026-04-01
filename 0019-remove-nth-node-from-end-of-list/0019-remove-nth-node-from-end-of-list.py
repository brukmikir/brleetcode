# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        
        cur1 = dummy
        cur2 = dummy

        for _ in range(n + 1):
            cur2 = cur2.next

        while cur2:
            cur1 = cur1.next
            cur2 = cur2.next

        cur1.next = cur1.next.next

        return dummy.next

        
        