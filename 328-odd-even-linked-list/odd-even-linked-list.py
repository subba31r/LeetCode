# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1 2 3 4 5
        # slow -> 1
        # fast -> 1
        # slow -> 2
        # fast -> 3
        #swap both
        # 1 3 2 4 5
        # slow -> 2
        # fast -> 5
        # 1 3 5 2 4

        if head is None or head.next is None or head.next.next is None:
            return head
        
        pre = head
        slow = head.next
        fast = head.next.next
        while fast and fast.next:
            temp = fast.next
            fast.next = pre.next
            pre.next = fast
            
            slow.next = temp
            pre = fast
            fast = temp.next
            slow = slow.next
        
        if fast is not None:
            temp = fast.next
            fast.next = pre.next
            pre.next = fast
            slow.next = temp
            pre = fast
        
        return head


