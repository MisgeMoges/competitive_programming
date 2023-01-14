# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
            slow = fast = head
            while head:
                if not fast or not fast.next:
                    return slow
                else:
                    fast = fast.next.next
                    slow = slow.next
            return None
                
#         len_nodes= 0
#         current = node = head
#         while current:
#             len_nodes+= 1
#             current = current.next
#         middle = len_nodes//2
        
#         count = 0
#         while node:
#             if(count == middle):
#                 return node
#             else:
#                 count += 1
#                 node = node.next
#         return None

            
        
        