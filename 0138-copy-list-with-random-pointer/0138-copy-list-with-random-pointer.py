"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None
        
        cur = head
        
        while cur:
            new = Node(cur.val)
            new.next = cur.next
            cur.next = new
            cur = new.next
        
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        
        cur = head
        new_head = head.next
        
        while cur:
            copy = cur.next
            cur.next = copy.next
            if copy.next:
                copy.next = copy.next.next
            cur = cur.next
        
        return new_head

        