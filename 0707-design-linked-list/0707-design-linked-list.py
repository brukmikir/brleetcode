class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val):
        node = ListNode(val)
        node.next = self.head
        self.head = node
        self.size += 1

    def addAtTail(self, val):
        node = ListNode(val)
        if not self.head:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node
        self.size += 1

    def addAtIndex(self, index, val):
        if index < 0:
            index = 0
        if index > self.size:
            return

        node = ListNode(val)

        if index == 0:
            node.next = self.head
            self.head = node
        else:
            cur = self.head
            for _ in range(index - 1):
                cur = cur.next
            node.next = cur.next
            cur.next = node

        self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return

        if index == 0:
            self.head = self.head.next
        else:
            cur = self.head
            for _ in range(index - 1):
                cur = cur.next
            cur.next = cur.next.next

        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)