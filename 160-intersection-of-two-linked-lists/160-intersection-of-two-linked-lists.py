# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        dummyA, dummyB = headA, headB # Take dummy nodes

        while dummyA != dummyB:
            dummyA = headB if dummyA is None else dummyA.next 
            dummyB = headA if dummyB is None else dummyB.next
        # Return any dummy pointer. i.e. If any intersection node is present it'll get returned else it will return None because at the end of iteration both dummy pointers will point to NULL.
        return dummyA 

# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#         hashSet = set()
#         currentA = headA
#         currentB = headB
#         if currentA == currentB:
#             return currentA
#         while currentA:
#             hashSet.add(currentA)
#             currentA = currentA.next
#         while currentB:
#             if currentB in hashSet:
#                 return currentB
#             currentB = currentB.next
#         return None