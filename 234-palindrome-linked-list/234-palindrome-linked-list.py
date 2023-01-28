# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []
        current = head
        while current:
            nums.append(current.val)
            current = current.next
        start, end = 0, len(nums)-1
        while start <= end:
            if nums[start] != nums[end]:
                return False
            start += 1
            end -= 1
        return True
            