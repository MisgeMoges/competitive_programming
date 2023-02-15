class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums = sorted(nums)
        if len(nums) == 0:
            return -1
        right = len(nums)-1
        ans = []
        for i in range(len(nums)):
            ans.append((nums[i] + nums[right])/2)
            right -= 1
        return len(set(ans))