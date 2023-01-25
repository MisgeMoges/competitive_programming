class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        if len(nums) == 1:
            return nums[0]
        for num in nums:
            if counter[num] > len(nums)/2:
                return num
        return 