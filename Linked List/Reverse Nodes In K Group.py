# You are given the head of a singly linked list head and a positive integer k.

# You must reverse the first k nodes in the linked list, and then reverse the next k nodes, and so on. If there are fewer than k nodes left, leave the nodes as they are.

# Return the modified list after reversing the nodes in each group of k.

# You are only allowed to modify the nodes' next pointers, not the values of the nodes.

def reverseKGroup(self, head, k):
    if not head or k == 1:
        return head

    nodes = []
    curr = head
    while curr:
        nodes.append(curr)
        curr = curr.next

    n = len(nodes)
    for start in range(0, n, k):
        end = start + k
        if end <= n: 
            left, right = start, end - 1
            while left < right:
                nodes[left], nodes[right] = nodes[right], nodes[left]
                left += 1
                right -= 1

    for i in range(n - 1):
        nodes[i].next = nodes[i + 1]
    nodes[-1].next = None

    return nodes[0]