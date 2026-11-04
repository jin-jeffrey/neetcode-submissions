# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = ListNode(None)

        while head != None:
            current_node.val = head.val
            head = head.next
            temp_current = current_node
            current_node = ListNode(None, temp_current)
        
        return current_node.next