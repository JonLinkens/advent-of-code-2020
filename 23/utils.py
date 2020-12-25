# approach : circular linked list (of nodes: values, prev/next pointers)
# algorithms module proving useful here
class LinkedListNode:
    def __init__(self, value):
        self.next = self.prev = None
        self.value = value

class CircularLinkedList:
    def __init__(self, vals):
        self.lookup = {}
        head = prev = None
        for v in vals:
            node = LinkedListNode(v)
            if not head:
                head = node
            if prev:
                prev.next = node
                node.prev = prev
            self.lookup[v] = prev = node
        head.prev = prev
        prev.next = head
    
    def getNode(self, key):
        return self.lookup[key]

    def moveCups(self, key, dest):
        cup = self.lookup[key]
        dest = self.lookup[dest]
        prev_next = dest.next
        cup.prev.next = cup.next
        cup.next.prev = cup.prev
        dest.next.prev = cup
        dest.next = cup
        cup.prev = dest
        cup.next = prev_next
