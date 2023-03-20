# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return head
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1
        current.next = head
        k = length-(k%length)
        while k > 0:
            current = current.next
            k -= 1
        newHead = current.next
        current.next = None
        return newHead