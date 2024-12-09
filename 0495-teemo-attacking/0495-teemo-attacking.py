
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:  # Handle empty list case
            return 0
        
        total_time = 0

        for i in range(1, len(timeSeries)):
            # Add the minimum of the gap or the poison duration
            total_time += min(duration, timeSeries[i] - timeSeries[i - 1])

        # Add the duration for the last attack
        total_time += duration

        return total_time
        