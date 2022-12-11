class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
       
        countNumber = [0]*len(nums)
       
        for i in range(len(nums)):
            
            count = 0
            for j in range(0, len(nums)):
                if(nums[j] < nums[i]) and (i != j):
                    count +=1
            countNumber[i] += count
            
            
        return countNumber