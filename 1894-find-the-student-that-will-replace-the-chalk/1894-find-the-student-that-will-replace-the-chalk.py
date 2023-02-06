class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        if total == 1:
            return 0
        for i in range(k):
            j = 0
            while k < total and j < len(chalk):
                if k < chalk[j]:
                    return j
                k = k-chalk[j]
                
                j += 1
                
            k = k-total
        return -1 
            