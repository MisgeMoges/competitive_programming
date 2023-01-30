class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum, window_sum = 0, 0
        left, right = 0, k
        for i in range(k):
            window_sum += nums[i]
        
        max_sum = window_sum
        start = 0
        for i in range(k, len(nums)):
            window_sum = window_sum-nums[start]+nums[i]
            max_sum = max(max_sum, window_sum)
            start += 1
        return max_sum/k
                    
                
            