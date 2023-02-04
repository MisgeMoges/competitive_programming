class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_val = nums[0]
        for i in range(1, len(nums)):
            max_val = max(max_val, nums[i])
        for i in range(len(nums)):
            if max_val != nums[i] and  max_val < 2*nums[i]:
                return -1
        return nums.index(max_val)
            
        