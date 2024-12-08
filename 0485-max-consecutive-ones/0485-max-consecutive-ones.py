class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, window_size = 0, 0
        for n in nums:
            if n == 1:
                window_size += 1
            else:
                res = max(res, window_size)
                window_size = 0
        res = max(res, window_size)
        return res
        