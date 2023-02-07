 
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        decentPeriods = len(prices)
        
        start = 0
        while start < len(prices):
            end = start + 1
            while end < len(prices) and prices[end] == prices[end-1] - 1 :
                end = end + 1
            decentPeriods = decentPeriods + (end-start)*(end-start-1)//2
            start = end
        return decentPeriods
        