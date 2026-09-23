class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, head):
        self.head = head 

    def addNodeAtStart(self, val, head):
        new_node = Node(val)

        if not head:
            return new_node

        new_node.next = head
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

        return head

    def deleteNode(self, head, target):

        if not head:
            return None

        if target == head.val:
            return head.next

        curr = head
        prev = None

        while curr and curr.val != target:
            prev = curr
            curr = curr.next

        if curr == None:
            return head

        temp = curr.next
        prev.next = temp
        
        return head