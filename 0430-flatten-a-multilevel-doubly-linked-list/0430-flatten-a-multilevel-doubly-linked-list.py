"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        if not head:
            return head
        
        def dfs(node):
            curr = node
            last = node
            
            while curr:
                nxt = curr.next
                
                if curr.child:
                    child_last = dfs(curr.child)
                    
                    curr.next = curr.child
                    curr.child.prev = curr
                    
                    if nxt:
                        child_last.next = nxt
                        nxt.prev = child_last
                    
                    curr.child = None
                    last = child_last
                else:
                    last = curr
                
                curr = nxt
            
            return last
        
        dfs(head)
        return head