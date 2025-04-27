# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        if list1.val > list2.val:
            list1, list2 = list2, list1

        temp = list1        
        pre = None
        while temp and list2:
            if temp.val <= list2.val:
                pre = temp
                temp = temp.next
            else:
                cur = list2.next
                pre.next = list2
                pre = list2
                pre.next = temp
                list2 = cur
        pre.next = list2 or temp
        return list1


