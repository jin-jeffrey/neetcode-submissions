class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return

        nodes = []
        temp = head
        while temp:
            nodes.append(temp)
            temp = temp.next

        nodes = nodes[(len(nodes) + 1) // 2:]

        current = head
        while nodes:
            end = nodes.pop()
            temp_next = current.next
            current.next = end
            end.next = temp_next
            current = temp_next

        current.next = None  # Break any remaining old link