"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_head = Node(0)
        current_head = new_head
        
        legacy_to_new_nodes = {}
        temp_head = head
        while head != None:
            new_node = Node(head.val)
            current_head.next = new_node
            legacy_to_new_nodes[head] = new_node
            current_head = current_head.next
            # add the random node
            head = head.next
        
        current_head = new_head.next
        while temp_head != None:
            if temp_head.random:
                current_head.random = legacy_to_new_nodes[temp_head.random]
            temp_head = temp_head.next
            current_head = current_head.next
        
        return new_head.next

        
            