# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True


        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp


        first, second = head, prev
        while second:
            if first.val != second.val:
                return False
            first = first.next
            second = second.next

        return True
