# Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

def reverse(head):
    prev = None
    curr = head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev