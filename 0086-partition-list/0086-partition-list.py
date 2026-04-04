# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        before = ListNode(0)
        after = ListNode(0)
        
        before_cur = before
        after_cur = after
        
        while head:
            if head.val < x:
                before_cur.next = head
                before_cur = before_cur.next
            else:
                after_cur.next = head
                after_cur = after_cur.next
            head = head.next
        
        after_cur.next = None
        before_cur.next = after.next
        
        return before.next
        