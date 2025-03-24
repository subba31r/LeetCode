# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        slow = head
        fast = head
        pre=None
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        
        pre.next = slow.next
        slow.next = None
        return head
        
