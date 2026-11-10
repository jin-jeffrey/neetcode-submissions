class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # Find the kth node from group_prev
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if kth is None:
                    return dummy.next  # Incomplete group stays as is

            group_next = kth.next

            # Reverse this group, stopping at group_next
            prev = group_next
            curr = group_prev.next

            while curr != group_next:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            # Connect the reversed group and advance to the next group
            old_group_head = group_prev.next  # Now this group's tail
            group_prev.next = kth
            group_prev = old_group_head