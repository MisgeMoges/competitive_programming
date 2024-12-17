class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        n = len(nums)
        freq = [0]*(n+1)
        for num in nums:
            freq[num] += 1
        dup = missing = -1
        for i in range(1, n+1):
            if freq[i] == 2:
                dup = i
                
            elif freq[i] == 0:
                missing = i
        return [dup, missing]
            
            
            