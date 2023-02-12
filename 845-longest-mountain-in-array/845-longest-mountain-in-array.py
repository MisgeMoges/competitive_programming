class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        
        curLen = 1
        maxLen = 0
        goingUp = True

        for i in range(len(arr) - 1):
            # going up the mountain
            if goingUp and arr[i] < arr[i + 1]:  
                curLen += 1

            # going down the mountain
            elif curLen > 1 and arr[i] > arr[i + 1]:   
                goingUp = False
                curLen += 1
                if curLen >= 3:
                    maxLen = max(maxLen, curLen)
            
            # going up another mountain at the base of the last mountain
            elif not goingUp and arr[i] < arr[i + 1]:  
                curLen = 2
                goingUp = True
            
            # other invalid mountain status
            else:
                curLen = 1
            
        return maxLen