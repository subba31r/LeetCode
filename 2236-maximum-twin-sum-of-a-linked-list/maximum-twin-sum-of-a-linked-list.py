# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow = slow.next
        pre = None
        while slow:
            temp = slow.next
            slow.next = pre
            pre = slow
            slow = temp
        
        res = 0
        temp = head
        while pre:
            cur = pre.val + temp.val
            res = max(res,cur)
            pre = pre.next
            temp = temp.next
        return res

            
