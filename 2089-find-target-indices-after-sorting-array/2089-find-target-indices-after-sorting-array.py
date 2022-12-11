class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        nums.sort()
        indices  = []
        
        for i in range(0, len(nums)):
            targetIndex = 0
            if nums[i] == target:
                
                targetIndex = i
                indices += [targetIndex]
        
        return indices