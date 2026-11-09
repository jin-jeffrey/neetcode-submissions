# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # track the head
        # use two pointers, one left and one right, right will be n+1 points away from the end
        # cycle until right has no next then remove n
        # in order to use n+1 from the end, we need to be able to go into right pointer = None
        head_node = ListNode(0, head)

        left = head_node
        right = head_node.next

        for i in range(n):
            right = right.next

        while right != None:
            right = right.next
            left = left.next
        
        left.next = left.next.next

        return head_node.next