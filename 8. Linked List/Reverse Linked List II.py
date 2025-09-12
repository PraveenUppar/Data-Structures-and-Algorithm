# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head or left == right:
            return head

        res = ListNode(0,head)
        left_pointer = res

        for _ in range(left - 1):
            left_pointer = left_pointer.next

        left_node = left_pointer.next

        for _ in range(right - left):
            temp = left_node.next
            left_node.next = temp.next
            temp.next = left_pointer.next
            left_pointer.next = temp
        return res.next