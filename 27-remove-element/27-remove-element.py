class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp = 0
        if len(nums) == 0:
            return 0
        while val in nums:
                nums.remove(val)
        return len(nums)