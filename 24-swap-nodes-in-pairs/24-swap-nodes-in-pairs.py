# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, current = dummy, head
        while current and current.next:
            next_pairs = current.next.next
            second = current.next
            
            second.next = current
            current.next = next_pairs
            prev.next = second
            
            prev = current
            current = next_pairs
        return dummy.next
        
    
                