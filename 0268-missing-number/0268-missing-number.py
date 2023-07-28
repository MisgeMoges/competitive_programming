class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        set_values = set(nums)
        for i in range(len(nums)+1):
            if i not in set_values:
                return i
        return 