class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefixSum = sum(nums)
        sum_ = 0
        for i in range(len(nums)):
            sum_ += nums[i]
            if sum_ == prefixSum -( sum_ - nums[i]):
                return i
        return -1
        