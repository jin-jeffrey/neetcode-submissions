# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(None)
        head = result

        while list1 != None or list2 != None:

            if list1 == None:
                result.next = ListNode(list2.val)
                list2 = list2.next
            elif list2 == None:
                result.next = ListNode(list1.val)
                list1 = list1.next                
            elif list1.val < list2.val:
                result.next = ListNode(list1.val)
                list1 = list1.next
            else:
                result.next = ListNode(list2.val)
                list2 = list2.next

            result = result.next

        return head.next