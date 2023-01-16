class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        left = 0
        right = len(nums)-1
        while k > 0:
            nums.insert(left, nums[right])
            nums.pop(right+1)
            
           
            k -= 1
        
            