# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        current = head

        while current:
            length += 1
            current = current.next

        length -= n
        current = dummy

        while length > 0:
            current = current.next
            length -= 1

        current.next = current.next.next
        
        return dummy.next