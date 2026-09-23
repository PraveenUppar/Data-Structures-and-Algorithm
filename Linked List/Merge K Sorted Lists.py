# You are given an array of k linked lists lists, where each list is sorted in ascending order.

# Return the sorted linked list that is the result of merging all of the individual linked lists.

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def mergeKLists(self, lists):
    if len(lists) == 0:
        return None
    return self.merge(lists, 0, len(lists) - 1)

def merge(self, lists, lo, hi):
    if lo == hi:
        return lists[lo]
    mid = (lo + hi) // 2
    left = self.merge(lists, lo, mid)
    right = self.merge(lists, mid + 1, hi)
    return self.mergedList(left, right)

def mergedList(l1, l2):
    res = ListNode()
    curr = res
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    if l1:
        curr.next = l1
    if l2:
        curr.next = l2
    return res.next