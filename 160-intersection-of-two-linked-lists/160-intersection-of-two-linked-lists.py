# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hashSet = set()
        currentA = headA
        currentB = headB
        if currentA == currentB:
            return currentA
        while currentA:
            hashSet.add(currentA)
            currentA = currentA.next
        while currentB:
            if currentB in hashSet:
                return currentB
            currentB = currentB.next
        return None