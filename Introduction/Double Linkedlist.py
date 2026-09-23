class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class DoubleLinkedlist:

    def __init__(self, head):
        self.head = head

    def addNodeAtStart(self, val, head):
        new_node = Node(val)

        if not head:
            return new_node

        new_node.next = head
        head.prev = new_node
        head = new_node

        return head

    def addNodeAtEnd(self, val, head):
        new_node = Node(val)

        if not head:
            return new_node 

        curr = head
        while curr.next is not None:
            curr = curr.next

        curr.next = new_node
        new_node.prev = curr

        return head        

    def deleteNode(self, target, head):
        if not head:
            return None 

        if head.val == target:
            next_node = head.next
            if next_node:
                next_node.prev = None
            return next_node

        curr = head
        prev_node = None

        while curr and curr.val != target:
            prev_node = curr
            curr = curr.next

        if curr is None:
            return head

        temp = curr.next
        prev_node.next = temp
        if temp:
            temp.prev = prev_node

        return head