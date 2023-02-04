class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return sum(list(set(nums)))*2 - sum(nums)
#         for i in range(len(nums)):
#             if nums.count(nums[i]) == 1:
#                 return nums[i]
                
                
#         return 