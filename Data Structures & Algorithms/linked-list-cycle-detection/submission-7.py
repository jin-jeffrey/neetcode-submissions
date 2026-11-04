# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Use two pointers, one pointer travels 1 at a time, one pointer travels 2 at a time
        first = head

        if first == None or first.next == None:
            return False
        
        second = head.next

        while second != None:

            if first is second:
                return True
            
            first = first.next

            second = second.next
            if second != None:
                second = second.next
            else:
                return False

        return False