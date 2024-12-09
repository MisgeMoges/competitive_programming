class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        total_time = 0
        for i in range(1, len(timeSeries)):
            overlap_time = timeSeries[i]-timeSeries[i-1]
            total_time += min(overlap_time, duration)
            
        total_time += duration
        return total_time
        