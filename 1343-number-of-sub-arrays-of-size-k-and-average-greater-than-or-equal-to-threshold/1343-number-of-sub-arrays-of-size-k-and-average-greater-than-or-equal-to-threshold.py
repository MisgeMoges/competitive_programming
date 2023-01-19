class Solution:
     def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
      
        left,count = 0, 0
    
        _sum = sum(arr[:k])
        if _sum >= k*threshold:
            count = 1
        for right in range(k, len(arr)):
            _sum += arr[right]-arr[left]
            if _sum >= k*threshold:
                count += 1
            left += 1
        return count
                