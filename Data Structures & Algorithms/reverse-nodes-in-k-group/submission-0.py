# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        result = ListNode(0)
        current_result = result
        current_group_head = ListNode(0)
        current_group_reversed_head = None
        current_group_reversed = None
        current_group_count = 0
        while head != None:
            temp_node = ListNode(head.val)
            temp_node.next = current_group_reversed
            if current_group_reversed == None:
                current_group_reversed_head = temp_node
            current_group_reversed = temp_node
            current_group_count += 1
            # print(current_group_reversed.val, current_group_count)
            head = head.next
            if current_group_count == k:
                # add current_group_reversed_head.next to result
                # print(current_group_reversed_head.val, current_group_reversed_head.next)
                current_result.next = current_group_reversed
                current_result = current_group_reversed_head
                # update current_group_head, current_group_reversed_head, current_group_reversed, current_group_count
                current_group_head = head
                current_group_reversed_head = None
                current_group_reversed = None
                current_group_count = 0

        if current_group_count < k:
            current_result.next = current_group_head
        
        return result.next
            

