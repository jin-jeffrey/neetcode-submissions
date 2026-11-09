# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # cycle through and handle the summation, if it is greater than 10, carry over a 1
        carry = 0
        result = ListNode(0)
        current = result
        while l1 != None or l2 != None:
            current_total = carry
            carry = 0
            # only traverse if the current node is not none
            if l1 != None:
                current_total += l1.val
                l1 = l1.next
            if l2 != None:
                current_total += l2.val
                l2 = l2.next
            if current_total > 9:
                carry = 1
                current_total -= 10
            current.next = ListNode(current_total)
            current = current.next
        
        if carry == 1:
            current.next = ListNode(1)

        return result.next