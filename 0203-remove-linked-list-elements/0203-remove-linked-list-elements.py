# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):

    def removeElements(self, head, val):
        dumy = ListNode(0)
        dumy.next=head
        cur=dumy
        while(cur.next):
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur=cur.next
        return dumy.next
        