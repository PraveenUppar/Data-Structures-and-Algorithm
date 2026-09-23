# You are given the head of a singly linked list and two integers left and right where left <= right, 
# reverse the nodes of the list from position left to position right (1-indexed), and return the reversed list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        res = ListNode(0)
        res.next = head
        prev = res

        for _ in range(left - 1):
            prev = prev.next

        sublist_head = prev.next
        sublist_tail = sublist_head

        for _ in range(right - left):
            sublist_tail = sublist_tail.next

        next_node = sublist_tail.next
        sublist_tail.next = None

        reversed_sublist = self.reverse_list(sublist_head)

        prev.next = reversed_sublist
        sublist_head.next = next_node

        return res.next

    def reverse_list(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev