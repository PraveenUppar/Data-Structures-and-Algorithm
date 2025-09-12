# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            merged_list = []
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                if (i + 1) < len(lists):
                    list2 = lists[i + 1]
                else:
                    list2 = None
                merged_list.append(self.merge_lists(list1,list2))
            lists = merged_list
        return lists[0]

    def merge_lists(self,list1,list2):
        res = ListNode()
        temp = res 

        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        if list1:
            temp.next = list1
        else:
            temp.next = list2
        return res.next