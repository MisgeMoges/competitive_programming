class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rightSum, leftSum = sum(nums), 0
        
        for index, num in enumerate(nums):
            rightSum -= num
            if leftSum == rightSum:
                return index
            leftSum += num
        return -1
            
            