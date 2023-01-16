class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return nums
        
        # compute rotation
        k = k % len(nums)
        lenght = len(nums)
        
        #swap positions
        nums[lenght-k:], nums[:lenght-k] = nums[:lenght-k],nums[lenght-k:]
        
        
#         left = 0
#         right = len(nums)-1
#         while k > 0:
#             nums.insert(left, nums[right])
#             nums.pop(right+1)
            
           
#             k -= 1

        