class Solution:
    def findLHS(self, nums: List[int]) -> int:
        frequency = Counter(nums)
        max_length = 0
        for num in frequency:
            if num + 1 in frequency:
                max_length = max(max_length, frequency[num]+frequency[num+1])
        return max_length
        