class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        first_occurence = {}
        last_occurence = {}
        
        min_length = float('inf')
        for i, num in enumerate(nums):
            freq[num] += 1
            if num not in first_occurence:
                first_occurence[num] = i
            last_occurence[num] = i
        degree = max(freq.values())  
        for num in freq:
            if freq[num] == degree:
                min_length = min(min_length, last_occurence[num]-first_occurence[num]+1)
        return min_length
                
        