# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # st1, st2 = "", ""
        # temp1, temp2 = l1, l2
        # while temp1:
        #     st1 = st1 + str(temp1.val)
        #     temp1 = temp1.next
        # while temp2:
        #     st2 = st2 + str(temp2.val)
        #     temp2 = temp2.next
        # num1 = int(st1[::-1])
        # num2 = int(st2[::-1])
        # total = num1 + num2
        # num = str(total)[::-1]
        # res = ListNode(1)
        # curr = res
        # i = 0
        # while i<len(num):
        #     curr.next = ListNode(int(num[i]))
        #     curr = curr.next
        #     i += 1
        # return res.next

        #by using carry
        carry = 0
        temp1 = l1
        temp2 = l2
        dummy = ListNode(1)
        prev = dummy
        while temp1 != None or temp2 != None or carry != 0:
            v1 = temp1.val if temp1 else 0
            v2 = temp2.val if temp2 else 0
            total = v1 + v2 + carry
            carry = total//10
            total = total%10
            cur = ListNode(total)
            prev.next = cur
            prev = cur
            if temp1:
                temp1 = temp1.next
            if temp2:
                temp2 = temp2.next
        return dummy.next