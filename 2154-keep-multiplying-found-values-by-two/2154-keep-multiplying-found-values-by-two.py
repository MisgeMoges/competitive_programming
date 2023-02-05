class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        hashSet = set(nums)
        while original in hashSet:
            original = 2*original
        return original
        