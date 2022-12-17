class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        
        count, left, right, = 0, 0, len(nums)-1
        
        while left < right:
            
            val = nums[left] + nums[right]
            
            if val <= k:
                left += 1
            if val >= k:
                right -= 1
            if val==k:
                count += 1
                
        return count
    
     
            
            
   