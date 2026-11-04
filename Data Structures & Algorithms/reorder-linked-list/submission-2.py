# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        nodes = []

        temp = head
        while temp:
            nodes.append(temp)
            temp = temp.next

        nodes = nodes[(len(nodes) + 1) // 2:]

        current = head
        temp_next = current
        while len(nodes) > 0:
            # every iteration, add one from front, one from back
            end = nodes.pop()
            temp_next = current.next
            current.next = end
            current = current.next
            current.next = temp_next
            current = current.next
        

        current.next = None

