# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        count = 0

        while curr:
            curr = curr.next
            count += 1
    
        middle_index = count // 2   
        curr = head
        for _ in range(middle_index):
            curr = curr.next

        return curr

            