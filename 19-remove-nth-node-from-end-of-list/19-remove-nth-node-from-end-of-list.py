# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr  = head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        index = count - (n+1)
        curr = head
        
        if count == n:
            return head.next
        i = 0
        while curr and index > 0:
            curr = curr.next
            index -= 1
            
        curr.next = curr.next.next
        return head
    
            