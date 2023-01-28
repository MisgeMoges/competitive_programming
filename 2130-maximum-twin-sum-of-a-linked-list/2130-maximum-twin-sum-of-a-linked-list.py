# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ans = []
        current = head
        while current:
            ans.append(current.val)
            current = current.next
        size = len(ans)
        max_twin_sum = 0
        for i in range(size):
            max_twin_sum = max(max_twin_sum, ans[i]+ans[size-1-i])
        return max_twin_sum
            
        