class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        maxSum = 0
        while left < right:
            maxSum = max(maxSum, nums[right]+nums[left])
            right -= 1
            left += 1
        return maxSum
            