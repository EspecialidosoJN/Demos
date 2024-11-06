# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        rhead = ListNode()
        current = None
        while l1 != None or l2 !=None or carry > 0:
            val1=0
            val2=0
            if current is None:
                current = rhead
            else:
                current.next = ListNode()
                current = current.next
            if l1 != None:
                val1 = l1.val
                l1 = l1.next
            if l2 != None:
                val2 = l2.val
                l2 = l2.next
            tot = val1+val2+carry
            carry = 0
            if tot >= 10:
                tot = tot%10
                carry = 1
            current.val = tot
        return rhead
