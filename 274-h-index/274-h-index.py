class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        N = len(citations)
        for i, value in enumerate(citations):
            if N-i <= value:
                return N-i
            
        return 0
    
    
        
        