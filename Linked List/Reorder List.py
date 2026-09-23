# You are given the head of a singly linked-list.

# The positions of a linked list of length = 7 for example, can intially be represented as:

# [0, 1, 2, 3, 4, 5, 6]

# Reorder the nodes of the linked list to be in the following order:

# [0, 6, 1, 5, 2, 4, 3]

# Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:

# [0, n-1, 1, n-2, 2, n-3, ...]

# You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

def reorder(head):

    if not head:
        return 

    nodes = []
    curr = head 

    while curr:
        nodes.append(curr)
        curr = curr.next

    i = 0
    j = len(nodes) - 1

    while i < j:
        nodes[i].next = nodes[j]
        i += 1

        if i > j:
            break 

        nodes[j].next = nodes[i]
        j -= 1

    nodes[i].next = None