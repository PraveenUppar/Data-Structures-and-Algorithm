# Given the head of a linked list and an integer n, remove the nth node from the end of the list and return its head.

def remove(head, n):

    nodes = []
    cur = head

    while cur:
        nodes.append(cur)
        cur = cur.next

    removeIndex = len(nodes) - n
    
    if removeIndex == 0:
        return head.next

    nodes[removeIndex - 1].next = nodes[removeIndex].next
    return head