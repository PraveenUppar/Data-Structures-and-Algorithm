# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # head: 1 -> 2 -> 3 -> 4 -> 5 -> None

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # head: 1 -> 2 -> 3 -> None
        # list2: 4 -> 5 -> None
        list2 = slow.next
        slow.next = None

        prev = None

        while list2:
            temp = list2.next
            list2.next = prev
            prev = list2
            list2 = temp

        # head: 1 -> 2 -> 3 -> None
        # prev: 5 -> 4 -> None
        node1 = head
        node2 = prev

        while node2:
            temp1 = node1.next
            temp2 = node2.next
            node1.next = node2
            node2.next = temp1
            node1 = temp1
            node2 = temp2


        